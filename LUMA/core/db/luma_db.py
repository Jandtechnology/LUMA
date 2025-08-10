from pymongo import MongoClient

# Conectar con MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["luma"]
coleccion = db["luma"]

# Guardar un programa
def guardar_programa(programa):
    result = coleccion.insert_one(programa)
    print(f"✅ Programa guardado con ID: {result.inserted_id}")

# Obtener todos los programas
def obtener_todos_programas():
    return list(coleccion.find())
