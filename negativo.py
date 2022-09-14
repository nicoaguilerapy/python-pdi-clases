import numpy as np 
import cv2
import matplotlib.pyplot as plt


def getNegativo(X):
    (N,M)=X.shape
    for i in range(N):
        xmin = np.min(X[i,:])
        X[i,:] = 255 - X[i,:]
    
    return X


img = cv2.imread('imgs/bio_low_contrast.jpg')
img = img[:,:,0]



cv2.imshow('Rices', img)
Y = getNegativo(img)
cv2.imshow('Img segmentada', Y)
cv2.waitKey(0)






