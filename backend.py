import sqlite3

def connect(): 
    conn=sqlite3.connect("BookData.db")
    cur=conn.cursor()
    cur.execute("Create Table if not exists Book(id integer primary key,title text,author text,year integer, isbn integer,genre text,price integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn,genre,price):
    conn=sqlite3.connect("BookData.db")
    cur=conn.cursor()
    cur.execute("Insert INTO Book VALUES(NULL,?,?,?,?,?,?)",(title,author,year,isbn,genre,price))
    conn.commit()
    conn.close()

def display():
    conn=sqlite3.connect("BookData.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn="",genre="",price=""):
    conn=sqlite3.connect("BookData.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Book WHERE title=? OR author=? OR year=? OR isbn=? OR genre=? OR price=?",(title,author,year,isbn,genre,price))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("BookData.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn,genre,price):
    conn=sqlite3.connect("BookData.db")
    cur=conn.cursor()
    cur.execute("UPDATE Book SET title=?,author=?,year=?,isbn=?,genre=?,price=? WHERE id=?",(title,author,year,isbn,genre,price,id))
    conn.commit()
    conn.close()

def isbn(id):
    conn=sqlite3.connect("BookData.db")
    cur=conn.cursor()
    cur.execute("SELECT isbn FROM Book WHERE id=?",(id,))
    rows=cur.fetchall()
    conn.close()
    return rows

connect() 