from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "abc_123"
mydatabase="library_db"

con = pymysql.connect(host="localhost",user="librarian",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
memTable = "members"

def searchMem():

    memname = memInfo1.get()
    memname = memname.upper()
    
    searchSql = "select memid,name from "+memTable+" where name like '%"+memname+"%'"

    root1 = Tk()
    root1.title("Library")
    root1.minsize(width=400,height=400)
    root1.geometry("600x500")


    Canvas2 = Canvas(root1) 
    Canvas2.config(bg="#12a4d9")
    Canvas2.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Search Members", bg='yellow', fg='blue', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-40s"%('Member ID','Name'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="-------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    
    try:
        cur.execute(searchSql)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s"%(i[0],i[1]),bg='white',fg='black').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    root1.mainloop()
    memInfo1.delete(0, END)
    

def search():

    global memInfo1,Canvas1,con,cur,memTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Search Member", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Member name to search
    lb2 = Label(labelFrame,text="Member Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    memInfo1 = Entry(labelFrame)
    memInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=searchMem)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()