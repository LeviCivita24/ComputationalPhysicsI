import matplotlib.pyplot as plt
import numpy as np

F = []

for j in range(10000):
    X = []
    Y = []
    Z = []
    x = 0
    y = 0
    for i in range(10):
        n=np.random.randint(0,100)
        if n<= 25:
          y = y+1
          X.append(x)
          Y.append(y)
        elif n<=50: 
           y = y-1
           X.append(x)
           Y.append(y)
        elif n<=75: 
           x = x+1
           X.append(x)
           Y.append(y)          
        elif n<=100: 
           x = x-1
           X.append(x)
           Y.append(y)
        Z.append(X[i]+Y[i])          
    F.append(Z[-1])   

for i in range(len(F)):
  if abs(F[i])!=2: 
    F[i]=0       
  else:
    F[i]=1    #Casos de exito


P = np.cumsum(F)/np.arange(1,10001) #Probabilidad acumulada

plt.figure(dpi=120)
plt.plot(np.arange(0,10000),P*100)
plt.grid()
plt.title('PROBABILIDAD ACUMULADA')
plt.xlabel('# de Experimentos')
plt.ylabel('Probabilidad(%)')
plt.show()
