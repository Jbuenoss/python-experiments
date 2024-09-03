import cv2

imagem = cv2.imread('OpenCV/images/Lenna.png')

pixel = imagem[200][200]
print(pixel)

pixel = imagem[200][200][0]
print(pixel)

print('Informacoes sobre a imagem: linha, colunas, canais de cor')
print(imagem.shape)
pix = str(imagem.size)
print('col x linha x canais: ' + pix)
n = int(pix)
n /= 3
pix = str(n)
print('pixels: ' + pix)

imagem[200,200] = [0,0,0]       #outra forma de representar matriz
cv2.imshow('modificado', imagem)
cv2.waitKey(0)