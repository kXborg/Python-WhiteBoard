import threading
import cv2 

def func_a():
	img = cv2.imread('panda.jpg')
	while True:
		cv2.imshow('Window 1', img)
		key = cv2.waitKey(1)
		if key == ord('q'):
			break 


def func_b():
	img = cv2.imread('tab.png')
	while True:
		cv2.imshow('Window 2', img)
		key = cv2.waitKey(1)
		if key == ord('q'):
			break 


if __name__ == '__main__':
	thread1 = threading.Thread(target=func_a)
	thread2 = threading.Thread(target=func_b)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()