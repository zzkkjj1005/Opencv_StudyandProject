import cv2
import numpy as np

img0=cv2.imread("./picture_video/3.jpg")
img=cv2.resize(img0,None,fx=0.3,fy=0.3)

h,w,ch=img.shape
print(img.shape)
#向下 向右为正
# M=np.float32([[1,0,200],[0,1,100]])

#旋转点 逆时针旋转 缩放比例 
# M=cv2.getRotationMatrix2D((w/2,h/2),15,1)

#三点不共线！！！
src=np.float32([[25,30],[31,47],[46,70]])
dst=np.float32([[37,34],[49,44],[51,51]])
M=cv2.getAffineTransform(src,dst)
new=cv2.warpAffine(img,M,(w,h))

cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)