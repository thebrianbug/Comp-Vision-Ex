import cv2
import numpy as np

def boxFilter(ksize):
    maskSize = 2 * ksize + 1    
    mat = np.ones((maskSize,maskSize)) / (float)(maskSize * maskSize) 
    return mat

img1 = cv2.imread('Ex8/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Ex8/Lenna_noise.jpg', cv2.IMREAD_GRAYSCALE)
box3 = boxFilter(1)
img3 = cv2.filter2D(img2, -1, box3)

nImg1 = cv2.Laplacian(img1, cv2.CV_64F)
nImg2 = cv2.Laplacian(img2, cv2.CV_64F)
nImg3 = cv2.Laplacian(img3, cv2.CV_64F)
#http://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=laplacian#laplacian

cv2.imshow('img 1', img1)
cv2.imshow('Laplacian 1', nImg1)
cv2.imshow('img 2', img2)
cv2.imshow('Laplacian 2', nImg2)
cv2.imshow('img 3', img3)
cv2.imshow('Laplacian 3', nImg3)


cv2.waitKey(0)
cv2.destroyAllWindows()

