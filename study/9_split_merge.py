import cv2
import numpy as np

img=np.zeros((460,680,3),np.uint8)
#通道的分割
b,g,r=cv2.split(img)
r[100:200,100:200]=255
g[100:200,100:200]=0
#通道的合并
img2=cv2.merge([b,g,r])

cv2.imshow('img',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('img2',img2)

cv2.waitKey(0)