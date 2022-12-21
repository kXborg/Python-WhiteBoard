import cv2

def dummyFunc(x):
    pass


# Load gray scale image.
image = cv2.imread('kukil-profile.jpg', 0)

cv2.namedWindow("Trackbar")
cv2.createTrackbar("T", "Trackbar", 0, 255, dummyFunc)


while True:
    img = image.copy()
    threshold = cv2.getTrackbarPos("T", "Trackbar")
    ret, thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow("Trackbar", thresh)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
        cv2.destroyAllWindows()