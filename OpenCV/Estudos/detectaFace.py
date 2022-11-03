import cv2 as cv

# Carregando algoritmos de detecção de uma face frontal
default = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

image = cv.imread('foto.jpg')

image_cinza = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


# Essa função me retorna 4 parâmetros 
# A posição (x, y), sendo essa posição o 'vertíce' superior esquerdo da imagem
# E também a largura e a altura da face reconhecida pelo algoritmo
face = default.detectMultiScale(image_cinza)

print(face)

for x, y, l, a in face:

    # A função retangulo recebe primariamente 5 argumentos
    # O primeiro sendo a imagem a ser analisada, seguido dos dois pontos de vertíce do retângulo
    # Um ponto inicial e outro ponto oposto a esse ponto inicial
    # Nesse caso estou definindo esses pontos como sendo o x, y iniciais(vertíce superior esquerdo) 
    # Da face identificada pelo algoritmo 'haarcascade_frontalface_default.xml' 
    # E o segundo pont sendo esses pontos iniciais
    # Somados da largura e altura aproximadas da respectiva da imagem
    # O quarto parâmetro é a cor do retângulo e por último a espessura da linha do mesmo
    cv.rectangle(image, (x, y), (x + l, y + a), (0, 255, 0), 3)


cv.imshow('Faces', image)
cv.waitKey(0)

key  = cv.waitKey(1)

if key % 256 == 27:
    print('Fechando a webcam')
    cv.destroyAllWindows()
