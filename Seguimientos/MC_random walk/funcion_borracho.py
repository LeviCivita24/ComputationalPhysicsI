import numpy as np 
import matplotlib.pyplot as plt  

def borracho(x,y, N, ini, fini): 
    # x, y son las CI donde arranca el borracho las cuales se van a ir modificando
    # N expresa el numero de pasos del borracho 
    # ini y fini crear un arreglo para generar un numero aleatorio entre esos valores

    path= []
    while N>=1: 
        nr = np.random.randint(ini,fini) 
        if nr <= 25: 
            path.append([0,y+1]) # Se mueve hacia arriba 
        elif 25<nr<=50: 
            path.append([0,y-1]) # Se mueve hacia abajo 
        elif 50<nr<=75: 
            path.append([x+1,0]) # Se mueve a la derecha
        elif 75<nr<=100: 
            path.append([x-1,0]) # Se mueve a la izquierda
        N = N-1  

    path = [[0,0]] + path # Para agregarle el punto inicial 
    path = np.array(path)
    xpath = []
    ypath = []

    for j in range(0,len(path)): 
        xpath.append(path[j][0])
        ypath.append(path[j][1])
    
    xexp = sum(xpath)
    yexp = sum(ypath)
    
    array = np.array([xexp,yexp])

    # Estas sirven para graficar la trayectoria del borracho. 
    SumXpath = np.cumsum(xpath)
    SumYpath = np.cumsum(ypath)
    '''
        Se pueden descomentar las dos siguientes líneas si se quiere ver la 
        trayectoria del borraco y poner a retonar f. 
    '''
    #f = plt.plot(SumXpath, SumYpath, '-o')
    #plt.show() 
    return  array

# Experimento de calculo de probabilidad 
NumExp = 10000;  # Se ingresa el número de experimentos 
graf = np.arange(0,NumExp) 

prob = []
i = 0
while NumExp >i: 
    f =borracho(0,0,10,0,100) 
    fa = abs(f) 
    if sum(fa) == 2: 
        prob.append(1)
    else: 
        prob.append(0) 
    
    i = i+1 

pcum = np.cumsum(prob)/np.arange(1,NumExp + 1) 

plt.plot(graf, pcum,'-o', markersize=0.5)
plt.ylabel("Probabilidad")
plt.xlabel("Experimentos") 
plt.show()

