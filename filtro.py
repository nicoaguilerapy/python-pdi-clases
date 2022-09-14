import numpy as np 
import cv2
import matplotlib.pyplot as plt

def getFiltro(X, fil):
    (N,M)=X.shape
    Y = X.copy()
    
    for i in range(N-1):
        for j in range(M-1):
            Y[i,j] = (X[i, j]*fil[1, 1] + X[i+1, j]*fil[2, 1] + X[i, j+1]*fil[1, 2] 
            + X[i+1, j+1]*fil[2, 2]+ X[i, j-1]*fil[1, 0] + X[i-1, j]*fil[0, 1] 
            + X[i-1, j-1]*fil[0, 0] + X[i+1, j-1]*fil[2, 0] + X[i-1, j+1]*fil[0, 2] )
            
    return Y

filtro = np.array([ (1,1,1),
                    (1,1,1),
                    (1,1,1)])/9

img = cv2.imread('imgs/onerice.png')
img = img[:,:,0]


cv2.imshow('Rices', img)
copia = getFiltro(img.copy(), filtro)
cv2.imshow('Img CONFILTRO', copia)
cv2.waitKey(0)






