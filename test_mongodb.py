from pymongo import MongoClient

# import pymongo
client = MongoClient("mongodb://localhost:27017/")
# client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.1")

# castro de pessoas num dicionario
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "Luanda"
}

db = client['Cadastro']
colecao = db['Cadastro_pessoa']
colecao.insert_one(pessoa)

resultado = colecao.find()
print(resultado)
# print(client.list_database_names())
print(client.list_database_names())
print(db.list_collection_names())

for r in resultado:
    print(r)