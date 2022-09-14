import brillo as br
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import histograma as hg

img = cv.imread('imgs/lung_cancer.jpg')
img0=cv.resize(img,(200,200))
img_gray = cv.cvtColor(img0,cv.COLOR_RGB2GRAY)
img = img[:,:,0]

# Primero ajustamos el contraste, luego aplicamos un suavizado gaussiano
img1 = br.getContrAuto(img)
img2 = cv.GaussianBlur(img1, (5,5), 0)
canny = cv.Canny(img1.copy(), 50, 195)
(contornos,_) = cv.findContours(canny.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)




#Las funciones son muy claras, luego de cada procesamiento, miramos la distribucion para determinar 
# el threshold, en el autocontraste genera mejores resultados que el que paso por un filtro blur
# en ambos casos con el mismo treshold, logramos resultados diferentes, teniendo en cuenta que es de uso medico
# el blur puede quitar informacion que puede ser relevante.


plt.subplot(331),plt.imshow(img0, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(334),plt.plot(hg.getHistogram(img_gray)),plt.title('HG Original')
plt.xticks([]), plt.yticks([])
plt.subplot(332),plt.imshow(img1, cmap='gray'),plt.title('AutoContraste')
plt.xticks([]), plt.yticks([])
plt.subplot(335),plt.plot(hg.getHistogram(img1)),plt.title('HG AutoContraste')
plt.xticks([]), plt.yticks([])
plt.subplot(333),plt.imshow(img2, cmap='gray'),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(336),plt.plot(hg.getHistogram(img2)),plt.title('HG Suavizado')
plt.xticks([]), plt.yticks([])
plt.subplot(337),plt.imshow(cv.Canny(img0.copy(), 50, 145), cmap='gray'),plt.title('Contorno Original')
plt.xticks([]), plt.yticks([])
plt.subplot(338),plt.imshow(cv.Canny(img1.copy(), 50, 195), cmap='gray'),plt.title('Contorno AutoContraste')
plt.xticks([]), plt.yticks([])
plt.subplot(339),plt.imshow(cv.Canny(img2.copy(), 50, 194), cmap='gray'),plt.title('Contorno Suavizado')
plt.xticks([]), plt.yticks([])
plt.show()

#a ojo humano aparentemente tendria mejor resultado con el autocontraste.
#se podrian aplicar multitrheshold para determinar varios niveles de interes.

plt.imshow(cv.drawContours(img1.copy(),contornos,-1,(0,0,255), 2), cmap='gray'),plt.title('Resultado Final')
plt.show()