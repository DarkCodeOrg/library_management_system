from tkinter import *
from PIL import  ImageTk,Image # PIL is the pillow module
import pymysql 
from tkinter import messagebox 

from AddBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from AddMember import *
from DeleteMember import *
from ViewMembers import *
from SearchMember import *
from SearchBook import *



# Add your own database name and password here to reflect in the code
mypass = "abc_123"
mydatabase="library_db"

con = pymysql.connect(host="localhost",user="librarian",password=mypass,database=mydatabase)   ## this creates 
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=1.5

# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.06,relwidth=0.6,relheight=0.14)

headingLabel = Label(headingFrame1, text="Welcome to \n Harnett High School Library", bg='#c3ff00', fg='#ff3b00', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='#c3ff00', fg='#ff3b00', command=addBook)
btn1.place(relx=0.28,rely=0.28, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="View Book List",bg='#c3ff00', fg='#ff3b00', command=View)
btn2.place(relx=0.28,rely=0.38, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Issue Book to Member",bg='#c3ff00', fg='#ff3b00', command = issueBook)
btn3.place(relx=0.28,rely=0.48, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="Return Book",bg='#c3ff00', fg='#ff3b00', command = returnBook)
btn4.place(relx=0.28,rely=0.58, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Issue new member",bg='#c3ff00', fg='#ff3b00', command= addMem)
btn5.place(relx=0.28,rely=0.68, relwidth=0.45,relheight=0.1)

btn6 = Button(root,text="Delete member",bg='#c3ff00', fg='#ff3b00', command= delete)
btn6.place(relx=0.28,rely=0.78, relwidth=0.45,relheight=0.1)

btn7 = Button(root,text="View members",bg='#c3ff00', fg='#ff3b00', command= ViewMem)
btn7.place(relx=0.28,rely=0.88, relwidth=0.45,relheight=0.1)

## Left 
btn8 = Button(root,text="DAILY CHECK",bg='#c3ff00', fg='#ff3b00')#, command= Check)
btn8.place(relx=0.05,rely=0.58, relwidth=0.20,relheight=0.1)

## Right
btn8 = Button(root,text="Search Member",bg='#c3ff00', fg='#ff3b00', command= search)
btn8.place(relx=0.75,rely=0.53, relwidth=0.20,relheight=0.1)

btn9 = Button(root,text="Search Book",bg='#c3ff00', fg='#ff3b00', command= search1)
btn9.place(relx=0.75,rely=0.63, relwidth=0.20,relheight=0.1)

root.mainloop()
