from flask import Flask, render_template, request, send_file
import sqlite3
from generate_pdf import create_pdf # type: ignore
import os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('bill.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            product TEXT,
            quantity INTEGER,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    customer = request.form['customer']
    product = request.form['product']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    conn = sqlite3.connect('bill.db')
    c = conn.cursor()
    c.execute('INSERT INTO bills (customer, product, quantity, price) VALUES (?, ?, ?, ?)',
              (customer, product, quantity, price))
    conn.commit()
    conn.close()

    total = quantity * price
    pdf_path = create_pdf(customer, product, quantity, price, total)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
