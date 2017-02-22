import cv2

refPt = []
SelectROI = 0
ROI_IMAGE = []

def mouseFunc(event, x, y, flags, param):
    #grab references to the global variables
    global refPt, SelectROI    
    if event == cv2.EVENT_LBUTTONDOWN and SelectROI == 1:
        print 'Pick the left top point'
        refPt = [(x,y)]
        SelectROI = 2
    elif event == cv2.EVENT_LBUTTONUP and SelectROI == 2:
        print 'Pick the right bottom point'
        refPt.append((x,y))
        SelectROI = 3
        ROI_IMAGE = imgClone[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
        cv2.imshow('ROI', ROI_IMAGE)

        
##########################################################
       
##########################################################
        
imgName = 'PickROI/Lenna.png'
img=cv2.imread(imgName)
imgClone = img.copy()
cv2.imshow(imgName, imgClone)
cv2.setMouseCallback(imgName, mouseFunc)
SelectROI = 1

while SelectROI != 3:
    cv2.waitKey(0)

cv2.destroyAllWindows()
