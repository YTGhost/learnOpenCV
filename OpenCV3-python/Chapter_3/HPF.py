import cv2 as cv
import numpy as np
from skimage import io,data
from scipy import ndimage   #一个科学计算的库

kernel_3x3 = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                        [-1, 1, 2, 1, -1],
                        [-1, 2, 4, 2, -1],
                        [-1, 1, 2, 1, -1],
                        [-1, -1, -1, -1, -1]])
img = data.astronaut()
#img = io.imread("C:\VS-Python\learnOpenCV\OpenCV3-python\Chapter_3\Lena.jpg", as_grey=True)
#img = cv.imread("C:\VS-Python\learnOpenCV\OpenCV3-python\Chapter_3\Lena.jpg", 0)
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = cv.GaussianBlur(img, (11,11), 0)
g_hpf = img - blurred

cv.imshow("3x3", k3)
cv.imshow("5x5", k5)
cv.imshow("g_hpf", g_hpf)
cv.waitKey()
cv.destroyAllWindows()

