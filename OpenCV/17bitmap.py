import cv2 as cv

imagem = cv.imread("OpenCV/images/detalhe-bitmap.bmp", cv.IMREAD_GRAYSCALE)
#poderia no lugar de GRAYSCALE: 0.

value = 127     #meio da escala cinza
_, binary_image = cv.threshold(imagem, value, 255, cv.THRESH_BINARY_INV)

cv.imshow("OpenCV/images/realBitmap.bmp", binary_image)

cv.waitKey(0)
cv.destroyAllWindows()