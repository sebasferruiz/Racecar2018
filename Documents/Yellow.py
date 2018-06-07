#!/usr/bin/python

import cv2
import numpy as np

def filter_region(image, vertices):
    mask = np.zeros_like(image)
    if len(mask.shape) == 2:
        cv2.fillPoly(mask, vertices, 255)
    else:
        cv2.fillPoly(mask, vertices, (255,)*mask.shape[2])
    return cv2.bitwise_and(image, mask)

kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
ret,frame = cap.read()
rows, cols = frame.shape[:2]

bottom_left = [cols*.1, rows]
top_left = [cols*0.4, rows*0.6]
bottom_right = [cols*0.9, rows]
top_right = [cols*0.6, rows*0.6]
vertices = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype = np.int32)

while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(filter_region(frame, vertices) , cv2.COLOR_BGR2HSV)
    ymn = np.array([20,100,100])
    ymx = np.array([50,255,255])
    

    mask = cv2.inRange(hsv, ymn, ymx)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('res', res)
    cv2.imshow('mask', mask)

    threshold = []
    for i in range(479):
        if mask[i][240] != 0:
            threshold.append(255)
        else:
            threshold.append(0)
    print(threshold)

    

    edge = cv2.Canny(mask, 50, 150, apertureSize= 3)
    cv2.imshow('edges', edge)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edge,1,np.pi/180,100,minLineLength,maxLineGap)
    if lines is not None:
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(res,(x1,y1),(x2,y2),(0,255,0),2)

        cv2.imshow('houghlines2',res)
   
    a = cv2.waitKey(5) 
    if a == 20:
        break
cv2.destroyAllWindows()
cap.release()
