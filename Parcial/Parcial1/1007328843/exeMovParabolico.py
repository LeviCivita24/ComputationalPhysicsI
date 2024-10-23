import movParabolico as mp
import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__': 
    
    t = np.arange(0,0.66,0.01)
    objeto = mp.movimiento(0, 0,5,0.71,-9.8,-5,t)
    tiempo_vuelo =objeto.tiempo_vuelo()
    print(tiempo_vuelo) 
    #Un while que me permite darle significado físico al problema
    while objeto.tiempo_vuelo() >= t[-1]: 
        x = objeto.x_t()
        y = objeto.y_t()
        grafica = mp.Grafica(0, 0,5,0.71,-9.8,-5,t, x,y)
        grafica.grafica() 
        
    else: 
        print("El problema no tiene significado físico")

    #t = np.arange(0,objeto.tiempo_vuelo(),0.01)
    #objeto = mp.movimiento(0, 0,5,0.71,-9.8,-5,t)
    #x = objeto.x_t()
    #y = objeto.y_t()
    
   
    
