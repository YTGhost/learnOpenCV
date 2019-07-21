import cv2
import numpy as np

lower_white = np.array([60, 10, 180])  # 设定白色的阈值
upper_white = np.array([80, 60, 255])


#cam=cv2.VideoCapture(0)#打开摄像头
cam = cv2.VideoCapture("C:\VS-Python\learnOpenCV\line.avi")#打开录制视频

while(1):
    ret,frame = cam.read()#获取每一帧
    
    cv2.namedWindow("original",1)
    cv2.resizeWindow("original",300,300)
    cv2.imshow("original",frame)#显示处理前的视频

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#获取HSV图片
    
    mask = cv2.inRange(hsv, lower_white, upper_white)#获取Mask掩模图

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ( 9, 9))
    mask2 = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)#对掩模图作闭运算（优化处理）
    
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)#调用Canny边缘检测

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 58, minLineLength=5, maxLineGap=10)#调用概率霍夫

    if np.all(lines != None):
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)#根据每一条直线的信息在原图上画出直线
                
    cv2.namedWindow("HSV",1)
    cv2.resizeWindow("HSV",400,300)
    cv2.imshow("HSV",hsv)#显示处理后的HSV图

    cv2.namedWindow("mask2",1)
    cv2.resizeWindow("mask2",400,300)
    cv2.imshow("mask2",mask2)#显示处理后的掩模图

    cv2.namedWindow("edges",1)
    cv2.resizeWindow("edges",400,300)
    cv2.imshow("edges",edges)#显示处理后的边缘检测图
    
    cv2.namedWindow("final",1)
    cv2.resizeWindow("final",400,300)
    cv2.imshow("final",frame)#显示处理后的视频
    

    k = cv2.waitKey(20) & 0xFF     #获取键盘输入值
    if k == 27:
        cv2.waitKey(0)             #如果是esc键则暂停

cam.release()#释放摄像头
cv2.destroyAllWindows()#关闭所有窗口
