import cv2

img = cv2.imread('C:\VS-Python\learnOpenCV\Tutorial_4_image\Lena.jpg',0)  #以灰度模式读入
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:     #wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):     #wait for 's' key to save and exit
    cv2.imwrite('C:\VS-Python\learnOpenCV\Tutorial_4_image\Lenagary2.jpg',img)
    cv2.destroyAllWindows()