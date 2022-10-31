import cv2 as cv
import mediapipe as mp
from time import time

mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

camera = cv.VideoCapture(0)

with mp_objectron.Objectron(static_image_mode=False, 
                            max_num_objects=2,
                            min_detection_confidence=0.5,    
                            min_tracking_confidence=0.8,    
                            model_name='Cup') as objectron:

    while camera.isOpened():

        verificador, imagem = camera.read()
        
        inicio = time()
        
        # Converte as cores do padrão BGR, para o padrão RGB
        imagem = cv.cvtColor(imagem, cv.COLOR_BGR2RGB)

        # Deixamos a imagem mais leve ao tirar a permissão de write dela
        # Logo após nós a processamos e a salvamos 
        imagem.flags.writeable = False
        results =  objectron.process(imagem)

        # Então devolvemos o atributo write para ser usado depois
        imagem.flags.writeable = True
        imagem = cv.cvtColor(imagem, cv.COLOR_RGB2BGR)

       
        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(imagem, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                mp_drawing.draw_axis(imagem, detected_object.rotation, detected_object.translation)


        termino = time()

        tempo_total = termino - inicio

        fps = 1 / tempo_total

        cv.putText(imagem, f'FPS: {int(fps)}', (20, 70), cv.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 0), 2)

        key = cv.waitKey(1)

        if key%256 == 27:
            break

camera.release()
cv.destroyAllWindows()



