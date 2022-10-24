#-------IMPORTAR NUMPY & OpenCV--------
import matplotlib.pyplot as plt
import numpy as np
import cv2
import histograma as hg
#---LEER IMAGEN ----------
#ESPECIFICAR RUTA DONDE ESTA LA IMAGEN SI NO ESTA EN EL MISMO NIVEL DE DIRECTORIO

def getFFF(PATH):

    imagen=cv2.imread(PATH)
    
    X = imagen[:,:,0]
    Nf=512
    Nc=512
    #-----ESCALAMIENTO DE LA IMAGEN 
    imagen=cv2.resize(imagen,(Nc,Nf))
    #CONVERSIÓN A ESCALA DE GRISES uint8
    i_gray=cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
    #CONVERSIÓN A PUNTO FLOTANTE PARA REALIZAR OPERACIONES MATEMATICAS
    i_grayd=np.float64(i_gray) 
    #TRANSFORMADA DE FOURIER EN 2D
    Fuv=np.fft.fft2(i_grayd)
    Fuv=np.fft.fftshift(Fuv)
    #OBTENER LA MAGNITUD DE LA TRANSFORMADA DE FOURIER DE LA IMAGEN 
    Fuv_abs=np.abs(Fuv)
    #ESPECTRO EN ESCALA LOGARITMICA
    Fuv_log=20*np.log10(Fuv_abs)

    return Fuv_log



# plt.subplot(231),plt.imshow(i_gray),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(232),plt.imshow(np.uint8(255*Fuv_log/np.max(Fuv_log))),plt.title('Transformada')
# plt.xticks([]), plt.yticks([])
# plt.subplot(233),plt.plot(hg.getHistogram(i_gray)),plt.title('histograma')
# plt.xticks([]), plt.yticks([])
# plt.subplot(234),plt.imshow(imagen2),plt.title('blur')
# plt.xticks([]), plt.yticks([])
# plt.subplot(235),plt.imshow(np.uint8(255*Fuv_log2/np.max(Fuv_log2))),plt.title('Transformada')
# plt.xticks([]), plt.yticks([])
# plt.subplot(236),plt.plot(hg.getHistogram(imagen2)),plt.title('histograma')
# plt.xticks([]), plt.yticks([])
# plt.show()