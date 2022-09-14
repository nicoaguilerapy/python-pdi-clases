from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

def getHistogram(X):
  result = np.zeros((256))
  (N,M)=X.shape
  for i in range(N):
      for j in range(M):
        try:
          result[X[i,j]] += 1
        except:
          result[X[i]] += 1
  
  arr = np.sort(result)[::-1]
  for i in range(3):
      print("{}: {}".format(i, arr[i]))

  return result
             

# # img = cv2.imread('imgs/lung_cancer.jpg')
# # img = img[:,:,0]

# # cv2.imshow('Original', img)
# # r = getHistogram(img)

# # plt.plot(r)
# # plt.show()
# # cv2.waitKey(0)



