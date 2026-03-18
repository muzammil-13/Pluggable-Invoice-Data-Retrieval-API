# MVP Roadmap: Structured Invoice Processing Engine

This roadmap outlines the evolution from an OCR-based system to a structured invoice processing engine aligned with real-world workflows (e.g., healthcare inventory), as detailed in the project's AI instructions.

---

## Phase 1: Input Layer Refactoring
**Goal:** Shift away from OCR-first approaches towards generic structured data ingestion.

- [x] Create project boilerplate and repo structure
- [x] Define API endpoint `POST /invoice/parse`
- [ ] Implement input validation for structured data:
  - GST QR strings (JWT format)
  - IRN (Invoice Reference Number)
  - Mock JSON fallback

## Phase 2: Mock Data Engine
**Goal:** Build a robust mock service to simulate real GST APIs for development.

- [x] Scaffold `/services/mock_invoice_service.py`
- [ ] Generate realistic invoice JSON datasets mimicking different scenarios
- [ ] Cover edge cases:
  - Missing fields (e.g., missing batch/expiry)
  - Invalid formats
  - Multi-item invoices

## Phase 3: Data Mapping Layer
**Goal:** Map external API structures to the internal database schema.

- [x] Scaffold `/services/invoice_mapper.py`
- [ ] Create transformation logic (e.g., `raw_invoice_data -> internal_schema`)
- [ ] Implement standard normalization rules:
  - Normalize item/drug names
  - Validate and convert quantity types
  - Handle missing batch and expiry fallbacks

## Phase 4: UI Upgrade (React)
**Goal:** Build a frontend flow to parse internal data structures and display them.

- [x] Build `InvoiceInput.jsx` (Form to capture IRN / QR data)
- [x] Build `InvoicePreview.jsx` (Component to display structured invoice overview)
- [x] Build `EditableTable.jsx` (Tabular display of line items)
- [ ] Wire up components to the FastAPI `/api/invoice/parse` backend

## Phase 5: Assisted Workflow 
**Goal:** Ensure humans stay in the loop. Prevent blind auto-saves.

- [ ] Ensure pre-filling works for all mapped fields
- [ ] Enable in-line editing in the `EditableTable.jsx`
- [ ] Implement a "Confirm & Save" action to commit verified data to the database

## Phase 6: External API & Integrations
**Goal:** Hook the application up to real data providers once the mock cycle is verified.

- [x] Scaffold `/services/invoice_provider.py`
- [ ] Write integration logic for the real GST API / Provider
- [ ] Create interface definition for `fetch_invoice(irn: str) -> dict`

## Phase 7: Testing & Polish
**Goal:** Ensure the pipeline is robust and test-driven.

- [ ] Write Backend Tests (`pytest`):
  - API parsing validation
  - Data mapping functions
  - Various edge cases
- [ ] Write Frontend Tests:
  - Basic interaction tests (fetching, editing, saving)
- [ ] Deploy MVP (Vercel & Railway)

---

## Future Extensions & Vision
- Integrate directly with CARE HMIS inventory APIs
- Multi-invoice batch processing
- Authentication and User Roles
- Analytics dashboard (Stock trends and Sales)
- Formats export to ERP systems
