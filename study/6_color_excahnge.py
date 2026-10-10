import cv2

def callback(x):
    print(x)

cv2.namedWindow('color',cv2.WINDOW_NORMAL)
cv2.resizeWindow('color',680,480)

img=cv2.imread("./picture_video/3.jpg")

colorspace=[cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2BGRA,
            cv2.COLOR_BGR2GRAY,cv2.COLOR_BGR2HSV_FULL,cv2.COLOR_BGR2YUV]

cv2.createTrackbar('colorx','color',0,len(colorspace)-1,callback)

while True:
    index=cv2.getTrackbarPos('colorx','color')

    cvt_img=cv2.cvtColor(img,colorspace[index])
    
    cv2.imshow('color',cvt_img)
    key=cv2.waitKey(1)
    if key& 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
