import cv2
import numpy as np

img1=np.zeros((200,200),np.uint8)
img2=np.zeros((200,200),np.uint8)

img1[20:150,20:150]=255
img2[80:200,80:200]=255
#与
new_img1=cv2.bitwise_and(img1,img2)
#非
new_img2=cv2.bitwise_not(img1)
#或
new_img3=cv2.bitwise_or(img1,img2)
#异或 相同为0 不同为1
new_img4=cv2.bitwise_xor(img1,img2)
cv2.imshow('img1',img1)
# cv2.imshow('new_img1',new_img1)
# cv2.imshow('new_img2',new_img2)
# cv2.imshow('new_img3',new_img3)
cv2.imshow('new_img4',new_img4)
cv2.waitKey(0)