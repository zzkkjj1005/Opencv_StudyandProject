import cv2
import numpy as np

img=cv2.imread("./picture_video/3.jpg")
#mat的深拷贝与浅拷贝
# img2=img
# img3=img.copy()
# img[100:200,100:200]=[0,0,255]
# cv2.imshow('img',img)
# cv2.imshow('img2',img2)
# cv2.imshow('img3',img3)
# cv2.waitKey(0)

#高度 长度 通道数
print(img.shape)
#占用空间
print(img.size)
#每个元素的位深
print(img.dtype)
