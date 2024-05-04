import cv2
import numpy as np

class MyDetectionMethods():
    def __init__(self):
        pass
    
    def detectionUsingThresholding(img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        GrayInvs=cv2.bitwise_not(gray)
        blurring=cv2.GaussianBlur(GrayInvs,(11,11),0)
        _,thres =cv2.threshold(blurring,120,255,cv2.THRESH_BINARY)# we can modify the thres value.
        
        contours,heriechy=cv2.findContours(thres,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        
        objectDetect=[]
        for cont in contours:
            area=cv2.contourArea(cont)
            if area> 1500 : # I get no result when I add if area> 15000 and area < 400000: 
                objectDetect.append(cont)
        return objectDetect
                
                
    def detectionUsingCanny(self,img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        GrayInvs=cv2.bitwise_not(gray)
        blurring=cv2.GaussianBlur(GrayInvs,(5,5),0)
        canny=cv2.Canny(blurring,120,180) # we can modify the lower and upper values.
        
        DilateKernel=np.ones((5,5), "uint8")
        dilation=cv2.dilate(canny,DilateKernel,iterations=1)
        contours,__=cv2.findContours(dilation,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('dilation',dilation)
        
        detectObject=[]
      
        
        for cont in contours:
            area=cv2.contourArea(cont)
            # if area> 4000:  # I get no result when I add if area> 15000 and area < 400000:  for exercise3
            #     detectObject.append(cont)
            if 2000>area > 1800:
                 detectObject.append(cont)
            if 3000 > area > 2000:
                 detectObject.append(cont)
        return detectObject
            
 
 
 
