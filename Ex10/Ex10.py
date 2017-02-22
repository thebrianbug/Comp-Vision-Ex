import cv2
import numpy as np

# Computing gradient in both x and y directions
def my_grad(img):
    n_row = img.shape[0]
    n_col = img.shape[1]
    gx = np.zeros((n_row-2, n_col-2), float)
    gy = np.zeros((n_row-2, n_col-2), float)    
    for i in range(1, n_row-2):
        for j in range(1, n_col-2):
            gx[i,j]=(img[i,j+1]-img[i,j-1])/2.0
            gy[i,j]=(img[i+1,j]-img[i-1,j])/2.0
    return gx, gy    
           

img1 = cv2.imread('Ex10/cameraman.png', cv2.IMREAD_GRAYSCALE)

img1 = cv2.normalize(img1.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

gx, gy = my_grad(img1)

gx_n = cv2.normalize(gx.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
gy_n = cv2.normalize(gy.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

mag_g = np.sqrt(gx**2 + gy**2)
mag_g = cv2.normalize(mag_g.astype('float'), None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('grad_x', gx_n)
cv2.imshow('grad_y', gy_n)
cv2.imshow('gradient magnitude', mag_g)

ret,imgOut = cv2.threshold(mag_g, 127, 255, cv2.THRESH_BINARY)


cv2.waitKey(0)
cv2.destroyAllWindows()




