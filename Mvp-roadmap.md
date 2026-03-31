# 🛣️ MVP Roadmap

## Invoice Data Retrieval System (GSoC 2026)

---

## 🎯 Goal

Build a **working MVP** that can:

> Accept an invoice → extract IRN (if available) → return structured invoice data via API.

The focus is on:

* correctness over perfection
* API-first delivery
* real-world usability

---

## 🧩 Development Strategy

Each phase delivers a  **usable milestone** , not just code.

* Every 2–3 weeks → working feature
* Continuous testing with real invoices
* Keep system modular and pluggable

---

# 🚀 Phase 1 (Weeks 1–3)

## IRN Extraction Pipeline + API Foundation

### 🎯 Objective

Build the **core ingestion + IRN extraction pipeline**

---

### 🔧 Tasks

* Implement PDF → image conversion
* Implement QR code detection (OpenCV / pyzbar)
* Decode JWT from QR payload
* Extract IRN from decoded data

---

### 🌐 API

* Create basic API skeleton:

```http
POST /invoice-data
```

* Accept:
  * PDF / image input
* Return:
  * raw QR data
  * extracted IRN

---

### ✅ Deliverable

* Working API that:
  * accepts invoice
  * extracts IRN successfully

---

### ⚠️ Risks

* QR not detected → add preprocessing
* invalid JWT → log + debug samples

---

# 🚀 Phase 2 (Weeks 4–6)

## GSP Adapter + IRN Data Retrieval

### 🎯 Objective

Enable **structured invoice retrieval via IRN**

---

### 🔧 Tasks

* Design adapter interface:

```python
class GSPAdapter:
    def fetch_invoice(self, irn: str) -> dict:
        pass
```

* Implement:
  * mock adapter (for testing)
  * initial real API integration (if accessible)
* Normalize API response into common format

---

### 🌐 API Upgrade

Return:

```json
{
  "source": "irn",
  "invoice_number": "...",
  "items": [...]
}
```

---

### ✅ Deliverable

* IRN → structured invoice data working
* Adapter-based architecture ready

---

### ⚠️ Risks

* API access restrictions
  👉 Mitigation:
* use mock + pluggable adapters

---

# 🚀 Phase 3 (Weeks 7–9)

## Fallback + Validation Layer

### 🎯 Objective

Ensure **system reliability when IRN fails**

---

### 🔧 Tasks

* Integrate fallback parsing engine
* Extract:
  * items
  * quantities
  * pricing
* Implement validation:
  * total vs sum(items)
  * required fields check
* Add confidence scoring

---

### 🌐 API Upgrade

```json
{
  "source": "fallback",
  "items": [...],
  "confidence": 0.82
}
```

---

### ✅ Deliverable

* System works even without IRN
* Reliable output with confidence score

---

### ⚠️ Risks

* parsing inconsistency
  👉 Mitigation:
* limit scope to key fields only

---

# 🚀 Phase 4 (Weeks 10–12)

## Integration + Testing + Finalization

### 🎯 Objective

Deliver **end-to-end usable system**

---

### 🔧 Tasks

* Simulate CARE HMIS integration:
  * API call → structured data → stock entry
* Test with:
  * multiple invoice formats
  * real-world samples
* Optimize:
  * performance
  * error handling
* Write documentation:
  * setup guide
  * API usage
  * architecture explanation

---

### ✅ Deliverable

* Fully working MVP
* Integration demo
* Clean documentation

---

### 📊 Success Criteria

* IRN extraction success rate
* API response accuracy
* fallback reliability
* ease of integration

---

# 📦 Final MVP Output

At the end of GSoC, the system will:

* accept invoice (PDF/image)
* extract IRN when available
* fetch structured invoice data via API
* fallback when necessary
* return clean JSON response

---

# 💡 Development Principles

* Build small, test fast
* Avoid unnecessary complexity
* Prioritize API stability
* Keep system pluggable

---

# ⚡ Final Note

This roadmap focuses on:

> Delivering a working, integration-ready system, not just a prototype.

---