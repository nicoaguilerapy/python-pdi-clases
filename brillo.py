import matplotlib.pyplot as plt
import numpy as np 
import cv2
import matplotlib.pyplot as plt
import histograma as hg


def getContraste(X, brillo):
    (N,M)=X.shape
    for i in range(N):
        for j in range(M):
            if X[i,j] * brillo > 255:
                X[i,j] = 255
            elif X[i,j] * brillo < 0:
                X[i,j] = 0
            else:
                X[i,j] = X[i,j] * brillo 

    return X

def getBrillo(X, brillo):
    (N,M)=X.shape
    for i in range(N):
        for j in range(M):
            if X[i,j] + brillo > 255:
                X[i,j] = 255
            elif X[i,j] + brillo < 0:
                X[i,j] = 0
            else:
                X[i,j] = X[i,j] + brillo 

    return X

def getContrAuto(X):
    min = np.min(X[:,:])
    max = np.max(X[:,:])
    Y = X.copy()
    print("Maximo: {}, Minimo: {}".format(max, min))
    (N,M)=X.shape
    Y[:,:] = (X[:,:] - min)*(255/(max-min))
    
    return Y


# img = cv2.imread('imgs/bio_low_contrast.jpg')
# img = img[:,:,0]


# cv2.imshow('Original', img)
# Y = getContrAuto(img)
# R = hg.getHistogram(img)
# plt.plot(R)
# plt.show()
# cv2.imshow('Contraste auto', Y)
# R = hg.getHistogram(Y)
# plt.plot(R)
# plt.show()
# cv2.waitKey(0)







