import	cv2
import	numpy	as	np

imagemOriginal	=	cv2.imread("OpenCV/images/Captura de tela 2024-01-16 063454.png")
pontosIniciais	=	np.float32(
				[[128,56],	[301,54],	[129,242],	[318,240]]
)
pontosFinais	=	np.float32(
				[[0,0],	[500,0],	[0,500],	[500,500]]
)
matriz	=	cv2.getPerspectiveTransform(
				pontosIniciais,	pontosFinais
)
imagemModificada	=	cv2.warpPerspective(
				imagemOriginal,	matriz,	(500,	500)
)
cv2.imshow("Imagem	Original",	imagemOriginal)
cv2.imshow("Imagem	Modificada",	imagemModificada)
cv2.waitKey(0)
cv2.destroyAllWindows()
