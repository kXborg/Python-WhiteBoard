import cv2
import numpy as np

def fn(x):
	pass

windowName ="Window" 
# window name
cv2.namedWindow(windowName) 
   
# there trackbars which have the name
# of trackbars min and max value 
cv2.createTrackbar('blue_l', windowName, 0, 255, fn)
cv2.createTrackbar('blue_u', windowName, 255, 255, fn)
cv2.createTrackbar('green_l', windowName, 50, 255, fn)
cv2.createTrackbar('green_u', windowName, 100, 255, fn)
cv2.createTrackbar('red_l', windowName, 0, 255, fn)
cv2.createTrackbar('red_u', windowName, 255, 255, fn)

img = cv2.imread('apples.jpg')
img = cv2.resize(img, None, fx=0.2, fy=0.2)

while True:
	
	a = cv2.getTrackbarPos('blue_l', windowName)
	b = cv2.getTrackbarPos('blue_u', windowName)
	c = cv2.getTrackbarPos('green_l', windowName)
	d = cv2.getTrackbarPos('green_u', windowName)
	e = cv2.getTrackbarPos('red_l', windowName)
	f = cv2.getTrackbarPos('red_u', windowName)

	color_lb = np.array([a, 50, c], np.uint8)
	color_ub = np.array([255, 100, 255], np.uint8)

	# Create a green mask (use: inRange())
	green_mask = cv2.inRange(img, color_lb, color_ub)
	# Segment the lakes (use bitwise_and())
	green_seg = cv2.bitwise_and(img, img, mask=green_mask)
	cv2.imshow('Original', img)

	cv2.imshow(windowName, green_seg)
	key = cv2.waitKey(1)
	if key == ord('q'):
		break