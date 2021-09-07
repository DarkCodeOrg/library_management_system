from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def memRegister():
    
    memid = memInfo1.get()
    name = memInfo2.get()
    address = memInfo3.get()
    Aadhar = memInfo4.get()
    DateOfIssue = memInfo5.get()
    
    insertMem = "insert into "+memTable+" values('"+memid+"','"+name+"','"+address+"','"+Aadhar+"','"+DateOfIssue+"')"
    try:
        cur.execute(insertMem)
        con.commit()
        messagebox.showinfo('Success',"Member added successfully")
    except:
        messagebox.showinfo("Error","Can't add member into Database, MemID already exists")
    
    #print(memid)
    #print(name)
    #print(address)      Debug purposes
    #print(Aadhar)
    #print(DateOfIssue)

    root.destroy()
    
def addMem(): 
    
    global memInfo1,memInfo2,memInfo3,memInfo4,memInfo5,Canvas1,con,cur,memTable,root
    
    root = Tk()  ##this creates a gui window 
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "abc_123"
    mydatabase="library_db"
    
    con = pymysql.connect(host="localhost",user="librarian",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    memTable = "members" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#050300",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='yellow', fg='blue', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Member ID
    lb1 = Label(labelFrame,text="Member ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    memInfo1 = Entry(labelFrame)  ## creates the text entry  box 
    memInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    memInfo2 = Entry(labelFrame)
    memInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Member Address
    lb3 = Label(labelFrame,text="Address : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    memInfo3 = Entry(labelFrame)
    memInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Member Aadhar Number
    lb4 = Label(labelFrame,text="Aadhar_no : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
         
    memInfo4 = Entry(labelFrame)
    memInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    # Member Date OF Issue
    lb5 = Label(labelFrame,text="Date Of Issue of member : ",bg='black',fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)

    memInfo5 = Entry(labelFrame)
    memInfo5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)    
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='red',command=memRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='red', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()