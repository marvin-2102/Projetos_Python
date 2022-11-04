import cv2 as cv

# O valor do VideoCapture() é 0 apenas em notebooks
# Num PC normal, o valor padrão é 1 ou 2
webcam = cv.VideoCapture(0)

default_face = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
default_olhos = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')

while True:

    # O webcam.read() retorna cada frame(foto) da webcam a cada momento
    verificador, frame = webcam.read()

    # Assim, tratamos o frame da mesma forma que fizemos com as imagems anteriores
    frame_cinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face = default_face.detectMultiScale(frame_cinza)

    for x, y, l, a in face:

        cv.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 3)

        olhos = frame[y: y + a, x: x + l]
        olhos_cinza = cv.cvtColor(olhos, cv.COLOR_BGR2GRAY)
        olhos_regiao = default_olhos.detectMultiScale(olhos_cinza, scaleFactor=1.05, minNeighbors=4)

        for olhox, olhoy, olhoL, olhoA in olhos_regiao:
            cv.rectangle(olhos, (olhox, olhoy), (olhox + olhoL, olhoy + olhoA), (0, 0, 255), 3)


    cv.imshow('Video Webcam', frame)

    key = cv.waitKey(1)

    if key % 256 == 27:
        print('Fechando Tela')
        break
