import sqlite3

class Database:
    def __init__(self, db):
        conn= sqlite3.connect(db)
        cur=conn.cursor()
        conn.execute("CREATE TABLE IF NOT EXISTS Books(id INTEGER PRIMARY KEY, Title text, Author text, Year integer, ISBN integer)")
        conn.commit()
        conn.close()

    def insert(Title, Author, Year, ISBN):
        conn= sqlite3.connect("books.db")
        cur=conn.cursor()
        conn.execute("INSERT INTO Books VALUES (NULL,?,?,?,?)" , (Title, Author, Year, ISBN))
        conn.commit()
        conn.close()

    def view():
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM books")
        rows=cur.fetchall()
        conn.close()
        return rows

    def search(Title="",Author="",Year="",ISBN=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM books WHERE Title=? OR Author=? OR Year=? OR ISBN=?", (Title,Author,Year,ISBN))
        rows=cur.fetchall()
        conn.close()
        return rows

    def delete(id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM books WHERE id=?", (id,))
        conn.commit()
        conn.close()

    def update(id, Title, Author, Year, ISBN):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE books SET Title=?,Author=?,Year=?,ISBN=? WHERE id=?", (Title,Author,Year,ISBN,id))
        conn.commit()
        conn.close()

#connect()
#delete(4)
#update(1,"Game of Thrones", "George R R Martin", 1996, 9789646807815)
#insert("Percy Jackson and Lightning Theif", "Rick Rirdan", 2005, 9845613204576)
#print(search(Author="George R R Martin"))
#print(view())
