import cv2
import numpy as np
import sqlite3
import os
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
conn = sqlite3.connect('face_database.db')
print("Opened database successfully")

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
    
Id=input('enter your id :')
branch=input('enter branch :')
name=input('enter name :')

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
        #saving the captured face in the dataset folder
        if not os.path.isdir('images/'+Id):
            os.makedirs('images/'+Id)
        cv2.imwrite("images/"+Id +'/'+name+"_"+ str(sampleNum) + ".jpg", img[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    #wait for 100 miliseconds 
        cv2.waitKey(100) 
    cv2.imshow('face',img)
    cv2.waitKey(1)
    
    # break if the sample number is morethan 20
    if sampleNum>5:
        break
cam.release()
cv2.destroyAllWindows()
