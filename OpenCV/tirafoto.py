# importing the python open cv library
import cv2 as cv
import shutil
import os
# intialize the webcam and pass a constant which is 0
cam = cv.VideoCapture(0)

# title of the app
cv.namedWindow('Câmera do Robô')

# Conta quantas imagens já estão na pasta

path = '/home/marcus/Documentos/UFRN/identificando/imagens'
img_count = os.listdir(path)

# let's assume the number of images gotten is 0
img_counter = len(img_count)

# while loop
while True:
    # intializing the frame, ret
    ret, frame = cam.read()
    # if statement
    if not ret:
        print('Falha em reconhecer objeto')
        break
    # the frame will show with the title of test
    cv.imshow('Testando', frame)
    #to get continuous live video feed from my laptops webcam
    key  = cv.waitKey(1)
    # if the escape key is been pressed, the app will stop
    if key%256 == 27:
        print('Fechando Webcam')
        break
    # if the spacebar key is been pressed
    # screenshots will be taken
    elif key%256  == 32:
        # the format for storing the images scrreenshotted
        img_name = f'Forma{img_counter}.png'
        # saves the image as a png file
        cv.imwrite(f'{img_name}', frame)

        shutil.move(f'/home/marcus/Documentos/UFRN/{img_name}', f'/home/marcus/Documentos/UFRN/identificando/imagens/{img_name}')
        print('Foto Tirada!')
        # the number of images automaticallly increases by 1
        img_counter += 1

# release the camera
cv.release()

# stops the camera window
cv.destoryAllWindows()
                          