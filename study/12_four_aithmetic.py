import cv2
import numpy as np


reward=cv2.imread("./picture_video/5.jpg")
#参数要一致
print(reward.shape) #获取长度 高度 通道数
img=np.ones((4096,3072,3),np.uint8)*100

cv2.imshow('reward',reward)
#加减乘除
result1=cv2.add(reward,img) 
result2=cv2.subtract(reward,img)
result3=cv2.multiply(reward,img)
result4=cv2.divide(reward,img)

cv2.imshow('result1',result1) 
cv2.waitKey(0)
