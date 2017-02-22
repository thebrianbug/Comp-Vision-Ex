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

#this function normalize a grayscale image into a 'uint8' type image with the range of [new_min, new_max]
def my_normalize(img, new_min, new_max):
    n_row = img.shape[0]
    n_col = img.shape[1]
    val_max= np.amax(img)
    val_min = np.amin(img)    
    nImg = np.zeros((n_row, n_col), np.uint8)
    for i in range(n_row):
        for j in range(n_col):
            nvalue = (img.item(i,j) - val_min) / (val_max - val_min)
            nvalue = np.uint((nvalue * (new_max - new_min)) + new_min)
            nImg.itemset((i,j), nvalue) 
    return nImg
               

imgName = 'Ex10/cameraman.png'
img1 = cv2.imread(imgName)
imgGray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow(imgName, imgGray)
img_n = cv2.normalize(imgGray.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
gx, gy = my_grad(img_n)

gx_n = cv2.normalize(gx.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
gy_n = cv2.normalize(gy.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

mag_g = np.sqrt(gx**2 + gy**2)
mag_g_n = my_normalize(mag_g, 0, 255)

cv2.imshow('grad_x', gx_n)
cv2.imshow('grad_y', gy_n)
cv2.imshow('gradient magnitude', mag_g_n)

threshold = 50  #try other threshold values here

ret,imgOut = cv2.threshold(mag_g_n, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow('binary output', imgOut)


cv2.waitKey(0)
cv2.destroyAllWindows()








