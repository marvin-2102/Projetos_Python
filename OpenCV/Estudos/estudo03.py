import cv2 as cv

# Carregando algoritmos de detecção de uma face frontal
default = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

image = cv.imread('foto.jpg')

image_cinza = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

face = default.detectMultiScale(image_cinza)

print(face)

for x, y, l, a in face:

    # A função retangulo recebe primariamente 5 argumentos
    # O primeiro sendo a imagem a ser analisada, seguido dos dois pontos de vertíce do retângulo
    # Um ponto inicial e outro ponto oposto a esse ponto inicial
    # Nesse caso estou definindo esses pontos como sendo o x, y iniciais da face identificada pelo
    # Algoritmo 'haarcascade_frontalface_default.xml' e o segundo pont sendo esses pontos iniciais
    # Somados da largura e altura respectiva da imagem
    # O quarto parâmetro é a cor do retângulo e por último a espessura da linha do mesmo
    cv.rectangle(image, (x, y), (x + l, y + a), (0, 255, 0), 3)


cv.imshow('Faces', image)
cv.waitKey(0)

key  = cv.waitKey(1)

if key % 256 == 27:
    print('Fechando a webcam')
    cv.destroyAllWindows()
