import cv2
import numpy as np

#定义回调函数
def callback(event,x,y,flag,userdata):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event,x,y,flag,userdata)
#定义窗口
cv2.namedWindow('mouse',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse',640,360)
#设置鼠标回调
cv2.setMouseCallback('mouse',callback,'123')
#设置展示背景颜色(全黑)
img=np.zeros((360,680,3),np.uint8)
while True:
    cv2.imshow('mouse',img)
    key=cv2.waitKey(1)
    if key & 0xff ==ord('q'):
        break

cv2.destroyAllWindows()
