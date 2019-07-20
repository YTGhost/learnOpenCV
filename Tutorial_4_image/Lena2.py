import cv2

#imwrite()函数用来保存图像

img = cv2.imread('C:\VS-Python\learnOpenCV\Tutorial_4_image\Lena.jpg',0)  #说明图片路径
cv2.namedWindow('image',cv2.WINDOW_NORMAL)  #创建一个名为image的窗口，该窗口大小可随意变化
cv2.imshow('image',img)     #当这里面窗口名字与nameWindow相同时生成一个名为image的可变大小窗口。若这里名字不同，则生成不同的两个窗口。
cv2.imwrite('C:\VS-Python\learnOpenCV\Tutorial_4_image\Lenagray.jpg',img) #保存灰度模式处理后的图片
cv2.waitKey()
cv2.destroyAllWindows()