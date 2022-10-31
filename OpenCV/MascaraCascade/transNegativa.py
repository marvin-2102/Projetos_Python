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



# def store_raw_images():
#     neg_images_link = '//image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
#     neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
#     pic_num = 1
#
#     if not os.path.exists('neg'):
#         os.makedirs('neg')
#
#     for i in neg_image_urls.split('\n'):
#         try:
#             print(i)
#             urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
#             img = cv.imread("neg/"+str(pic_num)+".jpg",cv.IMREAD_GRAYSCALE)
#             # should be larger than samples / pos pic (so we can place our image on it)
#             resized_image = cv.resize(img, (100, 100))
#             cv.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
#             pic_num += 1
#
#         except Exception as e:
#             print(str(e))
