import fft 
import matplotlib.pyplot as plt
import numpy as np
import cv2

def toShow(float_n):
    return np.uint8(255*float_n/np.max(float_n))

def getPasabajaIdeal(PATH):
    imagen=cv2.imread(PATH, 0)
    img = imagen[:,:,0]

    X = fft.getFFF(PATH)

    (M,N) = img.shape
    Y = X.copy()
    for i in range(N):
        for j in range(M):
            Y[i,j] = ((i-(M/2))^2/(i-(N/2))^2)^(-1/2)

    return Y

plt.imshow(toShow(getPasabajaIdeal('imgs/onerice.png'))),plt.title('Transformada')
plt.show()



