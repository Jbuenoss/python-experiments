import	cv2
captura	=	cv2.VideoCapture("videos/cat.mp4")
while True:
		ret,	frame	=	captura.read()
		cv2.imshow("Imagem",	frame)
		if	cv2.waitKey(20)	&	0xFF	==	ord("q"):       #o programa ira parar com o q
				break
captura.release()       #fecha o video
cv2.destroyAllWindows()

#erro 215 diz que terminou o video e não encontrou mais nenhum frame

'''Webcam
import	cv2
captura	=	cv2.VideoCapture(0)
while True:
		ret,	frame	=	captura.read()
		cv2.imshow("Imagem",	frame)
		if	cv2.waitKey(1)	&	0xFF	==	ord("q"):
				break
captura.release()
cv2.destroyAllWindows()

'''