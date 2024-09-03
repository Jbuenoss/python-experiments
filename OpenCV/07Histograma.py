import	cv2
import	numpy	as	np
from	matplotlib	import	pyplot	as	grafico

imagem	=	cv2.imread("OpenCV/images/detalhe-bitmap.bmp",	0) #0 significa que vai ser lido em tons de cinza
grafico.hist(imagem.ravel(),	256,	[0,256]) #ravel() transforma a imagem num vetor


imagem	=	cv2.imread("OpenCV/images/Lenna.png")
azul,	verde,	vermelho	=	cv2.split(imagem)
grafico.figure()        #nova figura sera gerada
grafico.hist(azul.ravel(),	256,	[0,256])
grafico.figure()
grafico.hist(verde.ravel(),	256,	[0,256])
grafico.figure()
grafico.hist(vermelho.ravel(),	256,	[0,256])

grafico.show()