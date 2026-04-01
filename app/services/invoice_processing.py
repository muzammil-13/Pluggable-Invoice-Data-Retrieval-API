from app.models.invoice import InvoiceDataRequest, InvoiceDataResponse, InvoiceItem
from app.adapters.mock_adapter import MockGSPAdapter # Will be replaced by a dynamic factory

class InvoiceProcessingService:
    """
    Orchestrates the invoice data retrieval process according to the layered architecture.
    """
    def __init__(self):
        # In the future, this will be a factory that selects the right adapter
        self.gsp_adapter = MockGSPAdapter()

    async def process_invoice(self, request: InvoiceDataRequest) -> InvoiceDataResponse:
        """
        Executes the main logic:
        1. Phase 1: Extract QR -> Decode JWT -> Get IRN.
        2. Phase 2: If IRN exists, use GSP adapter.
        3. Phase 3: If IRN fails, use fallback parser.
        """
        # --- Placeholder Logic ---
        # TODO: Implement Phase 1 QR/IRN extraction here.
        mock_irn = "mock_irn_from_qr_code"

        # TODO: Implement Phase 2 dynamic adapter selection.
        # For now, we directly use the mock adapter if an IRN is "found".
        if mock_irn:
            gsp_data = self.gsp_adapter.fetch_invoice(mock_irn)
            return InvoiceDataResponse(
                source="gsp",
                invoice_number=gsp_data.get("invoice_number"),
                items=[InvoiceItem(**item) for item in gsp_data.get("items", [])],
                confidence=0.95 # High confidence for API-based data
            )
        
        # TODO: Implement Phase 3 fallback logic here.
        return InvoiceDataResponse(source="fallback", confidence=0.0)