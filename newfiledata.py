from tkinter import *
import sqlite3
from tkinter import messagebox
root = Tk()
connect = sqlite3.connect("database.db")
c = connect.cursor()
'''
# Create Table
c.execute(""" CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text
) """)
'''
# Submit function
def submit():
    connect = sqlite3.connect("database.db")
    c = connect.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city)",
              {
                  'f_name': entry1.get(),
                  'l_name': entry2.get(),
                  'address': entry3.get(),
                  'city': entry4.get()
              })

    connect.commit()
    connect.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
# Show function
def show():
    connect = sqlite3.connect("database.db")
    c = connect.cursor()
    c.execute("SELECT *, oid FROM addresses ")
    records = c.fetchall()
    show_records = ''
    for record in records:
        show_records += str(record[4]) + "\t" + str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2]) + "\t" + str(record[3]) + "\n"
    show_label = Label(root, text=show_records)
    show_label.grid(row=9, column=1, columnspan=4)
    connect.commit()
    connect.close()
# Delete function
def delete():
    answer = messagebox.askyesno("Delete", "Are you sure?")
    if answer:
        connect = sqlite3.connect("database.db")
        c = connect.cursor()
        c.execute("DELETE from addresses WHERE oid= " + select_entry.get())
        c.execute("SELECT *, oid FROM addresses ")
        records = c.fetchall()
        show_records = ''
        for record in records:
            show_records += str(record[4]) + "\t" + str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2]) + "\t" + str(record[3]) + "\n"
        show_label = Label(root, text=show_records)
        show_label.grid(row=8, column=1, columnspan=4)
        connect.commit()
        connect.close()
    select_entry.delete(0, END)
# Update Function
def update():
    window = Toplevel(root)
    window.title("Update Details")
    label1 = Label(window, text="First Name : ")
    label1.grid(row=0, column=0)
    label2 = Label(window, text="Last Name : ")
    label2.grid(row=1, column=0)
    label3 = Label(window, text="Address : ")
    label3.grid(row=2, column=0)
    label4 = Label(window, text="City : ")
    label4.grid(row=3, column=0)
    entry1 = Entry(window)
    entry1.grid(row=0, column=1)
    entry2 = Entry(window)
    entry2.grid(row=1, column=1)
    entry3 = Entry(window)
    entry3.grid(row=2, column=1)
    entry4 = Entry(window)
    entry4.grid(row=3, column=1)
    update_button = Button(window, text="Update")
    update_button.grid(row=4, column=1, pady=10)

label1 = Label(root, text="First Name : ")
label1.grid(row=0, column=0)
label2 = Label(root, text="Last Name : ")
label2.grid(row=1, column=0)
label3 = Label(root, text="Address : ")
label3.grid(row=2, column=0)
label4 = Label(root, text="City : ")
label4.grid(row=3, column=0)
entry1 = Entry(root)
entry1.grid(row=0, column=1)
entry2 = Entry(root)
entry2.grid(row=1, column=1)
entry3 = Entry(root)
entry3.grid(row=2, column=1)
entry4 = Entry(root)
entry4.grid(row=3, column=1)
submit = Button(root, text="Submit", command=submit)
submit.grid(row=4, column=1, pady=5)
show_records = Button(root, text="Show Records",command=show)
show_records.grid(row=5, column=1, pady=5)
select_label = Label(root, text="Select ID : ")
select_label.grid(row=6, column=0)
select_entry = Entry(root)
select_entry.grid(row=6, column=1, pady=5, padx=20)
delete_button = Button(root, text = "Delete", command=delete)
delete_button.grid(row=7, column=1, pady=5, padx=20)
update_button = Button(root, text = "Update", command=update)
update_button.grid(row=8, column=1, pady=5, padx=20)
connect.commit()
connect.close()
root.mainloop()