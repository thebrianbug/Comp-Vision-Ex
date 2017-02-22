import cv2
import numpy as np


def boxFilter(ksize):
    maskSize = 2 * ksize + 1    
    mat = np.zeros((maskSize , maskSize))
    nElement = float(maskSize * maskSize)
    for i in range(maskSize):
        for j in range(maskSize):
            mat[i,j]= 1 / nElement
        
    # you can also simply use: 
    #mat = np.ones((maskSize,maskSize)) / (float)(maskSize * maskSize)    
    
    print mat
    return mat


img = cv2.imread('Ex7/LSU_logo.png', cv2.IMREAD_GRAYSCALE)
m1 = boxFilter(3)
nImg = cv2.filter2D(img, ddepth=-1, kernel=m1, borderType=cv2.BORDER_CONSTANT)

cv2.imshow('img', img)
cv2.imshow('filtered img', nImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

