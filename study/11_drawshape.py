import cv2
import numpy as np

curshape=0
startpos=[0,0]
cv2.namedWindow('drawshape',cv2.WINDOW_NORMAL)
cv2.resizeWindow('drawshape',680,480)
img=np.zeros((460,680,3),np.uint8)

def callback(event,x,y,flag,usedata):
    global startpos, curshape  #全局变量在函数内有修改时必须要加global
    if event& cv2.EVENT_LBUTTONDOWN==cv2.EVENT_LBUTTONDOWN:
        print(event,x,y,flag,usedata)
        startpos=(x,y)
    elif event& cv2.EVENT_LBUTTONUP==cv2.EVENT_LBUTTONUP:
        if curshape==1:
            cv2.line(img,startpos,(x,y),(255,255,0))
        if curshape==2:
            cv2.rectangle(img,startpos,(x,y),(0,255,0))
        if curshape==3:
            a=x-startpos[0]
            b=y-startpos[1]
            c=int((x+startpos[0])/2)
            d=int((y+startpos[1])/2)
            r=int(((a**2+b**2)**0.5)/2)
            cv2.circle(img,(c,d),r,(255,0,0),2)
        else:
            print("error:No shape")

cv2.setMouseCallback('drawshape',callback,'123')


while True:
    cv2.imshow('drawshape',img)
    key=cv2.waitKey(0)&0xFF
    if key==ord('q'):
        break
    elif key==ord('l'):
        curshape=1
    elif key==ord('r'):
        curshape=2
    elif key==ord('c'):
        curshape=3

cv2.destroyAllWindows()