import cv2
#设置视频类型和地址
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
vw=cv2.VideoWriter("./picture_video/video1.avi",fourcc,25,(640,480))

#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

#读取设备/读取视频 设置为0时默认调用电脑摄像头
cap=cv2.VideoCapture("D:\\learnopencv\\picture_video\\video1.mp4") 

while cap.isOpened():
    #ret为检验是否成功,frame为视频帧
    ret,frame=cap.read()
    if ret==True:
        cv2.imshow('video',frame)
        # vw.write(frame)
        key=cv2.waitKey(20)
        if key & 0xFF==ord('q'):
            break
    else:
        break

# vw.release()
cap.release()
cv2.destroyAllWindows()