import	cv2
import	numpy	as	np
imagemOriginal	=	cv2.imread("OpenCV/images/Lenna.png",	0)
totalLinhas,	totalColunas	=	imagemOriginal.shape
matriz	=	cv2.getRotationMatrix2D(    #fazer a matriz de rotação
				(totalColunas	/	2,	totalLinhas	/	2),	90,	1
)
imagemRotacionada	=	cv2.warpAffine(
				imagemOriginal,
				matriz,
				(totalColunas,	totalLinhas)
)
cv2.imshow("Resultado",	imagemRotacionada)
cv2.waitKey(0)
cv2.destroyAllWindows()