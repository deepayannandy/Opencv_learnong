import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
print(img.shape,img)

#img[:]=255,122,160
cv2.line(img,(0,0),(256,256),(0,0,225),2)
cv2.rectangle(img,(200,200),(256,256),(225,0,0),2)
cv2.circle(img,(256,256),100,(0,255,0),1)
cv2.putText(img,"Deepayan Nandy",(200,400),cv2.FONT_HERSHEY_COMPLEX,1,(125,125,124),1)


cv2.imshow("output",img)

cv2.waitKey(0)