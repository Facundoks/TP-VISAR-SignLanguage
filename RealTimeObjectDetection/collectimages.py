import cv2
import os
import time
import uuid

IMAGES_PATH = 'TensorFlow/workspace/images/collectedimages'

labels = ['duele', 'sí', 'no', 'alérgico', 'remedio', 'grupo', 'A', 'B', 'O', 'positivo', 'negativo']
number_images = 15

for label in labels:
    directory = os.path.join(IMAGES_PATH, label)
    os.makedirs(directory, exist_ok=True)    
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_images):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label+'.'+'.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()