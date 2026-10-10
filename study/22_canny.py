import cv2
import numpy as np

img=cv2.imread("./picture_video/8.png",0)
#Canny 王中王
#自己设置最小最大阈值 
new=cv2.Canny(img,100,200)

cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)