
import tiroparabolico as tp  # importa clase 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__=='__main__':


    te = np.linspace(0,4,100)    # tiempo de 4 segundos.

    ###def __init__(self,ang,v0,px0,ax,t)  parametro de entrada.

    # ang = radianes.



    posicionx = tp.TiroParabolico((np.pi)/6.0, 10*np.sin(np.pi/6.0),-3.0,0,te)  ##ax= -3

    print("la posicion en x es" , posicionx.posx())

    

    ## ahora se heredan caracteristicas de la posicion en x para calcular sobre y.

    # secambian los parámetros de ay, velinicial en y.


    posiciony = tp.TiroParabolico((np.pi)/6.0,10*np.cos(np.pi/6.0),50,-9.8,te)   ## altura 50 metros, gravedad 0 -9.8

    posy = posiciony.posx()


    plt.plot( posicionx.posx(), posy)
    plt.show()
    plt.grid()


    









