from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
import datetime
import mysql.connector
def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1590x1309+0+0")
        
        self.bg=ImageTk.PhotoImage(file="/Users/priyanshiranawat/AttendanceSystemManagement/Photo/beach.jpeg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/lock.login.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_start=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_start.place(x=113,y=100)
        
        #LABELS
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)
        
        #icon images
        img2=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/lock.login.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg2= ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/lock.login.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)
        
        # login button
        loginbutton=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="brown",activeforeground="red",activebackground="black")
        loginbutton.place(x=110,y=300,width=120,height=35)
        
        # register button
        regisbutton=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="brown",activeforeground="red",activebackground="black")
        regisbutton.place(x=20,y=350,width=160)
        
        # forget pass button
        forgetbutton=Button(frame,text="Forgot Password?",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="brown",activeforeground="red",activebackground="black")
        forgetbutton.place(x=20,y=370,width=160)
        
     
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
            
        elif self.txtuser.get()=="pri" and self.txtpass.get()=="P123":
            messagebox.showinfo("Success","Welcome to the portal")
        
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mysql@15", database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only to admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            
            conn.close()
            
    #reset passwor4d func
    
    def reset_pass(self):
        if self.combo_security=="select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.secure_entry.get()=="":
            message.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.new_pass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mysql@15", database="sys")
            my_cursor=conn.cursor()
            qry=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value= (self.txtuser.get(),self.combo_security.get(),self.secure_entry.get(),)
            my_cursor.execute(qry,value)
            row= my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_pass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                messagebox.showinfo("Success","password has been successfully changed!!!",parent=self.root2)
                self.root2.destroy()
            
    # forgot password window

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mysql@15", database="sys")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("My error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel(self.root)
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")
                
                l = Label(self.root2,text="Forgot password",font=("times new roman",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                securityQ_lbl=Label(self.root2,text="Select security questions",font=("times new roman",15,"bold"),bg="black")
                securityQ_lbl.place(x=50,y=80)
        
                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security['values']=("Select","Your Birth Place","Your favourite food","Your pet's name")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)
        
                securityA_lbl=Label(self.root2,text="Security Answer.",font=("times new roman",15,"bold"),bg="black")
                securityA_lbl.place(x=50,y=150)
        
        
                self.secure_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.secure_entry.place(x=50,y=180,width=250)
                
                new_password_lbl=Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="black")
                new_password_lbl.place(x=50,y=220)
        
                self.new_pass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.new_pass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="green",fg="green")
                btn.place(x=100,y=290)
                
                           
            

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
        b1=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2")
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
        
    def return_login(self):
        self.root.destroy()

if __name__=="__main__":
    main()
    
    
    