import numpy as np 
import cv2
import matplotlib.pyplot as plt

def getBordes(X):
    (N,M)=X.shape
    Y = X.copy()
    for i in range(0, N-1):
        for j in range(0, M-1):
            pix = X[i+1,j] - X[i,j]
            if pix > 0:
                Y[i,j] = pix
            else:
                Y[i,j] = 0

    return Y


img = cv2.imread('rices.png')
img = img[:,:,0]
img2 = getBordes(img.copy())




plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img2),plt.title('Bordes')
plt.xticks([]), plt.yticks([])
plt.show()