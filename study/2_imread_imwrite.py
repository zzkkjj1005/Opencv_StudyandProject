import cv2

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
img=cv2.imread("./picture_video/3.jpg",1)
cv2.imshow('img',img)

key=cv2.waitKey(0)
if key==ord('q'):
    print("1111")
elif key==ord('s'):
    cv2.imwrite("D:\\learnopencv\\picture\\1.png",img=img)
exit()
