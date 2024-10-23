import numpy as np
import matplotlib.pyplot as  plt


def rk4(f,y,t,b,n):
    '''------------------ Runge-kutta 4  ------------------------
    resuelve un sistema con varias ecuaciones diferenciales (ode)
    '''
    
    d  = len(y)      # obtener número de ecuaciones.
    k1 = k2 = k3 = k4 = np.zeros(d)
    
    tt = np.zeros(n)    # array tiempo
    Y  = np.zeros((d,n))# array coords      
    h = (b - t)/n
    ti = 0
    while ti<n:

        Y[:, ti] = y # almacene coords al tiempo t_i
        tt[ti] = t   # almacene el tiempo

        # *** runge kutta 4 metodo ***   
        k1 = h*f(t, y)
        k2 = h*f(t + h/2., y + k1/2.)
        k3 = h*f(t + h/2., y + k2/2.)
        k4 = h*f(t + h, y + k3)
        
        y = y + (k1 + 2.*(k2 + k3) + k4)/6.
    
        t = t + h   # incremente el tiempo por h
        ti = ti + 1 # incremente el contador  
        
    return Y,tt     # output: arrays con coords y tiempo para graficar.


## parámetros de entrada.

a, b = 0, 10.  # intervalo de integración
n = 10000      # Número max de pasos de integración
y0 = np.array([np.pi/3.0, 0]) # Condición inicial (pos, vel)

def f(t, y):   # función a integrar de la forma y'(t) = f(t,y(t))  
    g = 9.8 #[m/s**2]
    l= 1.0 # metros     
    f1 = y[1] ## y[1] = w'(t)
    f2 = (-g/l)*np.sin(y[0])

    return np.array([f1, f2])


Y, time = rk4(f,y0, a,b, n)  # llamar rk4
    
plt.plot(time, Y[0])
plt.plot(time, Y[1])
plt.legend( ["$y(t)$", "$v(t)$"], numpoints=1)
plt.xlabel('t')
plt.show()