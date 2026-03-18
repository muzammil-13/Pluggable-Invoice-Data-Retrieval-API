import React from 'react';
import EditableTable from './EditableTable';

const InvoicePreview = ({ invoiceData, onSave }) => {
    if (!invoiceData) return null;

    return (
        <div className="p-4 border rounded-lg bg-white shadow-sm">
            <h2 className="text-xl font-bold mb-4">Invoice Preview</h2>

            <div className="grid grid-cols-2 gap-4 mb-6">
                <div>
                    <p className="text-sm text-gray-500">Supplier</p>
                    <p className="font-medium">{invoiceData.supplier}</p>
                </div>
                <div>
                    <p className="text-sm text-gray-500">Invoice Number</p>
                    <p className="font-medium">{invoiceData.invoice_number}</p>
                </div>
                <div>
                    <p className="text-sm text-gray-500">Date</p>
                    <p className="font-medium">{invoiceData.date}</p>
                </div>
            </div>

            <div className="mb-6">
                <h3 className="text-lg font-semibold mb-2">Items</h3>
                {/* Phase 5: Assisted Workflow - Pre-fill fields, allow user edits */}
                <EditableTable initialItems={invoiceData.items} />
            </div>

            <div className="flex justify-end">
                <button
                    onClick={onSave}
                    className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
                >
                    Confirm & Save
                </button>
            </div>
        </div>
    );
};

export default InvoicePreview;
