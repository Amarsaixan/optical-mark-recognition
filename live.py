import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage	

def isFilled(crop_img, mor, bagana):
	bl = 0
	wh = 0
	for k in range(mor):
		for l in range(bagana):
			if[k,l] == 0:
				wh+=1
			else:
				bl+=1
	if bl>=wh:
		return True
	else:
		return False

def check(ff):
	rows,cols,ch = frame.shape
	print("rows,cols"+str(rows)+str(cols))
	blank_image = np.zeros((rows,cols,3), np.uint8)
	bagana = int(cols/10)
	mor = int(rows/25)
	for i in range(mor,rows,mor):
		for j in range(bagana,cols,bagana):
			crop_img = ff[i:i+mor, j:j+bagana]
			if isFilled(crop_img, mor, bagana):
				print(str(i)+' -- '+str(j))
				for k in range(mor):
					for l in range(bagana):
						if i+k<480:
							if j+l<480:
								blank_image[i+k, j+l] = 200

	cv2.imshow('result', blank_image)
cap = cv2.VideoCapture(0)
screenCnt = None
file = open("mydata.txt", "w")

while(True):
    ret, frame = cap.read()
    #frame = imutils.resize(frame, height = 500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    #print("cnts:")
    #print(cnts)
    for c in cnts:
    	peri = cv2.arcLength(c, True)
    	approx = cv2.approxPolyDP(c, 0.01 * peri, True)
    	if len(approx) == 4:
    		screenCnt = approx
    		break

    if screenCnt is None:
    	print("None screenCnt")
    else:
    	print("detected")
    	print(len(screenCnt))
    	file.write(str(screenCnt))
    	file.write("\n")
    	cv2.drawContours(frame, [screenCnt], -1, (0, 255, 0), 2)
    	for f in range(len(screenCnt)):
    		print("-----")
    		cv2.circle(frame, (screenCnt[f][0][0], screenCnt[f][0][1]), 8, [255, 0, 0], thickness=5, lineType=8, shift=0) 
    cv2.imshow('frame',frame)
    screenCnt = None
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(33) == ord('a'):
    	print("captured a")
    	cv2.imwrite('captured.png',frame)
    	#height, width, channels = frame.shape
    	#print(str(height)+":"+str(width))

    	rows,cols,ch = frame.shape
    	pts1 = np.float32(screenCnt)
    	print(screenCnt)
    	#pts2 = np.float32([[0,0],[639,0],[0,479],[639,479]])
    	#pts2 = np.float32([[0,0],[479,0],[0,639],[479,639]])
    	pts2 = np.array([
			[0, 0],
			[480 - 1, 0],
			[480 - 1, 640 - 1],
			[0, 640 - 1]], dtype = "float32")
    	M = cv2.getPerspectiveTransform(pts1,pts2)
    	dst = cv2.warpPerspective(frame,M,(480,640))
    	ff = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    	#COLOR_BGR2HSV
    	ff =  cv2.flip( ff, 1)
    	#ff[np.where((ff == [0] ).all(axis = 1))] = [255]
    	rs,cs = ff.shape
    	for x in range(0,rs-1):
    		for y in range(0,cs-1):
    			if ff[x,y]<=200:
    				ff[x,y] = 0
    			else:
    				ff[x,y] = 255
    	cv2.imshow('image', ff)
    	check(ff)
    	
    	plt.subplot(121),plt.imshow(frame),plt.title('Input')
    	plt.subplot(122),plt.imshow(dst),plt.title('Output')
    	plt.show()
    	break

cap.release()
cv2.destroyAllWindows()
file.close()






