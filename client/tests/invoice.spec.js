import { test, expect } from '@playwright/test';

test.describe('Structured Invoice Engine E2E', () => {
    test.beforeEach(async ({ page }) => {
        // Navigate to the React app
        await page.goto('/');
    });

    test('should display the main layout correctly', async ({ page }) => {
        // Assert the main header is visible
        await expect(page.locator('h1')).toHaveText('Structured Invoice Engine');

        // Assert the input form is visible
        await expect(page.locator('h2')).toHaveText('Input Invoice Data');

        // Check IRN and QR inputs
        await expect(page.getByLabel(/IRN/i)).toBeVisible();
        await expect(page.getByLabel(/QR Data/i)).toBeVisible();
        await expect(page.getByRole('button', { name: /Fetch Invoice/i })).toBeVisible();
    });

    test('should fetch and display invoice preview successfully', async ({ page }) => {
        // Mock the backend API response to avoid dependency on running the backend server for UI tests
        await page.route('/api/invoice/parse', async (route) => {
            const json = {
                supplier: "Test Health Supplies Ltd.",
                invoice_number: "INV-TEST-001",
                date: "2026-03-19",
                items: [
                    { name: "Test Paracetamol", quantity: 50, batch: "B-123", expiry: "2026-12-31" }
                ]
            };
            await route.fulfill({ json });
        });

        await page.getByLabel(/IRN/i).fill('1234567890');
        await page.getByRole('button', { name: /Fetch Invoice/i }).click();

        // Expect the preview section to appear
        await expect(page.locator('h2', { hasText: 'Invoice Preview' })).toBeVisible();

        // Expect supplier details
        await expect(page.locator('text=Test Health Supplies Ltd.')).toBeVisible();
        await expect(page.locator('text=INV-TEST-001')).toBeVisible();

        // Expect the mock items in the table
        // Because they are inputs, we need to check their values
        const itemNameInput = page.locator('tbody tr').first().locator('td').nth(0).locator('input');
        await expect(itemNameInput).toHaveValue('Test Paracetamol');

        const qtyInput = page.locator('tbody tr').first().locator('td').nth(1).locator('input');
        await expect(qtyInput).toHaveValue('50');
    });

    test('should support inline editing and trigger save', async ({ page }) => {
        // Mock the backend API response
        await page.route('/api/invoice/parse', async (route) => {
            const json = {
                supplier: "Test Health Supplies Ltd.",
                invoice_number: "INV-TEST-001",
                date: "2026-03-19",
                items: [
                    { name: "Demo Item", quantity: 1, batch: "", expiry: "" }
                ]
            };
            await route.fulfill({ json });
        });

        await page.getByLabel(/IRN/i).fill('1234567890');
        await page.getByRole('button', { name: /Fetch Invoice/i }).click();

        await expect(page.locator('h2', { hasText: 'Invoice Preview' })).toBeVisible();

        // Edit the quantity
        const qtyInput = page.locator('tbody tr').first().locator('td').nth(1).locator('input');
        await qtyInput.fill('100');
        await expect(qtyInput).toHaveValue('100');

        // Setup an event listener for the alert
        let dialogMessage = '';
        page.on('dialog', async dialog => {
            dialogMessage = dialog.message();
            await dialog.accept();
        });

        // Click Save
        await page.getByRole('button', { name: /Confirm & Save/i }).click();

        // Check alert message matches the stub behavior
        expect(dialogMessage).toBe("Phase 5: Confirm & Save Triggered");
    });
});
