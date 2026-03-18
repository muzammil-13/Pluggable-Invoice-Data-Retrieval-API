from fastapi import APIRouter, HTTPException
from models.invoice import InvoiceParseRequest, InvoiceResponse
from services.mock_invoice_service import MockInvoiceService

router = APIRouter(prefix="/invoice", tags=["Invoice"])
mock_service = MockInvoiceService()

@router.post("/parse", response_model=InvoiceResponse)
def parse_invoice(request: InvoiceParseRequest):
    if not request.irn and not request.qr_data:
        raise HTTPException(status_code=400, detail="Must provide irn or qr_data")
    
    # Using mock service for Phase 2 as per ai_instructions
    try:
        invoice_data = mock_service.generate_mock_invoice(request)
        return invoice_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
