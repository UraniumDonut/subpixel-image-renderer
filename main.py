import cv2
import numpy as np
import time
from math import *

image = cv2.imread('image.png')
black = np.zeros((512,512,3), np.uint8)

cv2.namedWindow("Display", cv2.WINDOW_NORMAL) 
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (0,10)
fontScale              = 0.5
fontColor              = (0,0,255)
thickness              = 1
lineType               = 2

cv2.putText(black,'Resize window to fit!', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)

cv2.imshow('Display', black)



cv2.waitKey(0)
size = cv2.getWindowImageRect('Display')
height = size[3]
width = size[2]
resized = cv2.resize(image, (width, height))
subpixel = np.zeros((height,width*3,3), np.uint8)
new = np.zeros((height,width,3), np.uint8)


for i in range(0, image.shape[0]):
    print("Percentage: ", i/image.shape[0]*100)
    for j in range(0, image.shape[1]):
        s_i = floor(i * height / image.shape[0])
        s_j = floor(j * width*3 / image.shape[1])
        subpixel[s_i,s_j] = image[i,j]

for i in range(0, new.shape[0]):
    print("Percentage: ", i/new.shape[0]*100)
    for j in range(0, new.shape[1]):
        R = subpixel[i,j*3][2]
        G = subpixel[i,j*3+1][1]
        B = subpixel[i,j*3+2][0]
        new[i,j] = [B,G,R]




cv2.putText(resized,'Regular scaling', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)


cv2.putText(new,'Subpixel optimized scaling', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)





while(1):
    k = cv2.waitKey(0)
    if k == 9 or k == 27 or k == 108:
        break
    elif k == 32:
        cv2.imshow('Display', resized)
    elif k == 13:
        cv2.imshow('Display', new) 
    else:
        print("Key: " + str(k))

cv2.destroyAllWindows()