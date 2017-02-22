import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def boxFilter(ksize):
    maskSize = 2 * ksize + 1    
    mat = np.ones((maskSize,maskSize)) / (float)(maskSize * maskSize) 
    return mat

def GaussianFilter(sigma):
    halfSize = 3 * sigma
    maskSize = 2 * halfSize + 1 
    mat = np.ones((maskSize,maskSize)) / (float)( 2 * np.pi * (sigma**2))
    xyRange = np.arange(-halfSize, halfSize+1)
    xx, yy = np.meshgrid(xyRange, xyRange)    
    x2y2 = (xx**2 + yy**2)    
    exp_part = np.exp(-(x2y2/(2.0*(sigma**2))))
    mat = mat * exp_part
    
    # plotting this function
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(xx, yy, mat, rstride=1, cstride=1, cmap='hot')
    plt.show()   

    return mat

img1 = cv2.imread('Ex9/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Ex9/Lenna_noise.jpg', cv2.IMREAD_GRAYSCALE)
box = boxFilter(3)  
img3 = cv2.filter2D(img2, -1, box)
gau = GaussianFilter(1)
img4 = cv2.filter2D(img2, -1, gau)
#Note: Both the box and gau masks have the size of [7*7]
 
nImg1 = cv2.Laplacian(img1, cv2.CV_64F)
nImg2 = cv2.Laplacian(img2, cv2.CV_64F)
nImg3 = cv2.Laplacian(img3, cv2.CV_64F)
nImg4 = cv2.Laplacian(img4, cv2.CV_64F)
#http://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=laplacian#laplacian
 
cv2.imshow('img 2', img2)
cv2.imshow('Laplacian 2', nImg2)
cv2.imshow('img 3', img3)
cv2.imshow('Laplacian 3', nImg3)
cv2.imshow('img 4', img4)
cv2.imshow('Laplacian 4', nImg4)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
