import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('imgs/onerice.png')
kernel1 =np.array([  (0,0,-1,0,0),
                     (0,-1,-2,-1,0),
                     (-1,-2,16,-1,-2),
                     (0,-1,-2,-1,0),
                     (0,0,-1,0,0),
                     ])/16

dst = cv.filter2D(img,-1,kernel1)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging2')
plt.xticks([]), plt.yticks([])
plt.show()