import cv2 as cv
import os
from imutils import paths
import shutil

def listNegImagem():

    # Entra na pasta contendo as imagens negativas
    imagemPath = list(paths.list_images('Imagens/semMascara'))
    numero = 1

    # Cria uma pasta chamada 'neg'
    if not os.path.exists('neg'):
        os.makedirs('neg')

    # Percorre as imagens da pasta e cria uma imagem formatada em escala cinza
    for foto in imagemPath:

        foto.replace(foto, f"neg/{numero}.png")
        shutil.copy(foto, foto.replace(foto, f"neg/{numero}.png"))
        img = cv.imread(f"neg/{numero}.png", cv.IMREAD_GRAYSCALE)
        resized_image = cv.resize(img, (100, 100))
        cv.imwrite(f"neg/{numero}.png", resized_image)

        print(foto.replace(foto, f"neg/{numero}.png"))

        numero += 1

# Chama a função
listNegImagem()

