from db import Database
db =  Database("Store.db")


def seleciona(num):
    row = db.select(num)
    return row
