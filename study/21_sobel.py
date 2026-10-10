import cv2
import numpy as np

img=cv2.imread("./picture_video/8.png")

#高通滤波
#索贝尔Sobel算子 要分别对x和y求导再相加 ksize设置为-1时转变为Scharr
# new1=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# new2=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# new=cv2.add(new1,new2)

#沙尔Scharr算子  卷积ksize固定为3X3 
# new1=cv2.Scharr(img,cv2.CV_64F,1,0)
# new2=cv2.Scharr(img,cv2.CV_64F,0,1)
# new=cv2.add(new1,new2)

#拉普拉斯Laplacian算子 可以同时对x和y求导 但是对噪声敏感
new=cv2.Laplacian(img,cv2.CV_64F,ksize=5)

cv2.imshow('img',img)
# cv2.imshow('new1',new1)
# cv2.imshow('new2',new2)
cv2.imshow('new',new)
cv2.waitKey(0)