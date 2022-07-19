import numpy as np 
import cv2
import matplotlib.pyplot as plt
import histograma as hg
def segmentacion(X, t):
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

def histograma(X):
    result = np.zeros((256))
    area = 0
    (N,M)=X.shape

    for i in range(N):
        for j in range(M):
            res = int(X[i,j])
            result[res] += 1
    
    return result

def minimo(X):
    (N,M)=X.shape
    for i in range(N):
        xmin = np.min(X[i,:])
        X[i,:] = X[i,:] - xmin
    
    return X

img = cv2.imread('rices.png')

cv2.imshow('one rice', img)
#cv2.waitKey(0)
def howIs(img):
    print(img.shape)
#valor maximo dentro de una matriz
    print(np.max(img))
#valor minimo dentro de una matriz
    print(np.min(img))

howIs(img)

img = img[:,:,0]

howIs(img)


new_img = minimo(img)
cv2.imshow('Img segmentada', new_img)
new_img2 = segmentacion(new_img, 65)
cv2.imshow('Img segmentada', new_img2)
result2 = histograma(new_img2)
plt.plot(result2)
plt.show()
cv2.waitKey(0)






