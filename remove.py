from db import Database
db = Database("Store.db")

def remove(num):
    db.remove(num)
    return "removido com sucesso"

