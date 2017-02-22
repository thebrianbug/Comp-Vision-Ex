import cv2
import numpy as np

# Convert the image into the range of [0.0, 1.0]
def img_normalize(img):
    min_val = np.min(img.ravel())
    max_val = np.max(img.ravel())
    output = (img.astype('float')-min_val)/(max_val - min_val)
    return output

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
            
        

img = cv2.imread('Ex6/LSU_logo.png', cv2.IMREAD_GRAYSCALE)


img_float = img_normalize(img)
# You can also use cv2.normalize:
#img_float = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)


print img_float.shape

gx, gy = my_grad(img_float)

print gx.shape
print gy.shape


img_gx = img_normalize(gx)
img_gy = img_normalize(gy)
#img_gx = cv2.normalize(gx.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
#img_gy = cv2.normalize(gy.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

cv2.imshow('img', img_float)
cv2.imshow('gradient x', img_gx)
cv2.imshow('gradient y', img_gy)

cv2.waitKey(0)
cv2.destroyAllWindows()

