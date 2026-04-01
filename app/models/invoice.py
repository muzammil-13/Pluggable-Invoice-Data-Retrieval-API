from pydantic import BaseModel, Field
from typing import List, Optional

class InvoiceItem(BaseModel):
    name: str
    quantity: int
    batch: Optional[str] = None
    expiry: Optional[str] = None

class InvoiceDataRequest(BaseModel):
    file: str = Field(..., description="Base64 encoded string of the PDF/image")
    provider: Optional[str] = Field(None, description="Optional GSP provider identifier (e.g., 'cleartax')")

class InvoiceDataResponse(BaseModel):
    source: str = Field(..., description="'irn' | 'gsp' | 'fallback'")
    invoice_number: Optional[str] = None
    items: List[InvoiceItem] = []
    confidence: float = Field(0.0, description="Confidence score of the extraction (0.0 to 1.0)")

