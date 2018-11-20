import numpy as np
import cv2
import os
bubbled = []
file = open("balckAndWhite.txt", "w")
ANSWER_KEY = {0: 0, 1: 2, 2: 3, 3: 0, 4: 0, 5: 1, 6: 2, 7: 3, 8:1, 9: 0, 10: 2, 11: 3, 12: 0, 13: 3, 14: 0, 15: 1, 16: 2, 17: 3, 18: 2, 19: 0, 20: 1, 21: 2, 22: 0, 23: 1, 24: 0}
def maskFrame(mask):
    rs,cs = mask.shape
    for x in range(0,rs-1):
    	for y in range(0,cs-1):
    		if mask[x,y]<=155:
    			mask[x,y] = 0
    		else:
    			mask[x,y] = 255	
    return mask
def isFilled(crop_img,black, white):
	mor,bagana = crop_img.shape
	for k in range(mor-1):
		for l in range(bagana-1):
			if crop_img[k,l] == 0:
				white=white+1
			else:
				black=black+1
	print("::"+str(black)+","+str(white))
	file.write(str(black)+", "+str(white))
	if black>=white*1.3:
		return True
	else:
		return False
def check(ff):
	correct = 0
	rows,cols = ff.shape
	print("rows,cols"+str(rows)+str(cols))
	blank_image = np.zeros((rows,cols,3), np.uint8)
	#cv2.imshow('blank_image', blank_image)
	bagana = int(cols/5)
	mor = int(rows/21)
	for i in range(mor,rows,mor):
		for j in range(bagana,cols,bagana):
			#print(str(i)+","+str(j))
			crop_img = ff[i:i+mor, j:j+bagana]
			if isFilled(crop_img,0,0) is not False:
				#print("filled", str(i)+","+str(j))
				print(str(i)+' -- '+str(j))
				
				for i1 in range(i, i+mor, 1):
					for j1 in range(j, j+bagana, 1):
						blank_image[i1, j1]=[0,255,0]
			else:
				correct+=1
				bubbled.append((int(i/mor),(int(j/bagana))))

	cv2.imshow('resultt', blank_image)
	cv2.imwrite("checked.png", blank_image)  
	for x in range(len(bubbled)):
		print(bubbled[x])
	#k = ANSWER_KEY[q]

	print("corrected"+ str(correct))
img = cv2.imread('jpeg.jpg', 0)
rows,cols = img.shape 
print(cols)
#check(img)

cv2.imshow('orig',img)


#cv2.imshow('masked', maskFrame(img))
check(maskFrame(img))
#tt = maskFrame(img);
#crop_img = tt[85:85+85, 133:133+133]
#cv2.imshow('orig',crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
file.close()
