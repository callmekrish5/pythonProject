from tkinter import *
import sqlite3

root=Tk()
root.title('Database Address Book')

conn=sqlite3.connect('address_book.db')
c=conn.cursor()
'''
c.execute("""CREATE TABLE open (
   first_name text,
   last_name text,
   address text,
   city text,
   state text,
   zipcode integer
)""")
print("Table created sucessfully")
'''
'''
def submit():
    conn=sqlite3.connect('address_book.db')

    c=conn.cursor()

c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",{

  'f_name':f_name.get(),
  'l_name': l_name.get(),
  'address':address.get(),
  'city':city.get(),
  'state':state.get(),
  'zipcode':zipcode.get(),
 })
print('Address created sucessfully')


conn.commit()
conn.close() #clear the text boxes
f_name.delete(0,END)
l_name.delete(0,END)
address.delete(0,END)
city.delete(0,END)
state.delete(0,END)
zipcode.delete(0,END)


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record +=str(record)+"\n"

        query_label = label(root, text=print_record)
        query_label.grid(row=9,column=0,colunmspan=2)

    conn.commit()

    conn.close()
'''

#Create text boxes
f_name=Entry(root,width=40)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=40)
l_name.grid(row=1,column=1)
address=Entry(root,width=40)
address.grid(row=2,column=1)
city=Entry(root,width=40)
city.grid(row=3,column=1)
state=Entry(root,width=40)
state.grid(row=4,column=1)
zipcode=Entry(root,width=40)
zipcode.grid(row=5,column=1)
#Create textbox labels
f_name_label=Entry(root,text="First Name")
f_name_label.grid(row=0,column=0)
l_name_label=Entry(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label=Entry(root,text="Address")
address_label.grid(row=2,column=0)
city_label=Entry(root,text="City")
city_label.grid(row=3,column=0)
state_label=Entry(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label=Entry(root,text="Zip Code")
zipcode_label.grid(row=5,column=0)
#create submit button
submit_btn=Button(root,text="Add Return")
submit_btn.grid(row=6,column=0,columnspan=3)
conn.commit()

conn.close()
mainloop()
