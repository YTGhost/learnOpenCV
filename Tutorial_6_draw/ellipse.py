# 画一个红色的半椭圆
import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)
#创建一个图像，高为512，宽为512，三通道，数据类型为无符号8位

cv.ellipse(img,(256,256),(100,50),0,0,180,(0,0,255),-1)     #若给一个闭合图形thickness参数设置为-1，那么这个图形会被填充。
# 5个参数分别为：要画的线所在的图像、中心点、长轴和短轴的长度、椭圆沿逆时针方向旋转的角度、
# 、椭圆沿顺时针方向起始角度、椭圆沿顺时针方向结束角度、线的颜色（BGR）、线条的粗细

cv.imshow('ellipse',img)
cv.waitKey()