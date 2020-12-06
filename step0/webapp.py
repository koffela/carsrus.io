from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#provide a route where requests on the web application can be addressed
#@webapp.route('/hello')
#provide a view (fancy name for a function) which responds to any requests on this route
#def hello():
#    return "Hello World!";

@webapp.route('/browse_cart')
#the name of this function is just a cosmetic thing. this is a sample query and I'm unsure if it's needed
def browse_cart():
    print("Fetching and rendering page")
    db_connection = connect_to_database()
    query = "SELECT * FROM cart;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('cart.html', rows=result)

@webapp.route('/insert_cart', methods=['POST','GET'])
def insert_cart():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT * FROM cart'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('cart.html', carts = result)
    elif request.method == 'POST':
        print("Add new cart!")
        cartID = request.form['cartID']
        productID = request.form['productID']
        totalCost = request.form['totalCost']
        quantity = request.form['quantity']

        query = "INSERT INTO cart (cartID, pid, totalCost, quantity) VALUES (%d, %d, %d, %d)"
        data = (cartID, (SELECT pid FROM products WHERE pid = productID), totalCost, quantity))
        execute_query(db_connection, query, data)
        return ('Cart added!')

#cart has insert and select done. inserting into cart requires a valid pid from products table

@webapp.route('/insert_order', methods=['POST','GET'])
def insert_order():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT * FROM orders'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('orders.html', orders = result)
    elif request.method == 'POST':
        print("Add new order!")
        orderNumber = request.form['orderNumber']
        cartID = request.form['cartID']
        finalPrice = request.form['finalPrice']
        query = "INSERT INTO orders (orderNumber, cartID, finalPrice) VALUES (%d, %d, %d)"
        data = (orderNumber, (SELECT cid FROM cart WHERE cid = cartID), totalCost, quantity))
        execute_query(db_connection, query, data)
        return ('Order added!')

#orders has insert and select done

@webapp.route('/insert_po', methods=['POST','GET'])
def insert_po():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT * FROM products_orders'
        result = execute_query(db_connection, query).fetchall()
        print(result)

        return render_template('products_orders.html', orders = result)
    elif request.method == 'POST':
        print("Add new product_order!")
        productID = request.form['productID']
        orderNumber = request.form['orderNumber']
        query = "INSERT INTO products_orders (productID, orderNumber) VALUES (%d, %d)"
        data = ((SELECT pid FROM products WHERE pid = productID), (SELECT orderNumber FROM orders WHERE orderNumber = orderNumber))
        execute_query(db_connection, query, data)
        return ('Products_order added!')