import cv2
import numpy as np

cap=cv2.VideoCapture("./picture_video/video2.mov")
bgsubmog=cv2.createBackgroundSubtractorMOG2()

min_w=50
min_h=50

line_height=600
offest=6
carno=0

def center(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return cx,cy

while True:
    ret,frame=cap.read()    
    if(ret==True):
        #灰度
        new=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #去噪
        blur=cv2.GaussianBlur(new,(7,7),5)
        #去背景
        mask=bgsubmog.apply(blur)
        #开运算 去除细小的背景噪点
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        #闭运算 填补车辆内部的黑色空洞
        kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close)
        #膨胀 让车辆轮廓更完整
        kernel_dilate = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel_dilate, iterations=1)

        contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #基准线
        cv2.line(frame,(10,line_height),(1270,line_height),(255,255,0),3)
        
        cars=[]
        
        for(i,c)in enumerate(contours):
            (x,y,w,h)=cv2.boundingRect(c)
            #限制宽高
            if(w>min_w and h>min_h):
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(frame, f"{w}x{h}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                #此处数量识别有待完善
                # cpoint=center(x,y,w,h)
                # cars.append(cpoint)
                # for(x,y)in cars:
                #     if((y>line_height-offest) and (y<line_height+offest)):
                #         carno=carno+1
                #         print(carno)

        cv2.imshow("video",frame)
        key=cv2.waitKey(20)
        if(key==27):
            break

cap.release()
cv2.destroyAllWindows()
