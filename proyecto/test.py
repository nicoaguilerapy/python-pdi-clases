import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

img = cv2.imread('image4.jpg')
img = img[:,:,0]
cv2.imshow('Original', img)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Blanco y negro', gray)
cv2.waitKey(0)