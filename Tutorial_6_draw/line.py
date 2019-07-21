# 画一条蓝色的线
import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)
#创建一个图像，高为512，宽为512，三通道，数据类型为无符号8位

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
# 5个参数分别为：要画的线所在的图像、直线起点、直线终点、直线的颜色（BGR）、线条的粗细(px)

cv.imshow('line',img)
cv.waitKey()