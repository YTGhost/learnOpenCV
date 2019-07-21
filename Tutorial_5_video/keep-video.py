# 从摄像头中捕获视频，把每一帧倒过来并保存它。

import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')    #表示使用XVID编码器
# fourcc = cv2.cv.FOURCC(*'XVID') 该用法是OpenCV2的用法
out = cv2.VideoWriter('C:\VS-Python\learnOpenCV\Tutorial_5_video\output.avi',fourcc,20.0,(640,480))
#cv2.VideoWriter()括号中四个参数分别表示：输出视频地址与名称，编码器，帧率，帧宽和高。

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)   #第二个参数可修改：1为水平翻转，0为垂直翻转，-1为水平垂直翻转

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) &0XFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
