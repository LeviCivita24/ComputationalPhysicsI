import numpy as np
import matplotlib.pyplot as plt
class particulaCampoBuniforme: 
    #Se utiliza el método del constructor para inicializar atributos
    def __init__(self, theta, masa, carga,Icampo, Ek, tiempo):
        self.theta = theta  #Ángulo de la partícula con respecto a dirección del campo 
        self.m = masa   #Masa de la partícula que ingresa en el campo
        self.q = carga #Carga de la partícula
        self.B = Icampo #Intensidad del campo 
        self.K = Ek #Energía cinética de la partícula 
        self.t = tiempo #Tiempo, generalmente va a ser un arreglo 

    """
        El primer método que se crea es con el fin de encontrar la frecuencia 
        ciclotrónica(mirar pdf). Este valor sirve para ser utilizado para todas las 
        ec's que se van a implementar.  
    """
    def freCiclo(self): 
        self.wc = (self.q*self.B)/self.m 
        return self.wc
    
    """
        Se utiliza la expresión de la energía cinética para encontrar la magnitud
        de la velocidad inicial, la cual también será implementada en el resto de 
        expresiones. 
    """
    
    def veloIni(self): 
        self.vo = np.sqrt( (2*self.K)/self.m )
        return self.vo 
    
    """
        Se implementan las expresiones que permiten determinar como evolucionan las 
        coordenadas de la partícula en cada uno de sus ejes. 
    """

    def coordEvolucion(self): 
        self.xt = np.zeros(len(self.t))
        self.yt = np.zeros(len(self.t))
        self.zt = np.zeros(len(self.t)) 
        for i in range(0,len(self.t)): 
            self.xt[i] = ( (self.veloIni()*np.sin(self.theta))/self.freCiclo() ) * np.sin(self.freCiclo()*self.t[i])
            self.yt[i] = ( (self.veloIni()*np.sin(self.theta))/self.freCiclo() ) * ( np.cos(self.freCiclo()*self.t[i]) -1)
            self.zt[i] = self.veloIni()*np.cos(self.theta)*self.t[i]
        
        fig1 = plt.figure() 
        plt.title('Evolución de las trayectorias en función del tiempo')
        plt.plot(self.t, self.xt, color = 'red', label='x(t)')
        plt.plot(self.t, self.yt, color = 'blue', label='$y(t)$')
        plt.legend()
        plt.grid()
        plt.show()
        fig2 = plt.figure()
        plt.title('Evolución de las trayectorias en función del tiempo')
        plt.plot(self.t, self.zt, color = 'black', label = 'z(t)')
        plt.legend()
        plt.grid()
        plt.show() 
        fig3 = plt.figure()
        plt.title('Trayectoria de la partícula')
        ax = plt.axes(projection='3d')
        ax.plot3D(self.xt, self.yt, self.zt,'gray')
        plt.show()

        return "El arreglo para x(t) es: \n{}\nEl arreglo para y(t) es: \n{}\nEl arreglo para z(t) es: \n{}".format(self.xt, self.yt, self.zt, fig1, fig2,fig3)  
    
    def helicoide(self): 
        self.vox = self.veloIni()*np.sin(self.theta) 
        self.y = -self.veloIni()*np.sin(self.theta)/self.freCiclo() + np.sqrt( ( self.veloIni()*np.sin(self.theta)/self.freCiclo() )**2 - self.xt**2 )
        self.y1 = -self.veloIni()*np.sin(self.theta)/self.freCiclo() - np.sqrt( ( self.veloIni()*np.sin(self.theta)/self.freCiclo() )**2 - self.xt**2 )

        self.z = self.veloIni()*np.cos(self.theta)*self.t
        fig1 =plt.figure()
        plt.title('Trayectoria de la partícula')
        ax = plt.axes(projection='3d')
        ax.plot3D(self.xt, self.y, self.z,'gray')
        ax.plot3D(self.xt,self.y1, self.z, 'gray')
        plt.show()
        
        return "Las coordenadas del círculo en función del tiempo son: \n{}".format(self.y, fig1) 


        


        

        