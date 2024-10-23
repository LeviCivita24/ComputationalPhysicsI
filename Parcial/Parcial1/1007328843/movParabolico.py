import numpy as np 
import matplotlib.pyplot as plt 

'''
    César Hoyos
    1007328843 
'''
class movimiento: 
    def __init__(self, Xox, Yoy, Vo, theta, gravedad, viento_aire,t):
        #Condiciones iniciales en la posición 
        self.Xox = Xox
        self.Yoy = Yoy
        #Condiciones iniciales en la velocidad
        self.Vo = Vo 
        #Ángulo de lanzamiento 
        self.theta = theta 
        #Gravedad
        self.g = gravedad
        #Fricción con aire
        self.fr = viento_aire 
        #Condiciones iniciales en la velocidad
        self.Vox = self.Vo*np.cos(self.theta)
        self.Voy = self.Vo*np.sin(self.theta)
        self.t = t 
        
    '''Ahora empezamos a definir cada uno de los métodos que son solicitados'''
    
    def tiempo_vuelo(self): 
        self.vuelo = -2 * self.Vo * np.sin(self.theta) / self.g
        return self.vuelo
    
    #Implementación vx 
    def velocidad_x(self): 
        self.vx = self.Vo * np.cos(self.theta) + self.fr * self.t
        return self.vx 

    #Implementación vy
    def velocidad_y(self): 
        self.vy = self.Vo * np.sin(self.theta) + self.g * self.t
        return self.vy 

    #Implementación del alcance máximo
    def alcance_max(self): 
        self.xmax = self.Xox + self.Vo * np.sin(self.theta) * self.tiempo_vuelo() + (1/2) * self.fr * (self.tiempo_vuelo()) ** 2
        return self.xmax    
    
    #Implementación de altura máxima
    def altura_max(self): 
        self.ymax = self.Yoy + self.Vo * np.sin(self.theta)*(self.tiempo_vuelo()/2) - (1/2)*self.g*(self.tiempo_vuelo()/2)**2
        return self.ymax  

    #Implementación de x(t)
    def x_t(self): 
        self.x_t = self.Xox + (self.Vo*np.cos(self.theta))*self.t + (1/2)*self.fr*(self.t**2)
        return self.x_t 

    # Implementación de y(t)
    def y_t(self): 
        self.y_t = self.Yoy + (self.Vo*np.sin(self.theta))*self.t + (1/2)*self.g*(self.t**2)
        return self.y_t

# Herencia múltiple
class Grafica(movimiento):
    def __init__(self, Xox, Yoy, Vo, theta, gravedad, viento_aire, t,x,y):
        movimiento.__init__(self, Xox, Yoy, Vo, theta, gravedad, viento_aire, t)
        self.x = x
        self.y = y
    def grafica(self): 
        plt.plot(self.x, self.y)
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada Y")
        plt.title("Trayectoria")
        plt.show() 





        


    


