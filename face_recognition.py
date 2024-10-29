from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x1309+0+0")
        self.root.title("FACE RECOGNITION")
        
       
        title_label=Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="black",fg="white")
        title_label.place(x=0,y=0,width=1590,height=45)
         # first image
        imgtop=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/face.jpeg")
        imgtop=imgtop.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)
        
        f_label=Label(self.root,image=self.photoimgtop)
        f_label.place(x=0,y=55,width=650,height=700)
        
        #second image
        imgbottom=Image.open("Photo/face2.png")
        imgbottom=imgbottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimgbottom=ImageTk.PhotoImage(imgbottom)
        
        f_label=Label(self.root,image=self.photoimgbottom)
        f_label.place(x=650,y=55,width=950,height=700)
        
        #Button
        b1_1 = Button(f_label,text="Face Recognition",cursor="hand2",font=("times new roman",16,"bold"),bg="black",fg="brown",command=self.face_recog)
        b1_1.place(x=350,y=600,width=200,height=40)
        
    # attendance function
    def mark_attendance(self,i,r,n,d):
        with open("pri.csv","r+",newline="\n") as f:
            myDataList= f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
        
        
    # face recognition function
    
    def face_recog(self):
        def draw_boundry(img, classifier, scaleFactor,minNeighbours, color, text, clf):
            gray_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image, scaleFactor,minNeighbours)
            
            coord =[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])  # Correct

                confidence=int((100*(1-predict/300)))
                
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@15",database="face_recogniser")
                my_cursor=conn.cursor()
                    
                    
                my_cursor.execute("select Name from student where StudentID="+ str(id))
                n = my_cursor.fetchone()
                n = n[0] if n is not None else "Unknown"

                    
                my_cursor.execute("select RollNo from student where StudentID="+ str(id))
                r = my_cursor.fetchone()
                r = r[0] if r is not None else "Unknown"

                    
                my_cursor.execute("select Dep from student where StudentID="+ str(id))
                d = my_cursor.fetchone()
                d = d[0] if d is not None else "Unknown"

                
                my_cursor.execute("select StudentID from student where StudentID="+ str(id))
                i = my_cursor.fetchone()
                i = i[0] if i is not None else "Unknown"

                
                if confidence> 77:
                    cv2.putText(img,f"StudentID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Deparment:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord =[x,y,w,h]
                
            return coord
        
        def recognize(img, clf,faceCascade):
            coord= draw_boundry(img, faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img 
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
       
        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image")
                break  # or continue, depending on what you want to do in case of failure
    
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

            
        video_cap.release()
        cv2.destroyAllWindows()
            
                    
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()