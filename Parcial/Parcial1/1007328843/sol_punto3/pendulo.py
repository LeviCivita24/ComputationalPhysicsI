import numpy as np 
class PenduloNoLineal:
    '''
        Implemento el algoritmo de RK dado por el texto debido a que el que se implemento
        en clases posteriores solo funcionaba de manera correcta para ed's de primer orden, al ir aumentando
        el orden de la ecuacion diferencial y el metodo de runge es sucesivo la expansion en series se ve
        incrementada
    '''
    def __init__(self, t,ht, n, gravedad, l, k, tf, ti, u0, du0):
        self.ht = ht # Pasos de tiempo 
        self.t = t # Inicializador de tiempo 
        self.n = n # Orden de la ED
        self.g = gravedad # Gravedad
        self.l = l # Longitud del pendulo
        self.k = k # Coeficiente de velocidad
        self.tf = tf # Tiempo final
        self.ti = ti # Tiempo inicial 
        self.u0 = u0 # Condicion inicial en el desplazamiento 
        self.du0 = du0 # Condicion para velocidad inicial 
        self.u = [self.t, self.u0, self.du0]  # Arreglo con CI's

    def DesplazamientoAngular(self, t, u, f):
        f[1] = self.u[2] 
        f[2] = (-self.g / self.l) * np.sin(self.u[1]) - self.k * self.u[2]
        return f
            
    def RK4(self, t, ht, u, n):
        
        #Aca se crean algunas listas vacias de tamano dado por n,es decir, si n=3
        #la lista tendra un tamano de 4 ceros [0, 0, 0, 0]
        f1 = [0] * ( self.n + 1); f2 = [0] * (self.n + 1) 
        f3 = [0] * ( self.n + 1); f4 = [0] * ( self.n + 1)  
        yt = [0] * ( self.n + 1)
        ht2 = self.ht/2 #define un valor de la mitad de los pasos
        #Se implementa el metodo de Runge Kutta en dos variables
        f1 = self.DesplazamientoAngular(self.t, self.u, f1)
        for i in range(1, self.n + 1): yt[i] = self.u[i] + ht2 * f1[i]
        f2 = self.DesplazamientoAngular(self.t + ht2, yt, f2)
        for i in range(1, self.n + 1): yt[i] = self.u[i] + ht2 * f2[i]
        f3 = self.DesplazamientoAngular(self.t + ht2, yt, f3)
        for i in range(1, self.n+1): yt[i] = self.u[i] + self.ht * f3[i]
        f4 = self.DesplazamientoAngular(self.t + self.ht, yt, f4) 
        h6 = self.ht / 6 
        for i in range(1, self.n + 1): self.u[i] += h6 * (f1[i] + 2 * (f2[i] + f3[i]) + f4[i])
        return self.u 