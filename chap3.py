import cv2
import numpy as np

img=cv2.imread("Resources/Lenna.png")
print(img.shape)
imgresize=cv2.resize(img,(320,320))
imgcrop=img[0:200,0:200]

cv2.imshow("output",img)
cv2.imshow("resize",imgresize)
cv2.imshow("croped",imgcrop)
cv2.waitKey(0)