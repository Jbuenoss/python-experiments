import	cv2

imgOriginal	=	cv2.imread("OpenCV/images/Lenna.png",	0)
imgSuavizada	=	cv2.GaussianBlur(imgOriginal,	(13,13),	3)
imgDetalhes	=	3	*	cv2.subtract(imgOriginal,	imgSuavizada) #multilicada por 3 para realçar ainda mais as bordas.
imgRealcada	=	cv2.add(imgOriginal,	imgDetalhes)
cv2.imshow("Original",	imgOriginal)
cv2.imshow("Tratada",	imgSuavizada)
cv2.imshow("Bordas",	imgDetalhes)
cv2.imshow("Realcada",	imgRealcada)
cv2.waitKey(0)
cv2.destroyAllWindows()
