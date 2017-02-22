import cv2

img = cv2.imread('Ex1/Lenna.png')
cv2.imshow('FRAME', img)
cv2.waitKey(0)
cv2.destroyAllWindows()