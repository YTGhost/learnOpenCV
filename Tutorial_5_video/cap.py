import cv2 as cv
#获取当前摄像头的一帧图像并转换为灰度模式imshow出来
cap = cv.VideoCapture(0)  
#可以用cap.get(propId)来获取视频的一些参数信息，这里的propId可以是0到18之间的任何整数
print(cap.get(3),cap.get(4))    #可查看当前帧的宽和高，默认是640X480
ret = cap.set(3,320)        #可以通过这两个操作
ret = cap.set(3,240)        #把宽和高改成320X240
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()     #cap.read()返回一个布尔值，如果帧读取的是正确的，就是True

    # Our operations on the frame come here
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):        #间隔1毫秒不断刷新
        break
    
    # When everything done, release the capture
cap.release()
cv.destroyAllWindows()