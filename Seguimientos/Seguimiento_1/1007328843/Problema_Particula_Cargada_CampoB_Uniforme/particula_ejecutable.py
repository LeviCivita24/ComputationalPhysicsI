import particula_clase as pc
import numpy as np 

if __name__=='__main__': 
    t = np.arange(1,10,0.01) #Se crea el arreglo de tiempo 
    electron = pc.particulaCampoBuniforme(np.pi/6,9.11e-31,1.62e-19,600e-6,18.6*1.60e-19,t)
    print(electron.coordEvolucion())
    print(electron.helicoide())
