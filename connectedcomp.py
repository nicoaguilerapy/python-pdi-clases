import cv2
import numpy as np
import re


def validator(texto):
  val = filter(lambda x : re.match(r'\D{3}\d{3}',x),texto)
  print(val)

 
# Loading the image
img = cv2.imread('imgs/placa2.jpg')
 
# preprocess the image
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
 
# Applying 7x7 Gaussian Blur
blurred = cv2.GaussianBlur(gray_img, (7, 7), 0)
 
# Applying threshold
threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
 
# Apply the Component analysis function
analysis = cv2.connectedComponentsWithStats(threshold,
                                            4,
                                            cv2.CV_32S)
(totalLabels, label_ids, values, centroid) = analysis
 
# Initialize a new image to store
# all the output components
output = np.zeros(gray_img.shape, dtype="uint8")
 
# Loop through each component
for i in range(1, totalLabels):
   
      # Area of the component
    area = values[i, cv2.CC_STAT_AREA]
    
     
    if (area > 60) and (area < 250):
        print(area)
        componentMask = (label_ids == i).astype("uint8") * 255
        output = cv2.bitwise_or(output, componentMask)


cv2.imshow("Image", img)
cv2.imshow("Filtered Components", output)
cv2.waitKey(0)

import easyocr as eocr
reader = eocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext(output)

print(result[0][1])
print(result[0][1].upper().replace(" ", ""))

validator(result[0][1].upper().replace(" ", ""))