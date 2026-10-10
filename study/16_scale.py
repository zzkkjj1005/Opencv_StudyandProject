import cv2
import numpy as np

img=cv2.imread("./picture_video/3.jpg")
#resize(img,new,(200,200),fx,fy,interpolation)
new=cv2.resize(img,None,fx=1.4,fy=1.4,interpolation=cv2.INTER_AREA)

cv2.imshow('new',new)
cv2.waitKey(0)