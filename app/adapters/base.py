from abc import ABC, abstractmethod
from app.models.invoice import InvoiceDataResponse

class GSPAdapter(ABC):
    """
    Base interface for all GSP (GST Suvidha Provider) adapters.
    Enforces the adapter pattern described in the architecture constraints.
    """
    @abstractmethod
    def fetch_invoice(self, irn: str) -> dict:
        pass