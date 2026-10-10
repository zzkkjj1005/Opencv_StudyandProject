import cv2
import numpy as np

img=np.zeros((480,680,3),np.uint8)

#线 (img,起使点,终止点,颜色,宽细,平滑程度)
cv2.line(img,(0,0),(255,255),(0,0,255),2,16)

#矩形 (img,左上点,右下点,颜色,实/空心)
cv2.rectangle(img,(139,4),(100,100),(0,255,0),-1)

#圆形 (img,中心点,半径,颜色,实/空心)
cv2.circle(img,(400,400),30,(255,0,0),-1)

#椭圆 (img,中心点,长宽的一半,椭圆旋转角度,从哪个角度开始绘制,从哪个角度结束,颜色,实/空心)
cv2.ellipse(img,(200,200),(50,25),0,180,360,(0,200,200),-1)

#多边形 pts为点集 Truro/False是否相连 fillPoly填充内部颜色并且会覆盖线的颜色
pts=np.array([(260,260),(350,350),(170,350)],np.int32) #int32表示只能4个字节
cv2.polylines(img,[pts],True,(0,0,255))
cv2.fillPoly(img,[pts],(255,255,0))
#输出字体 (img,"字符串",起使位置,字体样式,字号大小,颜色)
cv2.putText(img,"Helle World",(300,300),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255))

cv2.imshow('draw',img)
cv2.waitKey(0)