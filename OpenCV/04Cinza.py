import cv2

imagem = cv2.imread('OpenCV/images/Lenna.png')

imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem transformada', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()