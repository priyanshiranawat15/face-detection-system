from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x1309+0+0")
        self.root.title("Developer")
        
        title_label=Label(self.root,text="Developer", font=("times new roman",35,"bold"),bg="black",fg="white")
        title_label.place(x=0,y=0,width=1590,height=45)
        
        imgtop=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/dev.png")
        imgtop=imgtop.resize((1590,720),Image.Resampling.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)
        
        
        f_label=Label(self.root,image=self.photoimgtop)
        f_label.place(x=0,y=55,width=1590,height=720)

        #Frame
        main_frame=Frame(f_label,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        imgtop1=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/pri.jpg")
        imgtop1=imgtop1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimgtop1=ImageTk.PhotoImage(imgtop1)
        
        
        f_label=Label(main_frame,image=self.photoimgtop1)
        f_label.place(x=300,y=0,width=200,height=200)
        
        # developer info
        dev_label=Label(main_frame,text="Hello my name is PRIYANSHI RANAWAT",font=("time new roman",14,"bold"),bg="white",fg="black")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am full stack developer",font=("time new roman",14,"bold"),bg="white",fg="black")
        dev_label.place(x=0,y=40)
        
        img2=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/stulap.jpeg")
        img2=img2.resize((500,390),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_label=Label(main_frame,image=self.photoimg2)
        f_label.place(x=0,y=210,width=500,height=390)
        






if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()