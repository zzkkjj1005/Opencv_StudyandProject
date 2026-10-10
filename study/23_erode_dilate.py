import cv2
import numpy as np

img=cv2.imread("./picture_video/11.png")
# img=cv2.resize(img,None,fx=0.6,fy=0.6)
# kernel=np.ones((3,3),np.uint8)
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(17,17))

#kernel为卷积 iteration为腐蚀次数 
#腐蚀
# new=cv2.erode(img,kernel,iterations=3)

#膨胀
# new=cv2.dilate(img,kernel,iterations=3)

# 开运算
# new=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

#闭运算
# new=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

#梯度
# new=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

#顶帽 原图-开运算
# new=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

#黑帽 闭运算-原图
new=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)
