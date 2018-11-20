import cv2
import numpy as np
cit = open("cities.txt", "r")
citiesArray=[]
citiesLocation=[]
for line in cit:
	l = line.split()
	citiesArray.append(l[0])

file = open("citiesLocation.txt", "w")
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,255,0),-1)
        tmp = str(x)+' '+str(y)+'\n'
        citiesLocation.append(tmp)
        print(tmp)
img =cv2.imread('cities.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
	cv2.imshow('image',img)
	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()

for t in range(len(citiesLocation)):
	file.write(str(citiesArray[t])+' '+str(citiesLocation[t]))

file.close()