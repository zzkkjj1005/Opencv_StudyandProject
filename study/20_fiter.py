import cv2
import numpy as np

img=cv2.imread("./picture_video/10.png")


#低通滤波 模糊/除噪音/平滑图像
# kernel=np.ones((5,5),np.float32)/25
# new=cv2.filter2D(img,-1,kernel)

#均值滤波 等级于 低通滤波
# new=cv2.blur(img,(5,5))

#方盒滤波 当normalize为True时为均值滤波
#new=cv2.boxFilter(img,-1,(5,5),None,None,True)

#高斯滤波  处理高斯噪音
new=cv2.GaussianBlur(img,(5,5),sigmaX=1,sigmaY=1)

#中值滤波 处理胡椒噪音
# new=cv2.medianBlur(img,5)

#双边滤波 美颜 保留边缘的同时对内部进行平滑处理 
# new=cv2.bilateralFilter(img,7,20,50)
cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)
cv2.destroyAllWindows()