import cv2 as cv

# Carregando algoritmos de detecção de uma face frontal
default_face = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

image = cv.imread('imagem1.jpg')

image_cinza = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Alterando alguns parâmetros da função 'detectMultiScale' consigo aumentar levemente a precisão da detecção

face = default_face.detectMultiScale(image_cinza, scaleFactor=1.08, minNeighbors=3, minSize=(20, 20))


print(face)

for x, y, l, a in face:

    cv.rectangle(image, (x, y), (x + l, y + a), (0, 255, 0), 3)


cv.imshow('Faces', image)
cv.waitKey(0)

key  = cv.waitKey(1)

if key % 256 == 27:
    print('Fechando a webcam')
    cv.destroyAllWindows()