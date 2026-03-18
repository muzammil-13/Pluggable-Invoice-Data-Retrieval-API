import React, { useState } from 'react';

const InvoiceInput = ({ onFetchInvoice }) => {
  const [irn, setIrn] = useState('');
  const [qrData, setQrData] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onFetchInvoice({ irn, qr_data: qrData });
  };

  return (
    <div className="p-4 border rounded-lg bg-white shadow-sm mb-6">
      <h2 className="text-xl font-bold mb-4">Input Invoice Data</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">IRN (Invoice Reference Number)</label>
          <input
            type="text"
            className="w-full p-2 border rounded"
            value={irn}
            onChange={(e) => setIrn(e.target.value)}
            placeholder="Enter IRN..."
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">QR Data (JWT or raw string)</label>
          <textarea
            className="w-full p-2 border rounded"
            rows="3"
            value={qrData}
            onChange={(e) => setQrData(e.target.value)}
            placeholder="Paste QR string..."
          />
        </div>
        <button type="submit" className="bg-blue-600 text-white p-2 rounded hover:bg-blue-700 transition">
          Fetch Invoice
        </button>
      </form>
    </div>
  );
};

export default InvoiceInput;
