import cv2
import numpy as np

img=cv2.imread("Resources/Lenna.png") #import an image
kernel=np.ones((2,2),np.uint8)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(img,(9,9),0)
imgcanny=cv2.Canny(img,100,100)
imgdia=cv2.dilate(imgcanny,kernel,iterations=1)


cv2.imshow("output",img)  #show the image
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgblur)
cv2.imshow("Canny",imgcanny)
cv2.imshow("Cannydia",imgdia)

cv2.waitKey(0)

