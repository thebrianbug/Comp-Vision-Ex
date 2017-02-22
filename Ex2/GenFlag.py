# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 17:01:05 2017

@author: xinli
"""

import cv2
import numpy as np

img = np.zeros((400, 600, 3), np.uint8)

#Note: for OpenCV, the three color channels should follow the order of B,G,R
img[:,0:200,:]=(164, 85, 0)
img[:,200:400,:]=(255, 255, 255)
img[:,400:600,:]=(53, 65, 239)

cv2.imshow('Flag of France', img)
cv2.waitKey(0)

cv2.destroyAllWindows()




