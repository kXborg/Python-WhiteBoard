import cv2 

img = cv2.imread('pyOpenAnnotate-feature-image.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img_gray, (5,5), cv2.BORDER_DEFAULT)
canny = cv2.Canny(blur, 50, 150)

cv2.imshow('Edges', cv2.resize(canny, None, fx=0.4, fy=0.4))
cv2.imwrite('liz.jpg', canny)
cv2.waitKey(0)