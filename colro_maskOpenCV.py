import cv2
import numpy as np

def fn(x):
	pass

windowName ="Window" 
# window name
cv2.namedWindow(windowName) 
   
# there trackbars which have the name
# of trackbars min and max value 
cv2.createTrackbar('a', windowName, 30, 255, fn)
cv2.createTrackbar('b', windowName, 50, 255, fn)
cv2.createTrackbar('c', windowName, 80, 255, fn)

img = cv2.imread('Emerald_Lakes_New_Zealand.jpg')
img = cv2.resize(img, None, fx=0.2, fy=0.2)

while True:
	a = cv2.getTrackbarPos('a', windowName)
	b = cv2.getTrackbarPos('b', windowName)
	c = cv2.getTrackbarPos('c', windowName)

	g_lb = np.array([a, b, 50], np.uint8)
	g_ub = np.array([c, 255, 255], np.uint8)

	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Create a green mask (use: inRange())
	green_mask = cv2.inRange(img_hsv, g_lb, g_ub)
	# Segment the lakes (use bitwise_and())
	green_seg = cv2.bitwise_and(img, img, mask=green_mask)
	cv2.imshow('SOme', img)

	cv2.imshow(windowName, green_seg)
	key = cv2.waitKey(1)
	if key == ord('q'):
		break