from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql

def bookRegister():

    ## When the user clicks the submit button this bookRegister function is run 
    # BookInfos are stored in these variables.
    # and then these are uploaded to the database using the cursor method of pymysql 
    # 

    bookid = bookInfo1.get()
    title = bookInfo2.get()
    title = title.upper()
    author = bookInfo3.get()
    author = author.upper()
    status = bookInfo4
    

    insertBook = "insert into "+bookTable+" values('"+bookid+"','"+title+"','"+author+"','"+status+"')"
    print(insertBook)    ### debug purpose
    
    try:
        cur.execute(insertBook)
        con.commit()
        messagebox.showinfo("Success","Added the book successfully")

    except:
        messagebox.showinfo("Error","Cant add to Database, errors occurred")

    print(bookid)
    print(title)
    print(author)   ###### debug purposes
    print(status)

    root.destroy()

def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
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
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#050300",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='yellow', fg='blue', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)  ## creates the text entry  box 
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    bookInfo4 = 'avail'
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='red',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='red', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()