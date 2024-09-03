import cv2
import numpy as np

imgRGB = cv2.imread("OpenCV/images/LennaEqualizada.png")
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

color = np.uint8([[[255, 0, 0]]])
color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

claro = np.uint8([[[color[0, 0, 0]-20, 100, 100]]]) 
escuro = np.uint8([[[color[0, 0, 0]+20, 255, 255]]]) 

kernel = np.ones((2,1), np.uint8)

imgsegmentada = cv2.inRange(imgHSV, claro, escuro)
imgsegmentada = cv2.erode(imgsegmentada, kernel, iterations=1)
imgsegmentada = cv2.dilate(imgsegmentada, kernel, iterations=2)

valorMedio = cv2.mean(imgRGB)
print(valorMedio)

cv2.imshow("original", imgRGB)
cv2.imshow("Seg", imgsegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()