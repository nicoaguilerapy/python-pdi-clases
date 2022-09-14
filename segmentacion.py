import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img6.jpg')
X = img[:,:,0]

def seg(X, t):
    area = 0
    (N,M)=X.shape
    Y = np.zeros((N,M))

    for i in range(N):
        for j in range(M):
            if X [i,j]>t:
                area += 1
                Y [i,j] = 255
    
    return Y

Y = seg(X, 140)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(Y),plt.title('Img segmentada')
plt.xticks([]), plt.yticks([])
plt.show()






