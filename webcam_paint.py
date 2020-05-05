import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

mycolor=[]

def findcolor():
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mak = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("mak", mak)

while True:
    flag,img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    cv2.imshow("output",img)



    if cv2.waitKey(1)&0xFF==ord('q'):
        break