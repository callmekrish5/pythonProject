from tkinter import*
import sqlite3

root=Tk()

def query():
    conn = sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("SELECT*,oid FROM addresses")
    records=c.fetchhall()
    print(records)
    conn.commit()
    conn.close()