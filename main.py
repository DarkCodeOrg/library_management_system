from tkinter import *
from PIL import  ImageTk,Image # PIL is the pillow module
import pymysql 
from tkinter import messagebox 

#from AddBook import *
#from DeleteBook import *
#from ViewBooks import *
#from IssueBook import *
#from ReturnBook import *

# Add your own database name and password here to reflect in the code
mypass = "abc_123"
mydatabase="library_db"

con = pymysql.connect(host="localhost",user="librarian",password=mypass,database=mydatabase)   ## this creates 
cur = con.cursor()