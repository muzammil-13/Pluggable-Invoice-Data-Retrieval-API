from fastapi import FastAPI
from routes import invoice

app = FastAPI(title="Structured Invoice Processing Engine")

app.include_router(invoice.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to Structured Invoice Processing Engine"}
