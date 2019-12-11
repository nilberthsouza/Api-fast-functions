from db import Database
db = Database('Store.db')

def notes(i):
    print(i)
    a = list(db.fetch())
    return a

