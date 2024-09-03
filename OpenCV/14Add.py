import	cv2
import	numpy	as	np
from	matplotlib	import	pyplot	as	grafico

'''
imagemFichasVermelhas	=	cv2.imread("fichas-vermelhas.bmp")
imagemFichasPretas	=	cv2.imread("fichas-pretas.bmp")
imagem	=	cv2.add(imagemFichasVermelhas,	imagemFichasPretas)
cv2.imshow("Resultado",	imagem)

ou imagem	=	cv2.subtract(imagemFichaPosicao1,	imagemFichaPosicao2)
'''
imagemOriginal	=	cv2.imread("OpenCV/images/Lenna.png",	0)
imagemClara	=	cv2.add(imagemOriginal,	40)
imagemEscura	=	cv2.add(imagemOriginal,	-40)
cv2.imshow("Imagem	Original",	imagemOriginal)
cv2.imshow("Imagem	Clara",	imagemClara)
cv2.imshow("Imagem	Escura",	imagemEscura)
grafico.hist(imagemOriginal.ravel(),	256,	[0,256])
grafico.figure()
grafico.hist(imagemClara.ravel(),	256,	[0,256])
grafico.figure()
grafico.hist(imagemEscura.ravel(),	256,	[0,256])
grafico.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
