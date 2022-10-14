import cv2 as cv
import shutil
import os
# Inicializa a webcam
cam = cv.VideoCapture(0)

# Tiulo da janela
cv.namedWindow('Câmera do Robô')

# Acessa e conta quantas imagens já estão na pasta

path = 'camiho da pasta imagens'
img_count = os.listdir(path)
img_counter = len(img_count)

while True:
    # Armazenando os valores da câmera
    ret, frame = cam.read()
    # Se nenhum objeto for encontrado, o programa avisa
    if not ret:
        print('Falha em reconhecer objeto')
        break
    # Vai mostrar o título do frame
    cv.imshow('Testando', frame)
    key  = cv.waitKey(1)
    # Se a tecla 'ESC' for pressionada, o programa para
    if key%256 == 27:
        print('Fechando Webcam')
        break
        
    # Se a tecla SPACEBAR for pressionada, uma print da webcam é tirada
    elif key%256  == 32:
        # Cmo a imagem será salva
        img_name = f'Forma{img_counter}.png'
        # Salva a imagem
        cv.imwrite(f'{img_name}', frame)
           
        # Move as imagem para a pasta que eu quero
        shutil.move(f'pasta em que a imagem fica salva inicialmente/{img_name}', f'camiho da pasta imagens/{img_name}')
        print('Foto Tirada!')
        # Adiciona 1 ao número de imagem salvas
        img_counter += 1

# Libera a webcam
cv.release()

# Fecha todas as janelas
cv.destoryAllWindows()
                          
