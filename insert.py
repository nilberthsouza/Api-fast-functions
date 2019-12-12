from db import Database
db = Database("Store.db")

def insert(t,b):
    db.insert(t,b)
    print(t,b)
    return "inserido com sucesso"
