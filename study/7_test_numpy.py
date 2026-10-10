import numpy as np
import cv2

# #普通数组
# a=np.array([[1,2,3],[4,5,6]])
# print(a)

# #全为0
# b=np.zeros((8,8,3),np.uint8)
# print(b)

# #全为1
# c=np.ones((8,8,3),np.uint8)
# print(c)

# #斜对角为1
# d=np.identity(8)
# print(d)

# #斜对角为1并且可以通过k来控制初始1
# e=np.eye(3,7,k=2)
# print(e)

# #自己设置全为255或其它
# f=np.full((8,8,3),255,np.uint8)
# print(f)

#检索与赋值
# img=np.zeros((460,680,3),np.uint8)
# print(img[100,100])
# count=0
# while count<200:
#     #BGR
#     img[count,100,2]=100  #img[count,100]=[255,255,255]
#     count=count+1

# cv2.imshow('img',img)
# key=cv2.waitKey(0)
# if key &0xFF==ord('q'):
#     cv2.destroyAllWindows()

#子矩阵赋值
img=np.zeros((460,680,3),np.uint8)
roi=img[100:200,100:200]
roi[:]=[255,0,0]

cv2.imshow('img',img)
key=cv2.waitKey(0)
if key &0xFF==ord('q'):
    cv2.destroyAllWindows()