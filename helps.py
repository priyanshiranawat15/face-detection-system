from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x1309+0+0")
        self.root.title("Help")
        
        title_label=Label(self.root,text="Help Desk", font=("times new roman",35,"bold"),bg="black",fg="white")
        title_label.place(x=0,y=0,width=1590,height=45)
        
        imgtop=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/customercare.png")
        imgtop=imgtop.resize((1590,720),Image.Resampling.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)
        
        
        f_label=Label(self.root,image=self.photoimgtop)
        f_label.place(x=0,y=55,width=1590,height=720)
        
        help_label=Label(f_label,text="Email:pri@yahoo.com",font=("time new roman",30,"bold"),bg="white",fg="black")
        help_label.place(x=600,y=400)




if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()