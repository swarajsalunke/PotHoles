from flask import Flask, request, render_template
# from flask_mysqldb import MySQL
from geopy.geocoders import Nominatim
# import pyodbc
import firebase_admin
import requests
import polyline

from firebase_admin import credentials, db

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'tracker'

# conn = pyodbc.connect('DRIVER={SQL Server};'
#                       'SERVER=tcp:locationserver1.database.windows.net,1433;'
#                       'DATABASE=location;\
#                        UID=swaraj;\
#                        PWD=Password@123;')

# mysql = MySQL(app)

geolocator = Nominatim(user_agent="geoapiExercises")

# server = 'potholeserver.database.windows.net'
# database = 'potholesSQL'
# username = 'ojaspal'
# password = 'Ojas@1234'

# driver_name = 'ODBC Driver 17 for SQL Server'
# conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"

# Connect to the database
# conn = pyodbc.connect(conn_str)
cred = credentials.Certificate(
    'pothole-image-db-firebase-adminsdk-dkjle-4712d586c9.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pothole-image-db-default-rtdb.firebaseio.com/',
})


@app.route('/')
def home():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM vehicle_details")
    # data = cur.fetchall()
    # cur.close()
    # """"
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT latitude,longitude FROM roadconditiondb")
    #     all = cursor.fetchall()
    #     length = len(all)

    #     cursor.execute("SELECT TOP 1* FROM roadconditiondb ORDER BY id DESC;")
    #     row = cursor.fetchall()
    #     lati = row[0][1]
    #     long = row[0][2]
    ref = db.reference('/')
    data = ref.get()
    x = 0
    for d in data:
        x = x+1

    for i in range(x):
        var = 'test' + str(i)
        lati = data[var]['Lat']
        long = data[var]['Lon']

    location = geolocator.reverse(str(lati)+","+str(long))
    #     return render_template("index.html",lati = lati, long = long, location = location, all = all, length = length)
    # """
    # users = db.child("users").get()
    # for user in users.each():
    #     print(user.val())

    # cred = credentials.Certificate(
    #     'pothole-image-db-firebase-adminsdk-dkjle-4712d586c9.json')

    # # Initialize the app with a custom auth variable, limiting the server's access
    # firebase_admin.initialize_app(cred, {
    #     'databaseURL': 'https://pothole-image-db-default-rtdb.firebaseio.com/',
    # })

    ref = db.reference('/')
    data = ref.get()

    return render_template("index.html", data=data, location = location)


@app.route('/main')
def maps():
    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM vehicle_details")
    # data = cur.fetchall()
    # cur.close()

    # cursor = conn.cursor()
    # cursor.execute("SELECT latitude,longitude FROM roadconditiondb")
    # all = cursor.fetchall()
    # length = len(all)

    # cursor.execute("SELECT TOP 1* FROM roadconditiondb ORDER BY id DESC;")
    # row = cursor.fetchall()
    # lati = row[0][1]
    # long = row[0][2]

    ref = db.reference('/')
    data = ref.get()
    x = 0
    for d in data:
        x = x+1

    for i in range(x):
        var = 'test' + str(i)
        lati = data[var]['Lat']
        long = data[var]['Lon']
        
    location = geolocator.reverse(str(lati)+","+str(long))

    # return render_template("maps.html", lati=lati, long=long)#, location=location, all=all, length=length)
    arr1 = []
    arr2 = []
    arr3 = []

    x = 0
    for d in data:
        x = x+1

    for i in range(x):
        var = 'test' + str(i)
        lati = data[var]['Lat']
        arr1.append(lati)
        long = data[var]['Lon']
        arr2.append(long)
        string = data[var]['String']
        arr3.append(string)
    
    link = arr3[x-1]

    return render_template("maps.html", lati=lati, long=long, arr1=arr1,arr2=arr2, arr3 = arr3, link = link , location=location)
    # return render_template("maps.html")


@app.route('/streetView')
def street():
    # cursor = conn.cursor()
    # # cursor.execute("SELECT * FROM roadconditiondb")
    # cursor.execute("SELECT TOP 1* FROM roadconditiondb ORDER BY id DESC;")
    # row = cursor.fetchall()
    # lati = row[0][1]
    # long = row[0][2]
    ref = db.reference('/')
    data = ref.get()
    x = 0
    for d in data:
        x = x+1

    for i in range(x):
        var = 'test' + str(i)
        lati = data[var]['Lat']
        long = data[var]['Lon']
    return render_template("street/street.html", lati=lati, long=long)
# return render_template("street/street.html")


if __name__ == "__main__":
    app.run(debug=True)
