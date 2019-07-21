# 画一个绿色的矩形
import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)
#创建一个图像，高为512，宽为512，三通道，数据类型为无符号8位

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
# 5个参数分别为：要画的线所在的图像、左上顶点、右下顶点、直线的颜色（BGR）、线条的粗细（px）

cv.imshow('rectangle',img)
cv.waitKey()