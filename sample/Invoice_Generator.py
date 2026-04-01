import os
from pathlib import Path
import json
import base64
import io
from datetime import datetime
import qrcode
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_jwt_payload(irn):
    """Generates a fictional JWT string containing the IRN."""
    header = base64.b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()).decode().strip("=")
    payload = base64.b64encode(json.dumps({"data": {"Irn": irn}}).encode()).decode().strip("=")
    signature = base64.b64encode(b"fictional_secret_signature").decode().strip("=")
    return f"{header}.{payload}.{signature}"

def create_invoice(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    elements = []
    styles = getSampleStyleSheet()
    
    # --- 1. Data Setup ---
    irn = "5db8e7f1a3c2b9d8e7f1a3c2b9d8e7f1a3c2b9d8e7f1a3c2b9d8e7f1a3c2b9d8"
    invoice_no = "MSD-2024-0789"
    today = datetime.now().strftime("%d-%m-%Y")
    
    # --- 2. QR Code Generation ---
    jwt_data = generate_jwt_payload(irn)
    qr = qrcode.QRCode(box_size=2, border=1)
    qr.add_data(jwt_data)
    qr.make(fit=True)
    qr_img_io = io.BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_img_io, format='PNG')
    qr_img_io.seek(0)
    qr_reportlab = Image(qr_img_io, 1*inch, 1*inch)

    # --- 3. Header Section (Supplier & QR) ---
    supplier_info = Paragraph(
        "<b>MedSupply Distributors</b><br/>"
        "123 Pharma Estate, Peenya Industrial Area<br/>"
        "Bengaluru, Karnataka - 560058<br/>"
        "GSTIN: 29AAAAA0000A1Z5", styles['Normal']
    )
    
    header_table = Table([[supplier_info, qr_reportlab]], colWidths=[4.5*inch, 1.5*inch])
    header_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('ALIGN', (1,0), (1,0), 'RIGHT')]))
    elements.append(header_table)
    elements.append(Spacer(1, 12))

    # --- 4. Buyer & Invoice Details ---
    buyer_info = [
        [Paragraph("<b>Bill To:</b>", styles['Normal']), Paragraph(f"<b>Invoice No:</b> {invoice_no}", styles['Normal'])],
        [Paragraph("General Hospital Pharmacy", styles['Normal']), Paragraph(f"<b>Date:</b> {today}", styles['Normal'])],
        [Paragraph("456 Health City, Whitefield, Bengaluru", styles['Normal']), Paragraph(f"<b>IRN:</b> {irn[:32]}...", styles['Normal'])],
        [Paragraph("GSTIN: 29BBBBB1111B1Z5", styles['Normal']), ""]
    ]
    info_table = Table(buyer_info, colWidths=[3.5*inch, 2.5*inch])
    elements.append(info_table)
    elements.append(Spacer(1, 20))

    # --- 5. Items Table ---
    # Column Headers
    data = [['S.No', 'Description of Goods', 'HSN', 'Batch', 'Expiry', 'Qty', 'Rate', 'Amount']]
    
    # Sample Products
    items = [
        ['1', 'Paracetamol 500mg (10x10)', '3004', 'BT2201', '12/2026', '100', '15.50', '1550.00'],
        ['2', 'Amoxicillin 250mg (10x10)', '3004', 'AMX993', '08/2027', '50', '42.00', '2100.00'],
        ['3', 'Azithromycin 500mg (3 Tabs)', '3004', 'AZI442', '05/2026', '200', '65.00', '13000.00']
    ]
    data.extend(items)

    # Calculations
    subtotal = sum(float(item[7]) for item in items)
    cgst = subtotal * 0.09
    sgst = subtotal * 0.09
    grand_total = subtotal + cgst + sgst

    # Add Totals to Table
    data.append(['', '', '', '', '', '', 'Subtotal', f"{subtotal:,.2f}"])
    data.append(['', '', '', '', '', '', 'CGST (9%)', f"{cgst:,.2f}"])
    data.append(['', '', '', '', '', '', 'SGST (9%)', f"{sgst:,.2f}"])
    data.append(['', '', '', '', '', '', 'Grand Total', f"INR {grand_total:,.2f}"])

    item_table = Table(data, colWidths=[0.4*inch, 1.8*inch, 0.6*inch, 0.7*inch, 0.7*inch, 0.5*inch, 0.6*inch, 0.8*inch])
    item_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('GRID', (0,0), (-1, -5), 0.5, colors.grey),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (1,1), (1,-5), 'LEFT'), # Align description to left
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (-2, -1), (-1, -1), 'Helvetica-Bold'), # Bold Grand Total
        ('BACKGROUND', (-2, -1), (-1, -1), colors.lightgrey),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    elements.append(item_table)

    # --- 6. Footer ---
    elements.append(Spacer(1, 40))
    terms = "<b>Terms and Conditions:</b><br/>1. Goods once sold will not be taken back.<br/>2. Interest @18% will be charged if payment is not made within 30 days.<br/>3. Subject to Bengaluru Jurisdiction."
    elements.append(Paragraph(terms, styles['Normal']))

    # Build PDF
    doc.build(elements)
    print(f"File created successfully: {filename}")

if __name__ == "__main__":
    # This gets the directory where the current script (e.g., generator.py) is located
    script_dir = Path(__file__).parent.absolute()
    
    # Define the full path for the output file
    target_path = script_dir / "sample.pdf"
    
    print(f"Targeting directory: {script_dir}")
    
    # Call your function with the full absolute path
    create_invoice(str(target_path))