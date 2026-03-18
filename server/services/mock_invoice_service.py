from models.invoice import InvoiceParseRequest, InvoiceResponse, InvoiceItem
from datetime import datetime
import uuid

class MockInvoiceService:
    def generate_mock_invoice(self, request: InvoiceParseRequest) -> InvoiceResponse:
        """
        AI Task: Generate realistic invoice JSON datasets, covering edge cases:
        missing fields, invalid formats, multiple items.
        """
        # A simple mocked successful response for development
        return InvoiceResponse(
            supplier="Mock Health Supplies Ltd." if request.irn else "QR Pharma Wholesale",
            invoice_number=f"INV-{str(uuid.uuid4())[:8].upper()}",
            date=datetime.now().strftime("%Y-%m-%d"),
            items=[
                InvoiceItem(name="Paracetamol 500mg", quantity=100, batch="BATCH123", expiry="2025-12-31"),
                InvoiceItem(name="Amoxicillin 250mg", quantity=50, batch="BATCH456", expiry="2024-10-31"),
                InvoiceItem(name="Surgical Masks (Box of 50)", quantity=10), # Missing batch/expiry edge case
            ]
        )
