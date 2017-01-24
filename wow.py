import numpy as np 
import cv2
import ctypes

img_source = input("File name: ")

img=cv2.imread(img_source,1)
mono=cv2.imread(img_source,0)#greyscale image

faceCascade = cv2.CascadeClassifier('face_cascade.xml')
#eyeCascade = cv2.CascadeClassifier('eye_cascade.xml')

faces=faceCascade.detectMultiScale(mono,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(152,125,254),2)

cv2.imshow('lol',img)
ctypes.windll.user32.MessageBoxW(0, "Found {} faces".format(len(faces)), "Faces Found", 1)

chk = input("Press any key to exit ")
exit()