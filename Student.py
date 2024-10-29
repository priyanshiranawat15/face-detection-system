from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x1309+0+0")
        self.root.title("Student management system")
        
        
        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        #first image
        img=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s1.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s2.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s3.jpeg")
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
        
        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="black",fg="white")
        title_label.place(x=0,y=0,width=1590,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="brown")
        main_frame.place(x=10,y=55,width=1590,height=1100)
        
        #Left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="brown",relief=RIDGE,text="Student details",font=("time new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=700,height=700)
        
        imgleft=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s4.jpeg")
        imgleft=imgleft.resize((700,130),Image.Resampling.LANCZOS)
        self.photoimgleft=ImageTk.PhotoImage(imgleft)
        
        f_label=Label(left_frame,image=self.photoimgleft)
        f_label.place(x=5,y=0,width=700,height=130)
        
        #current course
        currentcourse_frame=LabelFrame(left_frame,bd=2,bg="brown",relief=RIDGE,text="Current Course Information",font=("time new roman",12,"bold"))
        currentcourse_frame.place(x=5,y=135,width=680,height=150)
        
        
        # department
        dep_label=Label(currentcourse_frame,text="Department:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer Science","Information Technology","CSE[AIML]")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        #course
        course_label=Label(currentcourse_frame,text="Course:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        course_label.grid(row=0,column=2,padx=10)
        
        course_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_course,font=("time new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","ME","PHD","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year
        year_label=Label(currentcourse_frame,text="Year:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_year,font=("time new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        semester_label=Label(currentcourse_frame,text="Semester:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(currentcourse_frame,textvariable=self.var_semester,font=("time new roman",12,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student information
        classstudent_frame=LabelFrame(left_frame,bd=2,bg="brown",relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"))
        classstudent_frame.place(x=5,y=260,width=680,height=420)
        
        #studentID
        studentId_label=Label(classstudent_frame,text="StudentID:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentId_entry=ttk.Entry(classstudent_frame,textvariable=self.var_std_id,width=20,font=("time new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #studentname
        studentname_label=Label(classstudent_frame,text="Student Name:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(classstudent_frame,textvariable=self.var_std_name,width=20,font=("time new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division
        classdivi_label=Label(classstudent_frame,text="Class Division:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        classdivi_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #classdivi_entry=ttk.Entry(classstudent_frame,textvariable=self.var_div,width=20,font=("time new roman",12,"bold"))
        #classdivi_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        classdivi_combo=ttk.Combobox(classstudent_frame,textvariable=self.var_div,font=("time new roman",12,"bold"),width=17,state="read only")
        classdivi_combo["values"]=("Select Division","D-1","D-2","D-3","D-4","A","B","C")
        classdivi_combo.current(0)
        classdivi_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #roll no
        rollno_label=Label(classstudent_frame,text="Roll No:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(classstudent_frame,textvariable=self.var_roll,width=20,font=("time new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(classstudent_frame,text="Gender:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(classstudent_frame,textvariable=self.var_gender,width=20,font=("time new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        gender_combo=ttk.Combobox(classstudent_frame,textvariable=self.var_gender,font=("time new roman",12,"bold"),width=17,state="read only")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #DOB
        dob_label=Label(classstudent_frame,text="Date Of Birth:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(classstudent_frame,textvariable=self.var_dob,width=20,font=("time new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        email_label=Label(classstudent_frame,text="Email:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(classstudent_frame,textvariable=self.var_email,width=20,font=("time new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Phoneno
        phno_label=Label(classstudent_frame,text="Contact No:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        phno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phno_entry=ttk.Entry(classstudent_frame,textvariable=self.var_phone,width=20,font=("time new roman",12,"bold"))
        phno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        address_label=Label(classstudent_frame,text="Address:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(classstudent_frame,textvariable=self.var_address,width=20,font=("time new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher name
        teacher_label=Label(classstudent_frame,text="Teacher Name:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(classstudent_frame,textvariable=self.var_teacher,width=20,font=("time new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(classstudent_frame,text="Take photo sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2=ttk.Radiobutton(classstudent_frame,text="No photo sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=6,column=1)
        
        #button frame
        btn_frame=Frame(classstudent_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=220,width=665,height=50)
        
        save_button=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("time new roman",12,"bold"))
        save_button.grid(row=0,column=0)
        
        update_button=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("time new roman",12,"bold"))
        update_button.grid(row=0,column=1)
        
        del_button=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font=("time new roman",12,"bold"))
        del_button.grid(row=0,column=2)
        
        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("time new roman",12,"bold"))
        reset_button.grid(row=0,column=3)
        
        btn_frame1=Frame(classstudent_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=280,width=665,height=50)
        
        
        Takephoto_button=Button(btn_frame1,command=self.generate_dataset,text="Take photo",width=28,font=("time new roman",12,"bold"))
        Takephoto_button.grid(row=1,column=0)
        
        updatephoto_button=Button(btn_frame1,text="Update photo",width=28,font=("time new roman",12,"bold"))
        updatephoto_button.grid(row=1,column=1)
        
        
        
        
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="brown",relief=RIDGE,text="Student details",font=("time new roman",12,"bold"))
        right_frame.place(x=720,y=10,width=680,height=700)
        
        imgright=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s5.jpeg")
        imgright=imgright.resize((680,130),Image.Resampling.LANCZOS)
        self.photoimgright=ImageTk.PhotoImage(imgright)
        
        f_label=Label(right_frame,image=self.photoimgright)
        f_label.place(x=5,y=0,width=680,height=130)
        
        #SearchSystem
        
        Search_frame=LabelFrame(right_frame,bd=2,bg="brown",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=660,height=80)
        
        search_label=Label(Search_frame,text="Search By:",font=("time new roman",12,"bold"),bg="brown",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("time new roman",12,"bold"),width=10,state="read only")
        search_combo["values"]=("Select ","Roll no","Ph.no","Student id","Class division","Name","Gender","DOB","Email","Contact No","Address","Teacher Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=10,font=("time new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_button=Button(Search_frame,text="Search",width=10,font=("time new roman",12,"bold"))
        search_button.grid(row=0,column=3)
        
        showAll_button=Button(Search_frame,text="Show All",width=10,font=("time new roman",12,"bold"))
        showAll_button.grid(row=0,column=4)

        #table frame
        table_frame=Frame(right_frame,bd=2,bg="brown",relief=RIDGE)
        table_frame.place(x=5,y=220,width=660,height=450)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","sem","id","year","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)   
        scroll_x.config(command=self.student_table.xview)  
        scroll_y.config(command=self.student_table.yview)  
        
        self.student_table.heading("dep",text="Department")   
        self.student_table.heading("course",text="Course")   
        self.student_table.heading("sem",text="Semester")   
        self.student_table.heading("id",text="Student ID")   
        self.student_table.heading("year",text="Year")   
        self.student_table.heading("name",text="Student Name")   
        self.student_table.heading("div",text="Division")   
        self.student_table.heading("roll",text="Roll No")   
        self.student_table.heading("gender",text="Gender")   
        self.student_table.heading("dob",text="DOB")   
        self.student_table.heading("email",text="Email")   
        self.student_table.heading("phone",text="Phone")   
        self.student_table.heading("address",text="Address")   
        self.student_table.heading("teacher",text="Teacher Name")   
        self.student_table.heading("photo",text="Photo")  
        
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1) 
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #Function declaration
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@15",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))
                conn.commit()
                
                
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            finally:
                my_cursor.close()            
                conn.close()
            
     # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@15",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    # get cursor func
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        

        
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@15",database="face_recogniser")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,Photo Sample =%s where StudentID=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))
        
                else:
                    if  not Update:
                        return
                messagebox.showinfo("successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            finally:
                my_cursor.close()            
                conn.close()
                
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@15",database="face_recogniser")
                    my_cursor=conn.cursor()
                    
                    sql="delete from student where StudentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                
                
                messagebox.showinfo("Delete","Successfully done",parent=self.root)
                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            finally:
                my_cursor.close()            
                conn.close()
                
    # reset func
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
        
        
    #generate dataset take photo samples
    def generate_dataset(self):
        try:
        
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
                
            else:
            
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@15",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult= my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,RollNo=%s,Gender=%s,DOB=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,`Photo Sample` =%s where StudentID=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()==id+1))
                    conn.commit()
                    
                self.fetch_data()
                #self.reset_data()
                
                
                    
                    
                    #loading predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    
                def face_cropped(img):
                    gray=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)  # scaling factor =1.3 , minimum neighbour =5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                        
                cap = cv2.VideoCapture(0)
                img_id=0
                    
                while True:
                    ret, my_frame=cap.read()
                    if ret and face_cropped(my_frame) is not None:
                        img_id+=1
                        face= cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user." + str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
        except Exception as es:

            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            conn.close()
        
                    
                    
                                
if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()