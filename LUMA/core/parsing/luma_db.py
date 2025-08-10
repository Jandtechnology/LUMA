from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.luma
collection = db.programs

def guardar_programa(program_json: dict):
    result = collection.insert_one(program_json)
    print(f"✅ Guardado en MongoDB con ID: {result.inserted_id}")
