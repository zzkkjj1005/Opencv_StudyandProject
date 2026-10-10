import cv2
import numpy as np
#引入图像
img=cv2.imread("./picture_video/15.png")
#转化为灰度图
new=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,binary=cv2.threshold(new,100,255,cv2.THRESH_BINARY)
#获取轮廓
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#绘制轮廓
# cv2.drawContours(img,contours,-1,(0,0,255),2)

# #计算面积
# area=cv2.contourArea(contours[0])
# print("area=%d"%(area))

# #计算周长
# len=cv2.arcLength(contours[0],True)
# print("len=%d"%(len))


# def drawShape(src,points):
#     i=0
#     while i<len(points):
#         if(i==len(points)-1):
#             x,y=points[i][0]
#             x1,y1=points[0][0]
#             cv2.line(src,(x,y),(x1,y1),(0,0,255),2)
#         else:
#             x,y=points[i][0]
#             x1,y1=points[i+1][0]
#             cv2.line(src,(x,y),(x1,y1),(0,0,255),2)
#         i=i+1
#多边形逼近
# e=30
# approx=cv2.approxPolyDP(contours[0],e,True)
# drawShape(img,approx)

#凸包
# full=cv2.convexHull(contours[0])
# drawShape(img,full)

#最小外接矩形
r=cv2.minAreaRect(contours[1]) #r((中心点x,中心点y),(宽,高),角度)
box=cv2.boxPoints(r)  #转变为坐标
box=np.intp(box)  #转变为整形
cv2.drawContours(img,[box],0,(0,0,255),2)

#最大外接矩形
x,y,w,h=cv2.boundingRect(contours[1])
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# print(contours[0])
cv2.imshow('binary',binary)
cv2.imshow('img',img)
cv2.waitKey(0)