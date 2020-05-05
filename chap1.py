import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    flag,img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgcanny = cv2.Canny(img, 100, 100)
    imgcom=imgcanny-imgGray

    cv2.imshow("output",imgcom)
    cv2.imshow("Gray", imgGray)
    cv2.imshow("Canny", imgcanny)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break