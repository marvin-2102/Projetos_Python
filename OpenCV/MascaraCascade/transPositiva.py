import cv2 as cv
import os
from imutils import paths
import shutil

def listPosImagem():
    imagemPath = list(paths.list_images('Imagens/comMascara'))
    numero = 1
    if not os.path.exists('pos'):
        os.makedirs('pos')

    for foto in imagemPath:
        foto.replace(foto, f"pos/{str(numero)}.png")
        shutil.copy(foto, foto.replace(foto, f"pos/{str(numero)}.png"))
        img = cv.imread(f"pos/{str(numero)}.png", cv.IMREAD_GRAYSCALE)
        resized_image = cv.resize(img, (100, 100))
        cv.imwrite(f"pos/{str(numero)}.png", resized_image)

        print(foto.replace(foto, f"pos/{str(numero)}.png"))

        numero += 1

listPosImagem()
