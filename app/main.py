from fastapi import FastAPI
from app.api.endpoints import router as invoice_router

app = FastAPI(
    title="Pluggable Invoice Data Retrieval API",
    description="IRN-first, API-driven invoice extraction for CARE HMIS.",
    version="0.1.0"
)

app.include_router(invoice_router, prefix="/api/v1", tags=["Invoice Processing"])

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Welcome to the Pluggable Invoice Data Retrieval API. See /docs for details."}