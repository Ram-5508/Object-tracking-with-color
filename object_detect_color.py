# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:26:03 2019

@author: Lenovo
"""

import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture('color.mp4')
cv2.namedWindow('Trackbar')

cv2.createTrackbar('l-H','Trackbar',0,50,nothing)
cv2.createTrackbar('l-S','Trackbar',0,150,nothing)
cv2.createTrackbar('l-V','Trackbar',0,150,nothing)
cv2.createTrackbar('h-H','Trackbar',0,70,nothing)
cv2.createTrackbar('h-S','Trackbar',0,255,nothing)
cv2.createTrackbar('h-V','Trackbar',0,255,nothing)

while 1:
    ret,img=cap.read()
    
    if ret is not True:
        cap=cv2.VideoCapture('color.mp4')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    l_H=cv2.getTrackbarPos('l-H','Trackbar')
    l_S=cv2.getTrackbarPos('l-S','Trackbar')
    l_V=cv2.getTrackbarPos('l-V','Trackbar')
    h_H=cv2.getTrackbarPos('h-H','Trackbar')
    h_S=cv2.getTrackbarPos('h-S','Trackbar')
    h_V=cv2.getTrackbarPos('h-V','Trackbar')
    
    mask=cv2.inRange(hsv,np.array([l_H,l_S,l_V]),np.array([h_H,h_S,h_V]))
    
    object_img=cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow('Img',img)
    cv2.imshow('mask',object_img)
    k=cv2.waitKey(100) & 0xff
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()