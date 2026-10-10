import cv2
import numpy as np

img=cv2.imread("./picture_video/3.jpg")
img=cv2.resize(img,None,fx=0.3,fy=0.3)

#反转 (反转不等同于旋转)
#filp 0代表上下翻转 >0代表左右翻转 <0上下左右都反转
# new=cv2.flip(img,1)
# cv2.imshow('new',new)
# cv2.waitKey(0)

#旋转 
new=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('new',new)
cv2.waitKey(0)