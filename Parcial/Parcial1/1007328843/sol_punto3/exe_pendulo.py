import pendulo as pd 
import numpy as np
import matplotlib.pyplot as plt 

if __name__=='__main__': 
    u0 = np.pi/2 # Condicion inicial en el desplazamiendo angular para CI1
    du0 = 0 # CI para la velocidad angular para CI1 
    t = 0 # Tiempo inicial
    ht = 0.001 # Pasos
    u = [t,u0,du0] # condicion inicial 1 
    u1 = [t, 0.1, 0] # condicion inicial 2
    u2 = [t, 3.1, 0]
    tf = 20 # tiempo final 
    n=2 # Orden de la ecuacion diferencial
    g = 9.8 # Gravedad
    k= 0    # Constante de velocidad
    l = 1   # Longitud pendulo
    objeto = pd.PenduloNoLineal(t, ht, n, g, l, k, tf, t, u[1], u[2])
    objeto1 = pd.PenduloNoLineal(t, ht, n, g, l, k, tf, t, u1[1], u1[2])
    objeto2 = pd.PenduloNoLineal(t, ht, n, g, l, k, tf, t, u2[1], u2[2])

    tiempo = [] 
    
    pos = [] 
    pos1 = []
    pos2 = []

    velocidad = []
    velocidad1 = []
    velocidad2 = []

    while (t+ ht <= (tf)): 
        # Se evalua la condicion inicial 1
        var = objeto.RK4(t, ht, u, n)
        tiempo.append(t)
        pos.append(var[1])
        velocidad.append(var[2])
        # Se evalua la condicion inicial 2
        var1 = objeto1.RK4(t, ht, u1, n)
        pos1.append(var1[1])
        velocidad1.append(var1[2])
        #Se evalua la CI 3
        #var2 = objeto1.RK4(t, ht, u2, n)
        #pos2.append(var2[1])
        #velocidad2.append(var2[2])
        t += ht


plt.title("Pos Angular vs tiempo")
plt.plot(tiempo, pos, label="uo = pi/2", color='green')
plt.plot(tiempo, pos1, label="uo = 0.1", color='blue')
#plt.plot(tiempo, pos2, label="u0 = 3.1", color='red') --> presenta problemas
plt.grid()
plt.legend()
plt.show()
