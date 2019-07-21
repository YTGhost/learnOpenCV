# 画一个红色的圆
import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)
#创建一个图像，高为512，宽为512，三通道，数据类型为无符号8位

# Draw a diagonal blue line with thickness of 5 px
cv.circle(img,(447,63),63,(0,0,255),-1)     #若给一个闭合图形thickness参数设置为-1，那么这个图形会被填充。
# 5个参数分别为：要画的线所在的图像、中心点、半径、直线的颜色（BGR）、线条的粗细

cv.imshow('rectangle',img)
cv.waitKey()