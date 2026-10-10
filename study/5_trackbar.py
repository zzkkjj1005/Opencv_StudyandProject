import cv2
import numpy as np

def callback(color):
    def on_changed(x):
        print(f"当前滑动{color}值为{x}")
    return on_changed

cv2.namedWindow('trackbar',cv2.WINDOW_NORMAL)

cv2.createTrackbar('R','trackbar',0,255,callback('R'))
cv2.createTrackbar('G','trackbar',0,255,callback('G'))
cv2.createTrackbar('B','trackbar',0,255,callback('B'))

img=np.zeros((640,480,3),np.uint8)

while True:
    r=cv2.getTrackbarPos('R','trackbar')
    g=cv2.getTrackbarPos('G','trackbar')
    b=cv2.getTrackbarPos('B','trackbar')
    img[:]=[r,g,b]

    cv2.imshow('trackbar',img)
    key=cv2.waitKey(1)
    if key &0xFF==ord('q'):
        break

cv2.destroyAllWindows()