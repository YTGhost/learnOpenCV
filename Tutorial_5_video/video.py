# 从文件中播放视频
import cv2 as cv

cap = cv.VideoCapture('C:\VS-Python\learnOpenCV\Tutorial_5_video\line.avi')     #将设备索引号改成视频文件的地址就可以读取视频了
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(25) & 0XFF == ord('q'):       #每一帧持续25毫秒
        break
cap.release()
cv.destroyAllWindows()
