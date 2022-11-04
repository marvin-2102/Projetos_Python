import cv2 as cv
import os
from imutils import paths
import shutil

def listNegImagem():
    imagemPath = list(paths.list_images('Imagens/semMascara'))
    numero = 1
    if not os.path.exists('neg'):
        os.makedirs('neg')

    for foto in imagemPath:
        foto.replace(foto, f"neg/{str(numero)}.png")
        shutil.copy(foto, foto.replace(foto, f"neg/{str(numero)}.png"))
        img = cv.imread(f"neg/{str(numero)}.png", cv.IMREAD_GRAYSCALE)
        resized_image = cv.resize(img, (100, 100))
        cv.imwrite(f"neg/{str(numero)}.png", resized_image)

        print(foto.replace(foto, f"neg/{str(numero)}.png"))

        numero += 1

listNegImagem()


