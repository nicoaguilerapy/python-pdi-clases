from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def getHistogram(path):
  img = Image.open(path)
  result = np.zeros((256))

  for y in range(img.height):
    for x in range(img.width):
      pixel = img.getpixel((x, y))
      try:
        result[pixel] += 1
      except:
        result[pixel[0]] += 1

  arr = np.sort(result)[::-1]
  for i in range(3):
      print("{}: {}".format(i, arr[i]))

  plt.plot(result)
  plt.show()




