# 🤖 AI Development Instructions: Smart Receipt Uploader → Structured Invoice Engine

## 🎯 Goal

Upgrade this project from an OCR-based receipt tool into a **structured invoice processing engine** aligned with real-world systems like healthcare inventory workflows.

Focus:
- Move away from OCR-first approach
- Introduce structured data ingestion (GST QR / IRN / APIs)
- Build a clean pipeline: **Invoice → Structured Data → Actionable UI**

---

## 🧠 Core Principle

> AI is a coding assistant, NOT the decision maker.

- All architecture, flow, and decisions must be human-defined
- AI should only assist in:
  - writing boilerplate
  - generating test cases
  - suggesting optimizations

---

## 🔄 System Evolution Plan

### Phase 1: Refactor Input Layer

#### Current:
- Image/PDF upload
- OCR extraction (Tesseract/EasyOCR)

#### Target:
- Accept structured inputs:
  - GST QR string (JWT)
  - IRN (Invoice Reference Number)
  - Mock JSON (for development)

#### Tasks:
- Create new API endpoint:
```

POST /invoice/parse

````
- Input:
```json
{
  "irn": "string",
  "qr_data": "string"
}
````

* Output:

  ```json
  {
    "supplier": "",
    "invoice_number": "",
    "date": "",
    "items": [
      {
        "name": "",
        "quantity": 0,
        "batch": "",
        "expiry": ""
      }
    ]
  }
  ```

---

### Phase 2: Mock Data Engine (IMPORTANT)

Since real GST APIs may not be accessible:

* Build a mock service:

  ```
  /services/mock_invoice_service.py
  ```

* AI Task:

  * Generate realistic invoice JSON datasets
  * Cover edge cases:

    * missing fields
    * invalid formats
    * multiple items

---

### Phase 3: Data Mapping Layer

Create transformation logic:

```
invoice → internal schema
```

Example:

* normalize item names
* validate quantity
* handle missing expiry/batch

#### File:

```
/services/invoice_mapper.py
```

---

### Phase 4: UI Upgrade (React)

#### Add new flow:

1. Input IRN / QR
2. Click "Fetch Invoice"
3. Display:

   * structured invoice preview
   * editable fields

#### Components:

* `InvoiceInput.jsx`
* `InvoicePreview.jsx`
* `EditableTable.jsx`

---

### Phase 5: Assisted Workflow (NOT FULL AUTO)

Important:

> Do NOT auto-save blindly.

Instead:

* Pre-fill fields
* Allow user edits
* Add “Confirm & Save” step

---

### Phase 6: Optional External API Integration

ONLY after mock works:

* Add pluggable API layer:

```
/services/invoice_provider.py
```

* Design interface:

```python
class InvoiceProvider:
    def fetch_invoice(irn: str) -> dict:
        pass
```

---

### Phase 7: Testing (HIGH PRIORITY)

#### Backend:

* Use pytest
* Test:

  * parsing
  * mapping
  * edge cases

#### Frontend:

* Add basic interaction tests

---

## 🧱 Folder Structure (Target)

```
server/
 ├── main.py
 ├── routes/
 │    └── invoice.py
 ├── services/
 │    ├── mock_invoice_service.py
 │    ├── invoice_mapper.py
 │    └── invoice_provider.py
 └── models/

client/
 ├── components/
 │    ├── InvoiceInput.jsx
 │    ├── InvoicePreview.jsx
 │    └── EditableTable.jsx
 └── pages/
```

---

## ⚙️ AI Usage Guidelines

### ✅ Use AI for:

* generating API boilerplate
* writing test cases
* suggesting UI structure
* refactoring repetitive code

### ❌ Do NOT use AI for:

* architecture decisions
* blindly generating full features
* copying large chunks without review

---

## 🧪 Validation Checklist

Before marking any feature complete:

* [ ] API returns structured JSON
* [ ] UI displays editable invoice data
* [ ] Edge cases handled (missing fields)
* [ ] No OCR dependency for core flow
* [ ] Code is readable and modular

---

## 🚀 End Vision

This project should evolve into:

> A modular invoice processing system that can plug into real-world workflows like healthcare inventory, replacing manual data entry with structured, assisted input.

---

## 🧭 Future Extensions

* CARE HMIS integration (inventory APIs)
* Multi-invoice batch processing
* Analytics dashboard (sales, stock trends)
* Authentication & user roles
* Export to ERP systems

---

## 📝 Final Note

Keep the system:

* simple
* modular
* demoable

Shipping a small working flow is better than designing a perfect system that never runs.

```
