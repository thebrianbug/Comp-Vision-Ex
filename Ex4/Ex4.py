
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('Ex4/MountStream.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])      
    hist = np.zeros(256, np.int)  # an int array of 256 elements 
    for j in xrange(0,img.shape[0]):
        for k in xrange(0,img.shape[1]):
            pVal = img[j,k,i]
            hist[pVal] += 1
    plt.subplot(221), plt.plot(hist, color = col)        
    plt.xlim([0,256])    
    plt.subplot(222), plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
