# 🤖 AI Instructions for Development

## Invoice Data Retrieval System (GSoC 2026)

---

## 🎯 Purpose

This document guides AI-assisted development for this project.

The goal is to ensure that any AI-generated code or suggestions:

* align with project architecture
* follow the API-first design
* remain simple, modular, and production-aware
* do not introduce unnecessary complexity

---

## 🧠 Project Context

This project builds a **pluggable invoice data retrieval system** for healthcare workflows.

Core objective:

> Given an invoice (PDF/image), return structured invoice data using IRN-based retrieval as the primary method.

---

## 🧩 System Architecture

The system follows a layered approach:

1. QR extraction → JWT decoding → IRN
2. IRN-based retrieval via GST/GSP APIs
3. Adapter-based provider system
4. Fallback parsing (only if needed)
5. Unified API response

AI-generated code must respect this architecture.

---

## ⚠️ Core Constraints

### 1. API-first approach

* Do NOT default to OCR-first solutions
* IRN-based retrieval is the primary path

---

### 2. Keep it pluggable

* Avoid hardcoding provider logic
* Use adapter-based design

---

### 3. Avoid overengineering

* No unnecessary microservices
* No heavy frameworks beyond requirement

---

### 4. Python-first backend

* Use Python for all core logic
* Prefer lightweight frameworks (FastAPI or minimal service layer)

---

## 🧱 Coding Guidelines

### General

* Write modular, readable functions
* Use clear naming (no abbreviations)
* Add docstrings for key functions

---

### Structure

Recommended structure:

```id=
app/
  api/
  services/
  adapters/
  utils/
```

---

### API Design

* Use REST endpoints
* Accept file input (PDF/image)
* Return structured JSON

---

### Error Handling

* Always handle:
  * missing QR
  * invalid JWT
  * API failures

Return meaningful responses, not crashes.

---

## 🔌 Adapter Pattern Rules

All provider integrations must follow:

```python
class GSPAdapter:
    def fetch_invoice(self, irn: str) -> dict:
        raise NotImplementedError
```

* No direct API calls in core logic
* All providers must be interchangeable

---

## 🔄 Fallback Logic Rules

Fallback parsing should:

* only trigger when IRN/API fails
* not replace primary logic
* be clearly marked in response (`source: fallback`)

---

## 📦 Output Format (Strict)

All responses must follow:

```json
{
  "source": "irn | gsp | fallback",
  "invoice_number": "...",
  "items": [],
  "confidence": 0.0
}
```

---

## ❌ What AI should NOT do

* Do NOT introduce UI/frontend code
* Do NOT rewrite entire architecture
* Do NOT use heavy ML models unless explicitly required
* Do NOT bypass adapter pattern
* Do NOT hardcode credentials or API keys

---

## ✅ What AI SHOULD focus on

* QR extraction logic
* JWT decoding
* clean API endpoints
* adapter implementations
* validation and error handling

---

## 🧪 Testing Expectations

AI-generated code should include:

* basic test cases
* sample inputs (PDF/image)
* edge case handling

---

## 💡 Development Philosophy

* Build small, test quickly
* Prefer working prototype over perfect design
* Keep everything simple and extensible

---

## ⚡ Final Instruction

When generating code, always ask:

> “Does this align with IRN-first, API-first, pluggable design?”

If not, simplify and correct.

---

# 🚀 Usage

This file is intended for:

* AI coding assistants
* contributors
* future maintainers

---

## 🧠 Reminder

This project solves a  **real operational problem** , not a demo.

Focus on:

* reliability
* simplicity
* integration readiness

---