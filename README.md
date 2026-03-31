# 📄 Pluggable Invoice Data Retrieval API

### IRN-first, API-driven invoice extraction for CARE HMIS

---

## 🚀 Why this exists

Hospital pharmacists spend significant time manually entering invoice data into systems like CARE HMIS.

Each invoice requires:

* medicine names
* quantities
* batch numbers
* expiry dates

This is repetitive, error-prone, and slows down operations.

At the same time, modern GST invoices already contain:

* a **QR code (JWT)**
* an **IRN (Invoice Reference Number)**
* access to **structured invoice data via APIs**

👉 The problem is not data availability
👉 The problem is **data accessibility inside workflows**

---

## 🎯 Objective

Build a **simple, reliable API** that returns structured invoice data from input documents.

This API is designed to:

* eliminate manual entry for pharmacists
* plug into CARE HMIS workflows
* remain flexible across hospitals and GST providers

---

## 🧠 Design Philosophy

This project is built on three principles:

### 1. API-first, not OCR-first

We prioritize **trusted, structured data sources (IRN APIs)** over extraction.

---

### 2. Pluggable, not opinionated

Hospitals can use their own:

* GST providers
* credentials
* integrations

---

### 3. Reliable, not perfect

When ideal paths fail, the system gracefully falls back instead of breaking.

---

## 🧩 System Overview

A layered approach ensures both accuracy and reliability:

### 🔹 1. IRN-based Retrieval (Primary Path)

* Extract QR code from invoice
* Decode JWT → obtain IRN
* Fetch structured invoice JSON via:
  * GST APIs
  * GSP providers

✅ High accuracy
✅ Authenticated data
✅ Zero manual parsing

---

### 🔹 2. GSP Adapter Layer

Supports multiple providers via pluggable adapters:

```python
class GSPAdapter:
    def fetch_invoice(self, irn: str) -> dict:
        raise NotImplementedError
```

* ClearTax (example)
* Other GSP APIs

👉 Enables vendor flexibility without code changes

---

### 🔹 3. Fallback Parsing Layer (Controlled Use)

If IRN/API retrieval is unavailable:

* Use structured parsing engine (existing system)
* Extract key invoice fields

⚠️ This is intentionally **not the primary path**
⚠️ Used only to ensure system continuity

---

### 🔹 4. Unified API Interface

```http
POST /invoice-data
```

#### Request

```json
{
  "file": "<pdf/image>",
  "provider": "optional_gsp"
}
```

#### Response

```json
{
  "source": "irn | gsp | fallback",
  "invoice_number": "INV-123",
  "items": [
    {
      "name": "Paracetamol 500mg",
      "quantity": 100,
      "batch": "B123",
      "expiry": "2027-05"
    }
  ],
  "confidence": 0.93
}
```

---

## 🏗️ Architecture

```
                Invoice Input (PDF/Image)
                          │
                  QR Extraction Layer
                          │
                  JWT Decode → IRN
                          │
              ┌───────────┴───────────┐
              │                       │
        IRN Available           IRN Not Available
              │                       │
      GST / GSP API Fetch      Fallback Parsing
              │                       │
              └───────────┬───────────┘
                          │
                 Unified API Response
```

---

## 🔌 Plug-Based Integration Model

This system follows OHC’s preferred  **plug architecture** :

* No vendor lock-in
* No credential ownership by the platform
* Hospitals configure their own providers

Example:

```yaml
provider: cleartax
api_key: XXXX
fallback_enabled: true
```

---

## 🏥 CARE HMIS Alignment

This API is designed to integrate directly with CARE workflows:

* Provides structured data for stock entry
* Enables automation of:
  * `/api/v1/supply_delivery/`
* Supports:
  * first-time inventory creation
  * repeat stock updates

👉 Focus is on  **data availability** , not UI replacement

---

## ⚠️ Constraints & Trade-offs

* GST APIs may require:
  * authentication
  * paid access
* Not all invoices include IRN
* API availability may vary across hospitals

👉 This is why fallback exists, but is not the default path

---

## 📦 Current Status

This project evolves from:

> **Structured Invoice Processing Engine**

Enhancements include:

* IRN extraction pipeline
* adapter-based API integration
* unified API interface
* healthcare-specific data modeling

---

## 🛠️ GSoC Scope (Proposed)

### Phase 1

* QR extraction + JWT decoding
* IRN identification

### Phase 2

* GSP adapter design (mock + real integration)
* API endpoint implementation

### Phase 3

* fallback parsing integration
* confidence scoring

### Phase 4

* CARE HMIS integration demo
* real-world invoice testing

---

## 💡 Impact

* Reduces manual effort for pharmacists
* Improves accuracy of stock entry
* Enables scalable hospital operations
* Bridges GST infrastructure with healthcare systems

---

## 📬 Context

This project is being developed in response to:

> OHC’s open challenge on automating pharmacy invoice workflows using GST IRN data

---

## 🤝 Contributions

Looking for:

* GST API research
* GSP adapter implementations
* real invoice datasets
* CARE integration validation

---

# ⚡ Final Note

This project is intentionally scoped to solve  **one core problem well** :

> “Given an invoice, return structured, reliable data.”

Everything else is built around that.

---
