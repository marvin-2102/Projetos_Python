import cv2 as cv
import os
from imutils import paths
import shutil

def listPosImagem():

    # Entra na pasta contendo as imagens positivas
    imagemPath = list(paths.list_images('Imagens/comMascara'))
    numero = 1

    # Cria uma pasta chamada 'pos'
    if not os.path.exists('pos'):
        os.makedirs('pos')

    # Percorre as imagens da pasta e cria uma imagem formatada em escala cinza
    for foto in imagemPath:

        foto.replace(foto, f"pos/{numero}.png")
        shutil.copy(foto, foto.replace(foto, f"pos/{numero}.png"))
        img = cv.imread(f"pos/{numero}.png", cv.IMREAD_GRAYSCALE)
        resized_image = cv.resize(img, (100, 100))
        cv.imwrite(f"pos/{numero}.png", resized_image)

        print(foto.replace(foto, f"pos/{str(numero)}.png"))

        numero += 1

# Chama a função
listPosImagem()
