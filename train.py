from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1590x1309+0+0")
        self.root.title("Training data set")
        
        title_label=Label(self.root,text="TRAIN DATASET", font=("times new roman",35,"bold"),bg="black",fg="white")
        title_label.place(x=0,y=0,width=1590,height=45)
        
        imgtop=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/face.jpeg")
        imgtop=imgtop.resize((1590,325),Image.Resampling.LANCZOS)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)
        
        f_label=Label(self.root,image=self.photoimgtop)
        f_label.place(x=0,y=55,width=1590,height=325)
        
        #Button
        b1_1 = Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="black",fg="brown")
        b1_1.place(x=0,y=380,width=1590,height=60)
        
        imgbottom=Image.open("/Users/priyanshiranawat/AttendanceSystemManagement/Photo/s2.jpeg")
        imgbottom=imgbottom.resize((1590,325),Image.Resampling.LANCZOS)
        self.photoimgbottom=ImageTk.PhotoImage(imgbottom)
        
        f_label=Label(self.root,image=self.photoimgbottom)
        f_label.place(x=0,y=440,width=1590,height=325)
        
        
    def train_classifier(self):
        data_dir=("Data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        """for image in path:
            img = Image.open(image).convert('L')   #converting into grayscale
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)
        ids=np.array(ids)"""
        for image in path:
        # Check if the file is an image
            if not image.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue  # Skip non-image files
        
            try:
                img = Image.open(image).convert('L')  # Converting into grayscale
                imageNp = np.array(img, 'uint8')
            
            # Ensure the filename is in the expected format
                filename = os.path.split(image)[1]
                id = int(filename.split('.')[1])  # Make sure this matches your file naming convention
            
                faces.append(imageNp)
                ids.append(id)
            
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)  # Just wait briefly to show the image
            except Exception as e:
                print(f"Error processing file {image}: {e}")

        ids = np.array(ids)


        
        # Train classifier
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
            
        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()