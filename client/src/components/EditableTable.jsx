import React, { useState } from 'react';

const EditableTable = ({ initialItems = [] }) => {
    const [items, setItems] = useState(initialItems);

    const handleChange = (index, field, value) => {
        const updatedItems = [...items];
        updatedItems[index][field] = value;
        setItems(updatedItems);
    };

    return (
        <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
                <thead>
                    <tr className="bg-gray-100">
                        <th className="p-2 border">Item Name</th>
                        <th className="p-2 border">Quantity</th>
                        <th className="p-2 border">Batch</th>
                        <th className="p-2 border">Expiry</th>
                    </tr>
                </thead>
                <tbody>
                    {items.map((item, index) => (
                        <tr key={index} className="hover:bg-gray-50">
                            <td className="p-2 border">
                                <input
                                    type="text"
                                    className="w-full p-1 border rounded"
                                    value={item.name || ''}
                                    onChange={(e) => handleChange(index, 'name', e.target.value)}
                                />
                            </td>
                            <td className="p-2 border">
                                <input
                                    type="number"
                                    className="w-full p-1 border rounded"
                                    value={item.quantity || 0}
                                    onChange={(e) => handleChange(index, 'quantity', Number(e.target.value))}
                                />
                            </td>
                            <td className="p-2 border">
                                <input
                                    type="text"
                                    className="w-full p-1 border rounded bg-yellow-50"
                                    value={item.batch || ''}
                                    onChange={(e) => handleChange(index, 'batch', e.target.value)}
                                    placeholder="Missing Batch?"
                                />
                            </td>
                            <td className="p-2 border">
                                <input
                                    type="date"
                                    className="w-full p-1 border rounded bg-yellow-50"
                                    value={item.expiry || ''}
                                    onChange={(e) => handleChange(index, 'expiry', e.target.value)}
                                />
                            </td>
                        </tr>
                    ))}
                    {items.length === 0 && (
                        <tr>
                            <td colSpan="4" className="p-4 text-center text-gray-500">No items found</td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default EditableTable;
