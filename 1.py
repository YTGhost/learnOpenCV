import cv2 as cv
import numpy as np

image = cv.imread("C:\VS-Python\learnOpenCV\line.png")#读入图片

cv.namedWindow("original",1)#新建可调节窗口
cv.resizeWindow("original",500,400)#调整窗口大小

cv.imshow("original",image)#显示处理前的图片

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)#将图片转换成灰度图
edgs = cv.Canny(gray,10,80)#Canny边缘检测

minLength = 100
maxGap = 80     #设置概率霍夫函数关键参数

lines = cv.HoughLinesP(edgs,1,np.pi/180,minLength,maxGap)#调用概率霍夫直线检测

for line in lines:
    for x1,y1,x2,y2 in line:
        cv.line(gray,(x1,y1),(x2,y2),(0,0,255),2)#根据每一条直线的信息在原图上画出直线

cv.namedWindow("final",1)
cv.resizeWindow("final",500,400)
cv.imshow("final",gray)#显示处理后的图片
cv.waitKey()