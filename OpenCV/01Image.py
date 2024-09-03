import cv2

imagem = cv2.imread("OpenCV/images/Lenna.png")
cv2.imshow("legenda da tela", imagem)
cv2.waitKey(0)          #espera 1 tempo para uma tecla ser digitada, 0 = infinito
cv2.destroyAllWindows()     #fecha todas as janelas de uma só vez, quando clickar qualquer coisa dentro de uma janela


