import cv2 as cv

image = cv.imread('formas.png', 0)

ret, limiar = cv.threshold(image, 127, 255, 0)

contornos,_ = cv.findContours(limiar, 1, 3)

# Pegando o primeiro contorno
contorno = contornos[0]

# Calcula os "momentos" da imagem. Se o vetor de input for do tipo numpy, deve ser do tipo np.int32 ou np.float32
momento = cv.moments(contorno)

print(momento)

# Para esses momentos o calculo do centroide é feito por: Cx = m10/m00 e Cy = m01/m00
cx = momento['m10'] / momento['m00']
cy = momento['m01'] / momento['m00']
print(cx, cy)

# Área de um contorno

area = cv.contourArea(contorno)
print(area)

# O perímetro

perimetro = cv.arcLength(contorno, True)
print(perimetro)

# Aproximação do contorno

x,y,w,h = cv.boundingRect(contorno)
cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow("Imagem", image)
cv.waitKey(0)

# Rotated Rectangle

import numpy as np

rect = cv.minAreaRect(contorno)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(image,[box], 0, (0,0,255), 2)
