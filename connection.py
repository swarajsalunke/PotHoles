# import pyodbc
# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="geoapiExercises")

# conn = pyodbc.connect('DRIVER={SQL Server};'
#                       'SERVER=tcp:locationserver1.database.windows.net,1433;'
#                       'DATABASE=location; UID=swaraj; PWD=Password@123;')

# cursor = conn.cursor()
# cursor.execute("SELECT latitude,longitude FROM roadconditiondb")
# all = cursor.fetchall()
# cursor.execute("SELECT TOP 1* FROM roadconditiondb ORDER BY id DESC;")
# row = cursor.fetchall()
# lati = row[0][1]
# long = row[0][2]
# location = geolocator.reverse(str(lati)+","+str(long))
# # while row:
# print(all)
# # print(len(all))
# # print (row)
#     # row = cursor.fetchone()


# return render_template("index.html")
