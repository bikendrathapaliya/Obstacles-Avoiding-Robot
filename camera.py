from picamera import PiCamera
import time
import cv2
import numpy as np
from config import WIDTH, HEIGHT, CHANNEL, MINIMUM_DISTANCE, CP_WIDTH, CP_HEIGHT
from ultrasonic import getDistance
#import  matplotlib.pyplot as plt

c = PiCamera()

def getImage():
	c.resolution = (HEIGHT, WIDTH)
	c.rotation = 270
	errors = False
	im = np.empty(( WIDTH, HEIGHT, 3), dtype=np.uint8)
	c.start_preview(fullscreen = False, window = (0, 100, CP_WIDTH, CP_HEIGHT))
	c.capture(im, 'bgr', use_video_port = True)
	time.sleep(2)
	#cv2.imshow('yolov3-tiny', im)
	#key = cv2.waitKey(15)
	#print(im.shape)	
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	#plt.imshow(im, cmap = 'gray')
	#plt.show()	
	im = im.reshape([-1, WIDTH, HEIGHT , CHANNEL])
	im = im / 255.	
	#print(im)
	#print(im.shape)
	dist = getDistance()
	if(dist < MINIMUM_DISTANCE):
		errors = True
	return im, errors

if __name__ == '__main__':
	getImage()
	c.close()
