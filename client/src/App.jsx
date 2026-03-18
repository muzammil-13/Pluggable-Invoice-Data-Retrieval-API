import React, { useState } from 'react';
import InvoiceInput from './components/InvoiceInput';
import InvoicePreview from './components/InvoicePreview';

function App() {
    const [invoiceData, setInvoiceData] = useState(null);

    const handleFetchInvoice = async (inputData) => {
        try {
            // Fetching from FastAPI backend
            const response = await fetch('/api/invoice/parse', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    irn: inputData.irn || null,
                    qr_data: inputData.qr_data || null
                })
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || "Failed to fetch invoice");
            }

            const data = await response.json();
            setInvoiceData(data);
        } catch (error) {
            console.error("Error fetching invoice:", error);
        }
    };

    const handleSave = () => {
        alert("Phase 5: Confirm & Save Triggered");
    };

    return (
        <div className="max-w-4xl mx-auto p-8">
            <h1 className="text-3xl font-bold mb-8">Structured Invoice Engine</h1>
            <InvoiceInput onFetchInvoice={handleFetchInvoice} />
            <InvoicePreview invoiceData={invoiceData} onSave={handleSave} />
        </div>
    );
}

export default App;
