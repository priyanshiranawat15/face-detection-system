from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x1309+0+0")
        self.root.title("Attendance management system")
        
        # variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        #first image
        img=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s1.jpeg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=800,height=200)
        
        #second image
        img1=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s2.jpeg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=800,y=0,width=800,height=200)
        
        #bg image
        img3=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/bg.webp")
        img3=img3.resize((1590,1209),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1590,height=1209)
        
        title_label=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="black",fg="white")
        title_label.place(x=0,y=0,width=1590,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="brown")
        main_frame.place(x=10,y=55,width=1590,height=1100)
        
        #Left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="brown",relief=RIDGE,text="Student attendance details",font=("time new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=710,height=700)
        
        imgleft=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s4.jpeg")
        imgleft=imgleft.resize((700,130),Image.Resampling.LANCZOS)
        self.photoimgleft=ImageTk.PhotoImage(imgleft)
        
        f_label=Label(left_frame,image=self.photoimgleft)
        f_label.place(x=5,y=0,width=700,height=130)
        
        left_inside_frame=Frame(left_frame,bd=2,bg="brown",relief=RIDGE)
        left_inside_frame.place(x=5,y=135,width=700,height=370)
        
        #Labels and entries
        #attendanceID
        attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("time new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Roll
        roll_label=Label(left_inside_frame,text="Roll No :",font=("time new roman",12,"bold"),bg="brown",fg="black")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)
        
        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("time new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,pady=8,sticky=W)
        
        #name
        name_label=Label(left_inside_frame,text="Name:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        name_label.grid(row=1,column=0)
        
        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("time new roman",12,"bold"))
        name_entry.grid(row=1,column=1,pady=8,sticky=W)
        
        #Department
        department_label=Label(left_inside_frame,text="Department:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        department_label.grid(row=1,column=2)
        
        department_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("time new roman",12,"bold"))
        department_entry.grid(row=1,column=3,pady=8,sticky=W)
        
        #time
        time_label=Label(left_inside_frame,text="Time:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        time_label.grid(row=2,column=0)
        
        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("time new roman",12,"bold"))
        time_entry.grid(row=2,column=1,pady=8,sticky=W)
        
        #Date
        date_label=Label(left_inside_frame,text="Date:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        date_label.grid(row=2,column=2)
        
        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("time new roman",12,"bold"))
        date_entry.grid(row=2,column=3,pady=8,sticky=W)
        
        #Attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        attendance_label.grid(row=3,column=0)
        
        self.atten_status= ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendance,font=("time new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        
        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=665,height=50)
        
        save_button=Button(btn_frame,text="Import CSV",command=self.importCsv,width=13,font=("time new roman",12,"bold"))
        save_button.grid(row=0,column=0)
        
        update_button=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=13,font=("time new roman",12,"bold"))
        update_button.grid(row=0,column=1)
        
        del_button=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("time new roman",12,"bold"))
        del_button.grid(row=0,column=2)
        
        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("time new roman",12,"bold"))
        reset_button.grid(row=0,column=3)
        
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="brown",relief=RIDGE,text="Attendance details",font=("time new roman",12,"bold"))
        right_frame.place(x=720,y=10,width=680,height=700)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=500)
        
        #scrollbar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll no")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    #Fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
     
     
    # import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Data exported successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        
    def update_data(self):
    # Get the currently selected row
        selected = self.AttendanceReportTable.focus()
    
    # If no row is selected, show an error
        if not selected:
            messagebox.showerror("Error", "No record selected", parent=self.root)
            return
    
    # Update the selected row with the new values from the entry fields
        self.AttendanceReportTable.item(selected, values=(
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
    ))
    
    # Optionally, show a confirmation message
        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

        
    
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()