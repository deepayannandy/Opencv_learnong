import cv2
import numpy as np

faceCascad= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
    flag, img=cap.read()
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascad.detectMultiScale(imggray,1.8,9)

    for (x,y,w,h) in faces:
        print(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

    cv2.imshow("Frame",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break