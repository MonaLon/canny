import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

img = cv.imread('what.PNG', 0)
fig = plt.figure()
minVal = 100
maxVal = 200

def on_trackbar(val):
	maxVal = val
	minVal = cv.getTrackbarPos(minTrackTitle, "Edge Detection")
	edges = cv.Canny(img, minVal, maxVal)
	cv.imshow('Edge Detection', edges)
def on_trackbarTwo(val):
	minVal = val
	maxVal = cv.getTrackbarPos(maxTrackTitle, "Edge Detection")
	edges = cv.Canny(img, minVal, maxVal)
	cv.imshow('Edge Detection', edges)

cv.namedWindow('Edge Detection')
maxTrackTitle = 'Max Threshold'
minTrackTitle = 'Min Threshold'
cv.createTrackbar(maxTrackTitle, 'Edge Detection', 0, 500, on_trackbar)
cv.createTrackbar(minTrackTitle, 'Edge Detection', 0, 500, on_trackbarTwo)

on_trackbar(maxVal)
on_trackbarTwo(minVal)

cv.waitKey()
