from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Student import student
import os
import subprocess
from time import strftime
from datetime import datetime
import platform
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helps import Help
import tkinter
class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x1209+0+0")
        self.root.title("Face recognition system")
        
        #first image
        img=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Stanford.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/face.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/college.webp")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        
        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=1000,y=0,width=500,height=130)
        
        
        #bg image
        img3=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/bg.webp")
        img3=img3.resize((1590,1209),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1590,height=1209)
        
        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="black",fg="white")
        title_label.place(x=0,y=0,width=1590,height=45)
        
        #Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl = Label(title_label,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        #student button
        img4=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/student.jpeg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="brown")
        b1_1.place(x=200,y=310,width=220,height=40)
        
        
        #Detect face button
        
        img5=Image.open("360_F_629815969_fP8umPrlXV8MhFYPU54YEhcGo0TgMSIk.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="brown")
        b1_1.place(x=500,y=310,width=220,height=40)
        
        #Attendance face button
        
        img6=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/attendance.jpeg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="brown")
        b1_1.place(x=800,y=310,width=220,height=40)
        
        #Help button
        
        img7=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/customercare.png")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Customer Care",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="black",fg="brown")
        b1_1.place(x=1100,y=310,width=220,height=40)
        
        #Train button
        
        img8=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/traindata.png")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="brown")
        b1_1.place(x=200,y=600,width=220,height=40)
        
        #Photos button
        
        img9=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/photo.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="brown")
        b1_1.place(x=500,y=600,width=220,height=40)
        
        #Developer button
        
        img10=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/developer.png")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="black",fg="brown")
        b1_1.place(x=800,y=600,width=220,height=40)
        
        #Exit button
        
        img11=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/exit.png")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="black",fg="brown")
        b1_1.place(x=1100,y=600,width=220,height=40)
        
    
    
    def open_img(self):
        path = "/Users/priyanshiranawat/AttendanceSystemManagement/Data"
    
        if platform.system() == 'Windows':
            os.startfile(path)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.call(['open', path])
        else:  # Linux
            subprocess.call(['xdg-open', path])

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure about exiting this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
# Function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    
