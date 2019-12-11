import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS notes( id INTEGER PRIMARY KEY AUTOINCREMENT, title text,body text)")
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT *FROM notes")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, body):
        self.cur.execute("INSERT INTO notes VALUES(Null,?,?)",(title,body))
        self.conn.commit()
    def remove(self,id):
        self.cur.execute("DELETE FROM notes WHERE id=?",(id,))
        self.conn.commit()
    def select(self,id):
        self.cur.execute("SELECT FROM notes WHERE id=?",(id,))
        self.conn.commit()
    def update(self,id,title,body):
        self.cur.execute("UPDATE notes SET title=?,body=? WHERE id = ?",(title,body))
    def __del__(self):
        self.conn.close()

db = Database("Store.db")
db.insert("teste titulo 1","asdiaosdjiajsidojaisodjaijsdoaisjdaiosjd")
db.insert("teste titule 2","ksaldkjasjdkalsjdakjsdlkajsdkjakldsjaksj")

