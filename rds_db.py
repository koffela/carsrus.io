import pymysql
import db_credentials as rds
conn = pymysql.connect(
        host = rds.host,
        port = rds.port,
        user = rds.user,
        password = rds.password,
        db = rds.db,
)

#table has already been created, so create the functions

def insert_vehicle(cartID, productID, totalCost, quantity):
    cur = conn.cursor()
    #%s is incorrect. need to fix for integers.
    cur.execute("INSERT INTO cart (cartID, pid, totalCost, quantity) VALUES (%d, %d, %d, %d)", (cartID, (SELECT productID FROM products WHERE productID = productID), totalCost, quantity))
    conn.commit()

def get_vehicles():
    cur.conn.cursor()
    cur.execute("SELECT * FROM cart")
    allVehicles = cur.fetchall()
    return allVehicles