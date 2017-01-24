import cv2
import numpy as np
import time
import math


faceCascade = cv2.CascadeClassifier('face_cascade.xml')
eyeCascade = cv2.CascadeClassifier('eye_cascade.xml')

print("Camera Startup....Wait")
camera = cv2.VideoCapture(0)
#open camera

while 1:
	retVal,img=camera.read()
	monocolor=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces= faceCascade.detectMultiScale(monocolor,1.2,4);

	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y),(x+w,y+h),(238,130,238),2)
		
		eye_space_color=img[y:y+h,x:x+h]
		eye_space_mono=monocolor[y:y+h,x:x+w]
		#eyes exist inside the face
		eyes=eyeCascade.detectMultiScale(eye_space_mono,1.2,5)

		for (xx,yy,ww,hh) in eyes:
			cv2.rectangle(eye_space_color,(xx,yy),(xx+ww,yy+hh),(255,255,255),1)

	cv2.imshow('That Detection',img)
	k = cv2.waitKey(10) & 0xff
	if k == 27 :
		break   

camera.release()
exit()