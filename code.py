import sqlite3

class Database:
    def __init__(self, db):
        self.conn= sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Books(id INTEGER PRIMARY KEY, Title text, Author text, Year integer, ISBN integer)")
        self.conn.commit()


    def insert(self,Title, Author, Year, ISBN):
        self.conn.execute("INSERT INTO Books VALUES (NULL,?,?,?,?)" , (Title, Author, Year, ISBN))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows=self.cur.fetchall()
        return rows

    def search(self, Title="",Author="",Year="",ISBN=""):
        self.cur.execute("SELECT * FROM books WHERE Title=? OR Author=? OR Year=? OR ISBN=?", (Title,Author,Year,ISBN))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM books WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id, Title, Author, Year, ISBN):
        self.cur.execute("UPDATE books SET Title=?,Author=?,Year=?,ISBN=? WHERE id=?", (Title,Author,Year,ISBN,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


#connect()
#delete(4)
#update(1,"Game of Thrones", "George R R Martin", 1996, 9789646807815)
#insert("Percy Jackson and Lightning Theif", "Rick Rirdan", 2005, 9845613204576)
#print(search(Author="George R R Martin"))
#print(view())
