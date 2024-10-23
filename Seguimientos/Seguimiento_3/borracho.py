
import random

import matplotlib.pyplot as plt

import numpy as np

X = []  # almacena coordenadas del borracho en x.

Y = []  # almacena coordenadas del borracho en y.


## inicializo posiciones x,y en el origen de coordenadas cartesiano.



# establezco movimiento del borracho.

## inicializo posiciones x,y en el origen de coordenadas cartesiano.
Ax=[]  ## almacena aciertos en x y y.

Ay=[]

for k in range(10000):  # realiza el experimento 10 mil veces.

  x=0  # inicializa coord origen.
  y=0

  for i in range(10):  # se tomarán 10 pasos desde la pos inicial.

   

    s = random.randint(1,4)  ## selector ( toma valores entre 1 y 4 aleatoriamente)

    ## 1 corresponde hacia la izquierda, 
    # 2 mov hacia arriba.
    # 3 mov hacia izquierda.
    #   4 mov hacia abajo.


    if s==1 :           

        x = x + 1
        y = y + 0

    if s==2:

        x = x + 0
        y = y + 1

    if s==3:

        x = x -1
        y = y +0

    if s==4:

        x = x + 0
        y = y - 1

  cf = (x,y)  # coordenada final

  #print(cf) 

  # coordenadas de puntos posibles ubicados a 2 pasos del origen.

  if cf== (2,0) or cf ==(1,1) or cf ==(0,2) or cf==(-1,1) or cf ==(-2,0) or cf == (-1,-1) or cf==(0,-2):

    Ax.append(x)  ## acierto en x.
    Ay.append(y)  ## acierto coordenada y.

    

#print(Ax,Ay)

len(Ax)   ## contabiliza el número de veces que el borracho terminó a 2 pasos.
len(Ay)


prob = (len(Ax)/10000 )*100

print( " La probabilidad aproximada de que el el borracho se halle a 2 pasos del origen luego de 10 pasos es", prob)


## ahora se evalua como cambia la probabilidad conforme se aumenta el número de experimentos.
## se calculará la probabilidad realizando 1, 2 , .. 10000 experimentos, y se observa como se
## se estabiliza la probabilidad.

A=[]

cont = 0

k = 1

while k < 10000:


  x=0  # inicializa coord origen.
  y=0

  for i in range(10):  # se tomarán 10 pasos desde la pos inicial.


    s = random.randint(1,4)  ## selector ( toma valores entre 1 y 4 aleatoriamente)

    ## 1 corresponde hacia la izquierda, 
    # 2 mov hacia arriba.
    # 3 mov hacia izquierda.
    #   4 mov hacia abajo.


    if s==1 :           

        x = x + 1
        y = y + 0

    if s==2:

        x = x + 0
        y = y + 1

    if s==3:

        x = x -1
        y = y +0

    if s==4:

        x = x + 0
        y = y - 1

  cf = (x,y)  # coordenada final

  #print(cf) 

  # coordenadas de puntos posibles ubicados a 2 pasos del origen.

  

  if cf== (2,0) or cf ==(1,1) or cf ==(0,2) or cf==(-1,1) or cf ==(-2,0) or cf == (-1,-1) or cf==(0,-2):

    cont = cont + 1

    A.append(cont)

  else:

    A.append(0)

  k = k + 1

B = np.array(A)

noexp = np.arange(1,10000,1)

probabi = B / noexp

plt.plot(noexp,probabi)
plt.xlabel("Número de experimentos")
plt.ylabel("Probabilidad")
plt.title(" Probabilidad de desplazamientos de 2 pasos vs # de experimentos")
plt.grid()

## el resultado de la gráfica muestra que que conforme aúmenta el número de experimentos, la probabilidad
## de que que el borracho quede a 2 pasos respecto al origen, se estabiliza aproximadamente despues de 1000 experimentos
## y su valor se aproxima a 0.32 .
