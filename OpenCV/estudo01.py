import cv2 as cv 

image = cv.imread('branco.jpeg')
image_cinza = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Aqui estou realizando o processo de limiarização, basicamente o primeiro argumento
# Eu delimito um tom de cinza, e logo em seguida com transformando os pixels com um certo tom de cinza
# Em branco(255), e os demais em preto(0)ou algum outro limiar, como o "THRESH_BINARY"
ret, limiar = cv.threshold(image_cinza, 127, 255, 0)


contornos,_ = cv.findContours(limiar, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Cada contorno é guardado como um vetor
# O segundo argumento tem que sempre ser em formato de lista
# Se o terceiro parâmetro(contourldx) for negativo, ele ira pintar todos os contornos
# O quinto parâmetro define a espessura da pintura

cv.drawContours(image, contornos, 0, (0, 255, 0), 3, maxLevel=1)

# Após cada uso do imshow a função "waitKey" tem de ser chamado logo após
# Sem isso o computador não irá realizar o processamento de interfáce para mostrar a imagem formatada
cv.imshow('Imagem', image)
cv.waitKey(0)

key  = cv.waitKey(1)

if key % 256 == 27:
    print('Fechando Tela')
    cv.destroyAllWindows()
