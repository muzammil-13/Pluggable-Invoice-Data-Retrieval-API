from fastapi import APIRouter, Depends
from app.models.invoice import InvoiceDataRequest, InvoiceDataResponse
from app.services.invoice_processing import InvoiceProcessingService

router = APIRouter()

@router.post("/invoice-data", response_model=InvoiceDataResponse)
async def get_invoice_data(
    request: InvoiceDataRequest,
    service: InvoiceProcessingService = Depends(InvoiceProcessingService)
):
    """Accepts an invoice file and returns structured data."""
    return await service.process_invoice(request)