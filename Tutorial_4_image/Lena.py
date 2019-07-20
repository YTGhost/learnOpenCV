import cv2

#cv2.imread(’地址‘，显示参数)   用来读入图像
#cv2.imshow(’窗口名称‘，显示图像变量)   用来显示图像
#cv2.imwrite(’文件名‘，显示图像变量)  用来保存一个图像
a = cv2.IMREAD_UNCHANGED    #值为-1
b = cv2.IMREAD_COLOR        #值为1
c = cv2.IMREAD_GRAYSCALE    #值为0
print(a,b,c)
img = cv2.imread('C:\VS-Python\learnOpenCV\Tutorial_4_image\Lena.jpg',0)  #说明图片路径
cv2.imshow("Lena.jpg",img)
cv2.waitKey()
cv2.destroyAllWindows()