import cv2
import numpy as np

img=cv2.imread("./picture_video/5.jpg")
img=cv2.resize(img,None,fx=0.3,fy=0.2)
#需要先转化为灰度图
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#ret为阈值(返回值)100,dst为新图像
ret,dst=cv2.threshold(img1,100,255,cv2.THRESH_BINARY)

#自适应卷积自动扫 但是噪声严重 
new=cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,0)
cv2.imshow('img',img1)
cv2.imshow('dst',dst)
cv2.imshow('new',new)
cv2.waitKey(0)
