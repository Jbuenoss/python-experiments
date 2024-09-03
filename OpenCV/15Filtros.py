import	cv2

imgOriginal	=	cv2.imread("OpenCV/images/Lenna.png")
imgTratada	=	cv2.blur(imgOriginal,	(5,5))
imgTratada2	=	cv2.GaussianBlur(imgOriginal,	(5,5),	0)
imgTratada3	=	cv2.medianBlur(imgOriginal,	5)
imgTratada4	=	cv2.bilateralFilter(imgOriginal,	9,	75,	75)


cv2.imshow("Original",	imgOriginal)
cv2.imshow("Tratada",	imgTratada)
cv2.imshow("TratadaG",	imgTratada2)
cv2.imshow("TratadaM",	imgTratada3)
cv2.imshow("TratadaB",	imgTratada4)
cv2.waitKey(0)
cv2.destroyAllWindows()
