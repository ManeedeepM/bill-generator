from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import uuid
import os

def create_pdf(customer, product, quantity, price, total):
    filename = f"{uuid.uuid4().hex}.pdf"
    filepath = os.path.join("generated", filename)
    os.makedirs("generated", exist_ok=True)

    c = canvas.Canvas(filepath, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 750, f"Customer: {customer}")
    c.drawString(100, 730, f"Product: {product}")
    c.drawString(100, 710, f"Quantity: {quantity}")
    c.drawString(100, 690, f"Price per item: ₹{price}")
    c.drawString(100, 670, f"Total: ₹{total}")
    c.drawString(100, 630, f"Thank you for your purchase!")

    c.save()
    return filepath
