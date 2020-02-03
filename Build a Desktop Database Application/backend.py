import sqlite3


def Connect():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def Insert(title,author,year,isbn):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def View():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows


def Search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows


def Delete(id):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()


def Update(id,title,author,year,isbn):
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


Connect()
Insert("How to be a Bawse","Lilly singh",2017,9780718186913)
Insert("Harry Potter And the Cursed Child","J.K Rowling",2016,9780751565355)
Insert("The Time Keeper","Mitch Albom",2013,9780751541182)


print(Search(author="J.K Rowling"))

print(View())
