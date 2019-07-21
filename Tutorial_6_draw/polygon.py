# 画一个黄色的具有四个顶点的多边形，并添加‘OpenCV’文字

import cv2 as cv
import numpy as np

# Create a black image
img = np.zeros((512,512,3), np.uint8)
#创建一个图像，高为512，宽为512，三通道，数据类型为无符号8位

font = cv.FONT_HERSHEY_SIMPLEX

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
# 这里 reshape 的第一个参数为-1，表明这一维的长度是根据后面的维数计算出来的。
# 如果第三个参数是False,我们得到的多边形是不闭合的（首尾不相连）。
cv.polylines(img,[pts],True,(0,0,255),1)    #图像、点集、是否闭合、颜色、线条粗细
cv.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv.LINE_AA)    #图像、绘制的文字、位置、字型、字体大小、文字颜色、粗细、线型   
#linetype用cv.LINE_AA字体会流畅一些，更好看

cv.imshow('polygon',img)
cv.waitKey()
