import cv2 as cv

# Carregando algoritmos de detecção de uma face frontal
default_face = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# Carregando algoritmos de detecção de olhos
default_olhos = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')

image = cv.imread('imagens/imagem7.jpg')

image_cinza = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

face = default_face.detectMultiScale(image_cinza)

print(face)

for x, y, l, a in face:

    cv.rectangle(image, (x, y), (x + l, y + a), (0, 255, 0), 3)

    # Com esssa váriavel eu guardo apenas a região da imagem onde os olhos estão localizados
    # Ao pegar a região da face que o programa já consegue identificar com certa acuidade
    # Eu seleciono a região dos olhos ao dizer que o ponto x incial é o y incial mais a altura da região
    # E no y o procedimento oposto

    # olhos = image[168: 332, 115: 163]
    olhos = image[y: y + a, x: x + l]
    olhos_cinza = cv.cvtColor(olhos, cv.COLOR_BGR2GRAY)
    cv.imshow('Olhos', olhos_cinza)
    cv.waitKey(0)
    olhos_regiao = default_olhos.detectMultiScale(olhos_cinza)

    print(olhos_regiao)

    # Percorrendo a região delimitada dos olhos
    for olhox, olhoy, olhoL, olhoA in olhos_regiao:
        cv.rectangle(olhos, (olhox, olhoy), (olhox + olhoL, olhoy + olhoA), (0, 0, 255), 3)


cv.imshow('Olhos', olhos_cinza)
cv.imshow('Olhos', image)
cv.waitKey(0)