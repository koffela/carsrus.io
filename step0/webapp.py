from flask import Flask, render_template
from flask import request, redirect, render_template,
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#provide a route where requests on the web application can be addressed
#@webapp.route('/hello')
#provide a view (fancy name for a function) which responds to any requests on this route
#def hello():
#    return "Hello World!";

@webapp.route('/')
def index():
    return render_template('index.html')

@webapp.route('/cart')
def cart():
    return render_template('cart.html')

@webapp.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        cartID = request.form['cartID']
        productID = request.form['productID']
        totalCost = request.form['totalCost']
        quantity = request.form['quantity']
        db.insert_vehicle(cartID, productID, totalCost, quantity)
        vehicles = db.get_vehicles()
        print(vehicles)
        for vehicle in vehicles:
            var = vehicle
        return render_template('cart.html', var = var)