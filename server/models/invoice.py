from pydantic import BaseModel
from typing import List, Optional

class InvoiceItem(BaseModel):
    name: str
    quantity: float
    batch: Optional[str] = None
    expiry: Optional[str] = None

class InvoiceResponse(BaseModel):
    supplier: str
    invoice_number: str
    date: str
    items: List[InvoiceItem]

class InvoiceParseRequest(BaseModel):
    irn: Optional[str] = None
    qr_data: Optional[str] = None
