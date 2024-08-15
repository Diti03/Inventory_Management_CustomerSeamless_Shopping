''' from flask import Flask

newpy = Flask(__name__)

@newpy.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    #newpy.run(debug=True)
    newpy.run(debug=True, port=5001) '''





from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

newpy = Flask(__name__)
CORS(newpy)

# Database connection
conn = psycopg2.connect(
    database="Inventory_Management",
    user="postgres",
    password="apurva26",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

@newpy.route('/', methods=['GET'])
def index():
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Products ";')
    rows = cur.fetchall()
    cur.close() 
    categories = [{"product_id": row[0], "product_name": row[1]} for row in rows]
    return jsonify(categories)


@newpy.route('/api/categories', methods=['GET'])
def get_categories():
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Products ";')
    rows = cur.fetchall()
    cur.close()

    categories = [{"product_id": row[0], "product_name": row[1]} for row in rows]
    return jsonify(categories)

if __name__ == '__main__':
    newpy.run(debug=True , port=5001)

    
'''
@newpy.route('/Categories', methods=['GET'])
def get_categories():
    try:
        cursor.execute('SELECT * FROM public."Categories"')
        categories = cursor.fetchall()
        return jsonify(categories)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@newpy.route('/Products/<int:product_name>', methods=['GET'])
def get_products_by_category(product_name):
    try:
        cursor.execute('SELECT * FROM public."Products" WHERE product_name = %s', (product_name,))
        products = cursor.fetchall()
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@newpy.route('/Products', methods=['GET'])
def get_filtered_products():
    try:
        category_id = request.args.get('category_id')
        size = request.args.get('size')
        color = request.args.get('color')
        cursor.execute(
            'SELECT * FROM public."Products" WHERE category_id = %s AND size = %s AND color = %s',
            (category_id, size, color)
        )
        Products = cursor.fetchall()
        return jsonify(Products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    newpy.run(debug=True , port=5001) '''



