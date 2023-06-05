import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

Directorio = r'C:\Users\user\Desktop\Procesamiento de Imagenes\Grises.webp'
Img = cv2.imread(Directorio,0) 
[Fl, Cl] = Img.shape

print("Imagen inicial")
plt.imshow(Img,cmap='gray',vmin=0, vmax=255) 
plt.show()

Resultado=np.zeros((Fl,Cl))

Valor_Ajuste = int(input("Ingrese el valor con el que desea alterar la imagen, recuerde que valores altos dan tonos claros y valores cercanos al cero dan tonos oscuros: "))

print('')

for i in range(0, Fl, 1):
  for j in range(0, Cl, 1):
      Resultado[i,j]= Img[i,j] + Valor_Ajuste

      if Resultado[i,j]>255:
         Resultado[i,j]=255

      if Resultado[i,j]<0:
         Resultado[i,j]=0

Destino = r'C:\Users\user\Desktop\Procesamiento de Imagenes'
os.chdir(Destino)
cv2.imwrite('Grises1.webp', Resultado)


print("El resultado de alterar los valores es:")

plt.imshow(Resultado.astype('uint8'),cmap='gray',vmin=0, vmax=255) 
plt.show()