import cv2
import numpy as np

img=cv2.imread("Resources/cards.jpg")
width,height=250,350
points=np.float32([[111,219],[287,188],[154,482],[352,440]])
point2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(points,point2)
imgout=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("output",img)
cv2.imshow("worpout",imgout)

cv2.waitKey(0)