import json
import csv
from flask import Flask, request, render_template

app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)

def read_json_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def read_csv_file(file_name):
    products = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error_message="Wrong source!")

    if product_id:
        product_id = int(product_id)
        filtered_products = [p for p in products if int(p['id']) == product_id]
        if not filtered_products:
            return render_template('product_display.html', error_message="Product not found!")
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
