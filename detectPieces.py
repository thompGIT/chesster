#!/usr/bin/python

'''
This module should detect chess pieces on a standard chess board.
'''

import cv2
import numpy as np
import sys

print __doc__
try:
	fn = sys.argv[1]
except:
	fn = "images/chess.02.jpg"

def nothing(*arg):
    pass
        
src = cv2.imread(fn, 1)
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 5)
cimg = src.copy() # numpy function
cimgOrig = cimg

cv2.namedWindow('PieceFinder')
cv2.createTrackbar('dp',     'PieceFinder', 0, 10, nothing)
cv2.setTrackbarPos('dp',     'PieceFinder', 5)
cv2.createTrackbar('param1', 'PieceFinder', 0, 100, nothing)
cv2.setTrackbarPos('param1', 'PieceFinder', 50)

while True:
    dp     = cv2.getTrackbarPos('dp', 'PieceFinder') / 10.0
    param1 = cv2.getTrackbarPos('param1', 'PieceFinder')
            
    print dp
            
    circles = cv2.HoughCircles(img,                 # input image (grayscale)
                               cv2.HOUGH_GRADIENT,  # detection method (HOUGH_GRADIENT is only available option)
#                               0.5,                 # dp - inverse ration of accumulator resolution
                               dp,                  # dp - inverse ration of accumulator resolution
                               60,                  # minDist - minimum distance between centers
                               np.array([]),        # circles - output vector of detected circles
#                               50,                  # param1 - higher threshold of Canny() edge detector
                               param1,              # param1 - higher threshold of Canny() edge detector
                               17,                  # param2 - accumulator threshold; smaller => more false positives 
                               15,                  # minRadius - min circle radius
                               30)                  # maxRadius - max circle radius

    a, b, c = circles.shape
    for i in range(b):
        cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
        cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv2.LINE_AA) # draw center of circle
        
    cv2.imshow("PieceFinder", cimg)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

cv2.destroyAllWindows()

