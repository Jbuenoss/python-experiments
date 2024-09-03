import cv2 as cv

image = cv.imread('images/Lenna.png')

azul, verde, vermelho = cv.split(image)     #ordem inversa do r-g-b
#opencv geralmente trata rgb como bgr

'''
#exibindo
cv.imshow("Canal	R",	vermelho)
cv.imshow("Canal	G",	verde)
cv.imshow("Canal	B",	azul)


#salvando as imagens
cv.imwrite('images/LenaaRed.jpeg', vermelho)
cv.imwrite('images/LennaGreen.jpeg', verde)
cv.imwrite('images/LenaaBlue.jpeg', azul)

cv.waitKey(0)
cv.destroyAllWindows()
'''

#	Combinando	os	três	canais	em	uma	única	imagem, invertendo o processo
imagem	=	cv.merge((azul,	verde, vermelho))
cv.imshow("Imagem",	imagem)
cv.waitKey(0)
cv.destroyAllWindows()


