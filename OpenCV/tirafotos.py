import cv2 as cv
import shutil
from time import sleep
import os

# Inicializa a webcam
cam = cv.VideoCapture(0)

# Tiulo da janela
#cv.namedWindow('Câmera do Robô')

# Acessa e conta quantas imagens já estão na pasta

path_mascara = 'Imagens/comMascara'
path_sem = 'Imagens/semMascara'

img_countN = os.listdir(path_sem)
img_counterN = len(img_countN)

img_countP = os.listdir(path_mascara)
img_counterP = len(img_countP)


while True:
    # Armazenando os valores da câmera
    verificador, frame = cam.read()
    # Se nenhum objeto for encontrado, o programa avisa

    if not verificador:
        print('Falha em reconhecer objeto')
        break
    # Vai mostrar o título do frame
    cv.imshow('Testando', frame)
    key = cv.waitKey(1)
    # Se a tecla 'ESC' for pressionada, o programa para

    if key % 256 == 27:
        print('Fechando Webcam')
        break

    elif key % 256 == 110:
        # Como a imagem será salva
        count = 0
        sleep(5)
        print("Começando a tirar as fotos Negativas")
        while count < 1400:
            sleep(0.01)
            img_name = (f'{img_counterN}.png')
            # Salva a imagem
            cv.imwrite(f'{img_name}', frame)

            # Move as imagem para a pasta que eu quero
            shutil.move(f'{img_name}', f'Imagens/semMascara/{img_name}')
            # Adiciona 1 ao número de imagem salvas
            img_counterN += 1
            count += 1
        break

    elif key % 256 == 109:
        count = 0
        print("Começando a tirar as fotos Positivas")
        sleep(5)
        while count < 2500:
            # Como a imagem será salva
            sleep(0.01)
            img_name = (f'{img_counterP}.png')
            # Salva a imagem
            cv.imwrite(f'{img_name}', frame)

            # Move as imagem para a pasta que eu quero
            shutil.move(f'{img_name}', f'Imagens/comMascara/{img_name}')
            # Adiciona 1 ao número de imagem salvas
            img_counterP += 1
            count += 1
        break

# Libera a webcam
# cv.release()

# Fecha todas as janelas
cv.destroyAllWindows()

