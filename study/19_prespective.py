import cv2
import numpy as np

img0=cv2.imread("./picture_video/3.jpg")
img=cv2.resize(img0,None,fx=0.3,fy=0.2)
print(img.shape)

#透视变换
#四点确定 左上 右上 左下 右下
src=np.float32([[100,100],[700,100],[100,900],[900,900]])
dst=np.float32([[0,0],[819,0],[0,922],[819,922]])
M=cv2.getPerspectiveTransform(src,dst)

new=cv2.warpPerspective(img,M,(819,922))
cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)