import cv2
import numpy as np

#两张图片的长度和宽度和通道数要一样才可以用addWeighted
img1=cv2.imread("./picture_video/3.jpg")
img2=cv2.imread("./picture_video/5.jpg")
height,weight=img2.shape[0:2]
img3=cv2.resize(img1,(weight,height))
print(img2.shape)
print(img3.shape)

#(img1,权重,img2,权重,静态权重)
result=cv2.addWeighted(img3,0.7,img2,0.3,0)
cv2.imshow('reslut',result)
cv2.waitKey(0)