import cv2

#imgname = raw_input('image name')
imgname = 'Ex1/opencv_logo.png'
img = cv2.imread(imgname)

cv2.imshow(imgname, img)

while True:
    key = cv2.waitKey(0)
    print key
    if key == 27: # wait for ESC key to exit 
        cv2.destroyAllWindows() 
        break
    elif key == (112): # wait for 'p' key to partition into 3 channels
        row, col, channels = img.shape
        if channels == 3:
            print 'this is a color image'
            bImg,gImg,rImg = cv2.split(img)
            #you can also do 
            #bImg = img[:,:,0]
            #gImg = img[:,:,1]
            #rImg = img[:,:,2]            
        else:
            print 'this is a grayscale image'
            bImg,gImg,rImg = img
        cv2.imshow('rChannel', rImg)
        cv2.imshow('gChannel', gImg)
        cv2.imshow('bChannel', bImg)            
    elif key == (115): # wait for 's' key to save   
        cv2.imwrite('rChannel.png',rImg)
        cv2.imwrite('gChannel.png',gImg) 
        cv2.imwrite('bChannel.png',bImg)
        print 'three images saved'
        
    
        
    
