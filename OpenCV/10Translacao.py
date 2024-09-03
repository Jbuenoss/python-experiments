import	cv2
import	numpy	as	np
imagemOriginal	=	cv2.imread("OpenCV/images/Lenna.png")
totalLinhas,	totalColunas	=	imagemOriginal.shape[:2]
matriz	=	np.float32([[1,	0,	100],	[0,	1,	100]]) #[?,?, deslocamento horizontal], [?,?, deslocamento vertical]
imagemDeslocada	=	cv2.warpAffine(
				imagemOriginal,
				matriz,
				(totalColunas,	totalLinhas)
)
cv2.imshow("Resultado",	imagemDeslocada)
cv2.waitKey(0)
cv2.destroyAllWindows()
