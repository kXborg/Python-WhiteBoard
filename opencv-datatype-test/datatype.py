
import cv2
import numpy as np 

a = np.array([254], dtype=np.uint8)
b = np.array([2], dtype=np.uint8)

c = a + b
print('Numpy Sum', c)

d = cv2.add(a, b)
print('OpenCV Sum', d)

e = a*b
print('Numpy Mul', e)

f = cv2.multiply(a,b)
print('OpenCV Mul', f)