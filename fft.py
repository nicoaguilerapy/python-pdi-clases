#-------IMPORTAR NUMPY & OpenCV--------
import matplotlib.pyplot as plt
import numpy as np
import cv2
import histograma as hg
#---LEER IMAGEN ----------
#ESPECIFICAR RUTA DONDE ESTA LA IMAGEN SI NO ESTA EN EL MISMO NIVEL DE DIRECTORIO

imagen=cv2.imread('imgs/rices.png')
img = cv2.imread('imgs/rices.png',0)

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

# FILTRO
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

#-----ESCALAMIENTO DE LA IMAGEN 
imagen2=cv2.resize(dst,(Nc,Nf))
#CONVERSIÓN A ESCALA DE GRISES uint8
# i_gray2=cv2.cvtColor(imagen2,cv2.COLOR_RGB2GRAY)
#CONVERSIÓN A PUNTO FLOTANTE PARA REALIZAR OPERACIONES MATEMATICAS
i_grayd2=np.float64(imagen2) 
#TRANSFORMADA DE FOURIER EN 2D
Fuv2=np.fft.fft2(i_grayd2)
Fuv2=np.fft.fftshift(Fuv2)
#OBTENER LA MAGNITUD DE LA TRANSFORMADA DE FOURIER DE LA IMAGEN 
Fuv_abs2=np.abs(Fuv2)
#ESPECTRO EN ESCALA LOGARITMICA
Fuv_log2=20*np.log10(Fuv_abs2)
#MOSTRAR IMAGEN EN ESCALA GRISES Y SU ESPECTRO DE FRECUENCIA
# cv2.imshow("IMAGEN ORIGINAL",i_gray)
# cv2.imshow("ESPECTRO DE FOURIER",np.uint8(255*Fuv_log/np.max(Fuv_log)))



plt.subplot(231),plt.imshow(i_gray),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(np.uint8(255*Fuv_log/np.max(Fuv_log))),plt.title('Transformada')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.plot(hg.getHistogram(i_gray)),plt.title('histograma')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(imagen2),plt.title('blur')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(np.uint8(255*Fuv_log2/np.max(Fuv_log2))),plt.title('Transformada')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.plot(hg.getHistogram(imagen2)),plt.title('histograma')
plt.xticks([]), plt.yticks([])
plt.show()



# #DISEÑO DEL FILTRO PASA ALTO IDEAL
# #---------------------------------------------------------------------
# F1=np.arange(-Nf/2+1,Nf/2+1,1)
# F2=np.arange(-Nc/2+1,Nc/2+1,1)
# [X,Y]=np.meshgrid(F1,F2)
# D=np.sqrt(X**2+Y**2)
# D=D/np.max(D)
# #DEFINIR RADIO DE CORTE
# Do=0.59
# #Creación del Filtro Ideal en 2D
# Huv=np.zeros((Nf,Nc))
# #PRIMERO CREAR EL FILTRO PASA BAJO IDEAL
# for i in range(Nf):
#     for j in range(Nc):
#         if(D[i,j]<Do):
#             Huv[i,j]=1
# #CONVERTIR A PASA ALTO IDEAL
# Huv=1-Huv
# #----------------------------------------------------
# cv2.imshow("FILTRO 2D PASA ALTO IDEAL",np.uint8(255*Huv))
# #--------------------------FILTRADO EN FRECUENCIA
# #-MULTIPLICACIÓN ELEMENTO A ELEMENTO EN EL DOMINIO DE LA FRECUENCIA
# Guv=Huv*Fuv
# #MAGNITUD
# Guv_abs=np.abs(Guv)
# Guv_abs=np.uint8(255*Guv_abs/np.max(Guv_abs))
# cv2.imshow('ESPECTRO DE FRECUENCIA G',Guv_abs)
# #---TRANSFORMADA INVERSA PARA OBTENER LA SEÑAL FILTRADA 
# #IFFT2
# gxy=np.fft.ifft2(Guv)
# gxy=np.abs(gxy)
# gxy=np.uint8(gxy)
# #--MOSTRAR LA IMAGEN FILTRADA
# cv2.imshow('IMAGEN FILTRADA',gxy)

cv2.waitKey(0)
cv2.destroyAllWindows()