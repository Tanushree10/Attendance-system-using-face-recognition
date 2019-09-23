import tkinter as tk
from tkinter import *
import os
import cv2
import sqlite3
def click():
    os.system('spreadsheet.py')
    os.system('recog.py')

def click1():
    
    
    window = tk.Tk()
    window.geometry("600x400")
    window.title("add student data")
    message = tk.Label(window, text='ADD STUDENT',width=30  ,height=2,font=('times', 30, ' bold underline')) 

    message.pack()

    lbl = tk.Label(window, text="Enter ID",width=20  ,height=2  ,font=('times', 15, ' bold ') ) 
    lbl.pack()
    lbl.place(x=5, y=80)

    txt = tk.Entry(window,width=20  ,font=('times', 15, ' bold '))
    txt.place(x=190, y=90)

    lbl2 = tk.Label(window, text="Enter Name",width=20     ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=5, y=120)

    txt2 = tk.Entry(window,width=20  ,font=('times', 15, ' bold ')  )
    txt2.place(x=190, y=130)

    lbl3 = tk.Label(window, text="Enter Branch",width=20     ,height=2 ,font=('times', 15, ' bold ')) 
    lbl3.place(x=5, y=160)

    txt3 = tk.Entry(window,width=20  ,font=('times', 15, ' bold ')  )
    txt3.place(x=190, y=170)
    def clear():
        txt.delete(0, 'end')    
        res = ""
        txt.configure(text= res)
    def clear2():
        txt.delete(0, 'end')    
        res = ""
        txt2.configure(text= res)
    def clear3():
        txt.delete(0, 'end')    
        res = ""
        txt3.configure(text= res)
    def data():
        Id= txt.get()
        name=txt2.get()
        branch=txt3.get()
        cam = cv2.VideoCapture(0)
        detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        conn = sqlite3.connect('face_database.db')
    #print("Opened database successfully")

        def InsertOrUpdate(Id,name,branch):
            a=[Id,name,branch]
            conn = sqlite3.connect('face_database.db')
            cmd='select * from attendance where ID='+str(Id)
            cursor=conn.execute(cmd)
            isRecordExist=0
            for row in cursor:
                isRecordExist=1
            if isRecordExist==1:
            
                conn.execute('update into attendance (ID,NAME,BRANCH) values (?,?,?)',(a[0],a[1],a[2]));
            else:
            
                conn.execute('insert into attendance (ID,NAME,BRANCH) values (?,?,?)',(a[0],a[1],a[2]));
            conn.commit()
            conn.close()
    


        InsertOrUpdate(Id,name,branch)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(img, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
            #incrementing sample number 
                sampleNum=sampleNum+1
                print(sampleNum)
            #saving the captured face in the dataset folder
                if not os.path.isdir('images/'+Id):
                    os.makedirs('images/'+Id)
                cv2.imwrite("images/"+Id +'/'+Id+"."+ str(sampleNum) + ".jpg", img[y:y+h,x:x+w])

                cv2.imshow('frame',img)
        #wait for 100 miliseconds 
                cv2.waitKey(100) 
            cv2.imshow('face',img)
            cv2.waitKey(1)
    
        # break if the sample number is morethan 20
            if sampleNum>4:
                break
        cam.release()
        cv2.destroyAllWindows()

    clearButton = tk.Button(window, text="Clear", command=clear   ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton.place(x=450, y=80)
    clearButton2 = tk.Button(window, text="Clear", command=clear2  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton2.place(x=450, y=120)
    clearButton3 = tk.Button(window, text="Clear", command=clear3  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    clearButton3.place(x=450, y=160)
    add_data = tk.Button(window, text="ADD DATA", command=data  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    add_data.place(x=100, y=240)
    exit1 = tk.Button(window, text="BACK", command=window.destroy  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    exit1.place(x=300, y=240)  
     



window = tk.Tk()
window.geometry("400x400")
window.title("Face_Recogniser Attendance")
#window.configure()
x=Label(window,text='IIIT PUNE',width=50  ,height=2,font=('times', 30, ' bold underline'))
x.pack()
b=Button(window,text='ATTENDANCE',width=20  ,height=2,command=click)
b.pack()
b.place(x=120, y=150)
b1=Button(window,text='ADD STUDENT',width=20  ,height=2,command=click1)
b1.pack()
b1.place(x=120, y=200)
b2=Button(window,text='EXIT',width=20  ,height=2,command=window.destroy)
b2.pack()
b2.place(x=120, y=250)
window.mainloop()
