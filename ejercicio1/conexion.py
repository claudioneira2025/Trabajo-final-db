from pymongo import MongoClient

uri = "mongodb+srv://claudioneiraneirasti_db_user:W3rN4hCADKT4L0ZI@cluster0.xevor6r.mongodb.net/"

cliente = MongoClient(uri)

db = cliente["mibase"]

vehiculos = db["vehiculos"]

print("Conexión exitosa")