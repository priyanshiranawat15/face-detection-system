from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1590x1309+0+0")
        
        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #background image
        self.bg = Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/Register.jpeg")
        self.bg = self.bg.resize((1590, 1309), Image.Resampling.LANCZOS)
        self.bg=ImageTk.PhotoImage(self.bg)
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #left image
        left_img=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s4.jpeg")
        left_img=left_img.resize((470,550),Image.Resampling.LANCZOS)
        self.photoleftimg= ImageTk.PhotoImage(left_img)
        lblimg1=Label(image=self.photoleftimg,bg="black",borderwidth=0)
        lblimg1.place(x=50,y=100,width=470,height=550)
        
        
        #frame
        frame = Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        #label
        register_lbl=Label(frame,text="Register here ",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        # label and entries
        fname_lbl=Label(frame,text="First name",font=("times new roman",15,"bold"),bg="black")
        fname_lbl.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        lname_lbl=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="black")
        lname_lbl.place(x=370,y=100)
        
        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)
        
        #----------row2
        contact_lbl=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="black")
        contact_lbl.place(x=50,y=170)
        
        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)
        
        email_lbl=Label(frame,text="Email ID.",font=("times new roman",15,"bold"),bg="black")
        email_lbl.place(x=370,y=170)
        
        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=370,y=200,width=250)
        
        #---------row3
        
        securityQ_lbl=Label(frame,text="Select security questions",font=("times new roman",15,"bold"),bg="black")
        securityQ_lbl.place(x=50,y=240)
        
        self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security['values']=("Select","Your Birth Place","Your favourite food","Your pet's name")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)
        
        securityA_lbl=Label(frame,text="Security Answer.",font=("times new roman",15,"bold"),bg="black")
        securityA_lbl.place(x=370,y=240)
        
        
        self.secure_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.secure_entry.place(x=370,y=270,width=250)
        
        
        #------row4
        
        pswd_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black")
        pswd_lbl.place(x=50,y=310)
        
        self.pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.pswd_entry.place(x=50,y=340,width=250)
        
        confirmpswd_lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black")
        confirmpswd_lbl.place(x=370,y=310)
        
        self.confirmpswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.confirmpswd_entry.place(x=370,y=340,width=250)
        
        #checkbutton
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree The Terms and Conditions ",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        #buttons
        img = Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/Register1.png")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)
        
        
        img1 = Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/login1.jpeg")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)
        
    #func
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm password should be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mysql@15", database="sys")

            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("error","User already exists, try another email")
            else:
                my_cursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(), 
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(), 
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(), 
                                                                                         self.var_pass.get()
                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")
        
        
        

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()