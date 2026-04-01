from app.adapters.base import GSPAdapter
import uuid

class MockGSPAdapter(GSPAdapter):
    """
    A mock implementation of the GSPAdapter for Phase 2 testing,
    ensuring the API can return data without hitting a real external GST service.
    """
    
    def fetch_invoice(self, irn: str) -> dict:
        return {
            "source": "gsp",
            "invoice_number": f"INV-{str(uuid.uuid4())[:8].upper()}",
            "items": [
                {
                    "name": "Mocked Paracetamol 500mg",
                    "quantity": 100,
                    "batch": "B123",
                    "expiry": "2027-05"
                }
            ]
        }