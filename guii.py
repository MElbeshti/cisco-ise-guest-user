
from tkinter import *
import sqlite3
import requests
import urllib3

root = Tk()
root.title('??????')
root.geometry('500x500')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

con = sqlite3.connect('ise-company1.db3')

#select company
def sql_select(comp1):

    c = con.cursor()
    #print("*******sql_select*******", comp1)
    c.execute('select name from company_name where company =?', (comp1,))
    con.commit()
    return comp1


# Count For All Name in Selected Company
def sql_count(comp1):

    c = con.cursor()
    c.execute('select count(*) from company_name where company =?', (comp1,))
    con.commit()
    rows = c.fetchall()
    #print("Total Number of Users In N Company", rows[0][0])
    return rows[0][0]


#select Name of User
#return (aa, nows)
def sql_name(status1):
 #   comp1 = show()
 #   print(comp1)

    c = con.cursor()
    c.execute('select name from company_name where company =?' , (str(show()),))
    rows = c.fetchall()
    nows = len(rows)
    #print("USEEEEEEEEEER", nows)
    if status1 == "reinstate":
        status1 = "reinstate"
        #print("----------------", status1)
    elif status1 == "suspend":
        status1 = "suspend"
        #print("****************",status1)

    for n in range(0, nows):
        print(n)
        for row in rows:
            aa = (rows[n][0])
            #print(aa)

        name1 = aa
        z = name1
        #print("UserName", z)
        url2 = "https://172.24.11.20:9060/ers/config/guestuser/" + status1 + "/name/" + z
        payload = {}
        headers2 = {
            'Accept': 'application/json',
            'cache-control': "no-cache",
            'Content-Type': 'application/json', }
        result2 = requests.request("PUT", url2, headers=headers2, data=payload, verify=False,
                                    auth=('ers', '123456*mM'))
        #print("This User Hasbeen", status1, z)
        con.commit()
        return z



# Query For All Company name
def company_query():
    con = sqlite3.connect('ise-company1.db3')
    c = con.cursor()
    c.execute("select DISTINCT company from company_name order by company")
    records = c.fetchall()
    cc = []
    for row in records:
        aa = (row[0])
        cc.append(aa)
    con.commit()
    con.close()
    return (cc)

# Function For showing Selected Company.

def show():
    myl2 = Label(root, text=str("----------------"), font=('Times New Roman', '18'), fg='white', bg='black')
    myl = Label(root, text=str(clickd.get()), font=('Times New Roman', '18'), fg='black', bg='white')
    a = myl["text"]
    #print("---------show---------",a)
    sql_select(a)
    sql_count(a)
    myl2.grid(row=3, column=0)
    myl.grid(row=3, column=0)
    return (a)


def show2():
    myl2 = Label(root, text=str("----------------"), font=('Times New Roman', '18'), fg='white', bg='black')
    myl = Label(root, text=str("reinstate"), font=('Times New Roman', '18'), fg='green', bg='white')
    s = myl["text"]
    sql_name(s)
    
    myl.grid(row=10, column=0)
    myl2.grid(row=15, column=0)
    
    cursorObj = con.cursor()
    cursorObj.execute('select name from company_name where company =?' , (show(),))
    con.commit()
    rows = cursorObj.fetchall()
    numb = int(len(rows))
    #print("-------------*-*-*-*-*", numb)
    a = []
    a.append(rows)
    #print(a)
    

    mytree = ttk.Treeview(root)
    
    mytree['columns'] = ("Name", "Bank")
    
    mytree.column("#0", width=0, minwidth=25)
    mytree.column("Name", anchor=W, width=120)
    
    mytree.column("Bank", anchor=W, width=120)
    
    mytree.heading("#0", text="", anchor=W)
    mytree.heading("Name", text="UserName", anchor=W)
    
    mytree.heading("Bank", text="Bank Name", anchor=W)

    for i in range(0, numb):
        for record in a:
            mytree.insert(parent='', index='end', iid=i, text="", values=(record[i], show()))
            
    #add data
    #mytree.insert(parent='', index='end', iid=0, text="Parent", values=(rows))
    mytree.grid(row=30, column=0)
    

    #print(s)


def show3():
    myl2 = Label(root, text=str("----------------"), font=('Times New Roman', '18'), fg='white', bg='black')
    myl1 = Label(root, text=str("suspend"), font=('Times New Roman', '18'), fg='red', bg='white')
    r = myl1["text"]
    sql_name(r)
    
    myl1.grid(row=20, column=0)
    myl2.grid(row=25, column=0)
    
    cursorObj = con.cursor()
    cursorObj.execute('select name from company_name where company =?' , (show(),))
    con.commit()
    rows = cursorObj.fetchall()
    
    mytree = ttk.Treeview(root)
    
    mytree['columns'] = ("Name", "ID", "Bank")
    
    mytree.column("#0", width=120, minwidth=25)
    mytree.column("Name", anchor=W, width=120)
    mytree.column("ID", anchor=CENTER, width=80)
    mytree.column("Bank", anchor=W, width=120)
    
    mytree.heading("#0", text="Label", anchor=W)
    mytree.heading("Name", text="UserName", anchor=W)
    mytree.heading("ID", text="ID", anchor=CENTER)
    mytree.heading("Bank", text="Bank Name", anchor=W)
    
    #add data
    mytree.insert(parent='', index='end', iid=0, text="Parent", values=(rows,))
    mytree.grid(row=40, column=0)
    

    #print(r)

'''
def show4():

    
    mytree = ttk.Treeview(root)
    
    mytree['columns'] = ("Name", "ID", "Bank")
    
    mytree.column("#0", width=120, minwidth=25)
    mytree.column("Name", anchor=W, width=120)
    mytree.column("ID", anchor=CENTER, width=80)
    mytree.column("Bank", anchor=W, width=120)
    
    mytree.heading("#0", text="Label", anchor=W)
    mytree.heading("Name", text="UserName", anchor=W)
    mytree.heading("ID", text="ID", anchor=CENTER)
    mytree.heading("Bank", text="Bank Name", anchor=W)
    
    #add data
    mytree.insert(parent='', index='end', iid=0, text="Parent", values=(username))
    mytree.grid(row=40, column=0)
'''
clickd = StringVar()
clickd.set([company_query()[0]])
p = (clickd.set([company_query()[0]]))

clickA = StringVar()

clickB = StringVar()


#print(p)

drp = OptionMenu(root, clickd, *company_query())
drp.grid(row=0, column=0)


myb = Button(root, text="Show Selection", command=show)
myb.grid(row=6, column=0)


myb2 = Button(root, text="Active Users", command=show2)
myb2.grid(row=7, column=0)

myb3 = Button(root, text="Disable Users", command=show3)
myb3.grid(row=8, column=0)
'''
myb4 = Button(root, text="show", command=show4)
myb4.grid(row=10, column=0)
'''

count1 = sql_count(show())
print('****************************', count1)

'''
#print(show())
#companyname = input("Bank_name:")
status1 = str(input("susbend a or active b\t:"))
#comp1 = companyname
#sql_select(con, comp1)
#count1 = sql_count()
suspend = "a"
reinstate = "b"
if status1 == suspend:
   status1 = "suspend"
   print("Confirming of Users Status", status1)
else:
   status1 = "reinstate"
   print("Confirming of Users Status", status1)
count2 = int(count1)
print("TOTAL", count2)
'''


