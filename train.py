import os
import face_recognition
print('train')
ids = os.listdir('images')
classes = []

for i in ids:
    encodings = []
    for j in os.listdir('images/'+i):
        img = face_recognition.load_image_file("images/"+i+"/"+str(j))
        img_encoding = face_recognition.face_encodings(img)[0]
        
        encodings.append(img_encoding)
    classes.append(encodings)
