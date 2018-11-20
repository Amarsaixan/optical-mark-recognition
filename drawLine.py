import numpy as np
import cv2
img =cv2.imread('cities.jpg')
cv2.namedWindow('image')
lines = []
file = open("citiesLocation.txt", "r")
for line in file:
	l = line.split()
	lines.append(l[0]+' '+l[1]+' '+l[2])
l2 = None
for e in range(len(lines)):
	l = lines[e].split()
	if e==0:
		l2 = lines[int(len(lines)-1)].split()
	cv2.line(img,(int(l[1]),int(l[2])),(int(l2[1]),int(l2[2])),(255,0,0),2)
	l2 = l
cv2.imshow('image',img)
while(1):
	cv2.imshow('image',img)
	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()