import	cv2
import	numpy	as	np
from	matplotlib	import	pyplot	as	grafico

imagemOriginal	=	cv2.imread("OpenCV/images/Lenna.png")
	
imagem	=	cv2.cvtColor(imagemOriginal,	cv2.COLOR_BGR2HSV)
matiz,	saturacao,	valor	=	cv2.split(imagem)

valor = cv2.equalizeHist(valor)     #a equalização de imagens coloridas é só com o valor

imagemEqualizada = cv2.merge((matiz, saturacao,	valor))
imagemEqualizada = cv2.cvtColor(imagemEqualizada, cv2.COLOR_HSV2BGR)

cv2.imwrite("OpenCV/images/LennaEqualizadaCerto.png", imagemEqualizada)

cv2.imshow("Imagem	Original",	imagemOriginal)
cv2.imshow("Imagem	Equalizada",	imagemEqualizada)

grafico.hist(imagemOriginal.ravel(),	256,	[0,256])
grafico.figure()
grafico.hist(imagemEqualizada.ravel(),	256,	[0,256])
grafico.show()
