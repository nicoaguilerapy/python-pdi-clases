import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/onerice.png')

cv2.imshow('one rice', img)
#cv2.waitKey(0)
def howIs(img):
    print(img.shape)
#valor maximo dentro de una matriz
    print(np.max(img))
#valor minimo dentro de una matriz
    print(np.min(img))

howIs(img)

X = img[:,:,0]

howIs(X)
#segmentacion
def seg(X, t):
    area = 0
    (N,M)=X.shape
    #salida otra imagen 
    Y = np.zeros((N,M))
    #recorrer la matriz 
    for i in range(N):
        for j in range(M):
            if X [i,j]>t:
                area += 1
                Y [i,j] = 255
    
    print('Area = ', area)
    return Y

Y = seg(X, 170)
cv2.imshow('Img segmentada', Y)
#cv2.waitKey(0)

#grafico de un histograma, degradacion de pixeles 
#Definiciones 

#HISTOGRAMA:
#cantidad y valor del pixel 





