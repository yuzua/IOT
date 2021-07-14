sudo apt-get insatll libhdf5-dev libhdf5-serial-dev
sudo pip3 install opencv-python

import cv2
image = cv2.imread("/home/pi/Desktop/opencv/face.jpg")

casceade_file = "/home/pi/Desktop/opencv/haarcascade_frontalface_alt.xml"

cascade = cv2.CascadeClassifier(casceade_file)

face_list = cascade.detectMultiScale(image)

color = (0, 0, 255)

if len(face_list) > 0:
    for face in face_list:
        x, y, w, h = face
        cv2.rectangle(image, (x,y), (x+w))