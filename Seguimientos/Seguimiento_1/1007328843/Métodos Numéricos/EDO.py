import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

class Metodos_Matematicos: 
    def __init__(self, cix, ciy,a, b, f, valor, h): 
        self.cix = cix #Condición inicial en x
        self.ciy=ciy #Condición inicial en y
        self.a = a #Intervalo xo inicial 
        self.b = b  #Intervalo xf final 
        self.f =f   #La función 
        self.valor= valor  #Si quieres conocer y(1,2) simplemente ingresas valor=1 
        self.h = h #El valor de divisiones que se quiere utilizar

    def Euler_listas(self): 
        #En primer lugar se crean dos listas vacías 
        self.x = [] 
        self.y = []
        #Se introducen en la primera posición de las listas las condiciones iniciales
        self.x.append(self.cix) 
        self.y.append(self.ciy)
        #Se hace una variable que define el número de divisiones
        self.n1 = (self.b - self.a)/self.h 
        #Se realiza un for que implementa el método de Euler 
        for k in range(int(self.n1 -1)): #El INT se utiliza para asegurar que el for funcione
            self.x.append(self.h + self.x[k])
            self.y.append(self.y[k] + self.h*self.f(self.x[k], self.y[k]))

        #Se transforman las listas a un array de numpy 
        self.x = np.array(self.x) 
        self.y = np.array(self.y) 

        #El valor donde sea min significa que valor está más cercano a x
        self.N = np.abs(self.x - self.valor) 
        self.N1 = np.where(self.N==min(self.N))

        #Luego se elige los valores que se deben tomar 
        self.array = [self.x[self.N1], self.y[self.N1]] 

    
        return "El arreglo en X es: \n{} \nEl arreglo en Y es: \n{} \nPara un valor de X={} \nSe obtiene un Y={} \nObteniendo finalmente un punto con coordenadas: [{},{}] ".format(self.x, self.y,self.valor, self.array[1][0], self.array[0][0],self.array[1][0])

    def RK4_listas(self): 

        #Se crean las respectivas que permiten realizar el algoritmo de manera iterativa
        self.x = [] 
        self.y = []
        self.k1 = []
        self.k2 =[]
        self.k3 =[]
        self.k4 =[]

        #Se introducen las condiciones iniciales en las listas
        self.x.append(self.cix)
        self.y.append(self.ciy)

        #Se crea el una variable con el número de iteraciones 
        self.n1 = (self.b - self.a)/self.h 
        #Algoritmo que permite realizar runge Kutta

        for k in range(int(self.n1 -1)): #El INT permite que el for se ejecute  
            self.x.append( self.h + self.x[k])  #Se implementa la ecuacion para x
            self.k1.append(self.h*self.f(self.x[k], self.y[k])) #Se implementa la ecuacion para k1
            self.k2.append(self.h*self.f(self.x[k] +self.h/2, self.y[k] + self.k1[k]/2 )) #Se implementa la ecuacion para k2
            self.k3.append(self.h*self.f( self.x[k] + self.h/2, self.y[k] + self.k2[k]/2  ) ) #Se implementa la ecuacion para k3
            self.k4.append(self.h * self.f(self.x[k] + self.h, self.y[k] + self.k3[k]  )) #Se implementa la ecuacion para k4
            self.y.append( self.y[k] + (1/6)*(self.k1[k] + 2*self.k2[k] + 2*self.k3[k] +self.k4[k])) #Se implementa la ecuacion para y
        
        #Se transformar las listas en arreglos 
        self.x = np.array(self.x)
        self.y = np.array(self.y)


        #El valor donde sea min significa que valor está más cercano a x
        self.N = np.abs(self.x - self.valor) 
        self.N1 = np.where(self.N==min(self.N))

        #Luego se elige los valores que se deben tomar 
        self.array = [self.x[self.N1], self.y[self.N1]]

              
        return "El arreglo en X es: \n{} \nEl arreglo en Y es: \n{} \nPara un valor de X={} \nSe obtiene un Y={} \nObteniendo finalmente un punto con coordenadas: [{},{}] ".format(self.x, self.y,self.valor, self.array[1][0], self.array[0][0],self.array[1][0])

    def Analitico(self): 
        #Condiciones iniciales
        self.xo = self.cix
        self.yo = self.ciy  
        
        #Solución de la ecuación diferencial 
        self.n1 = (self.b - self.a)/self.h 
        self.t = np.linspace(self.a, self.b,int(self.n1))
        
        self.edo = odeint(self.f, self.yo, self.t) 
        self.edo = np.array(self.edo)

        #El valor donde sea min significa que valor está más cercano a x
        self.N = np.abs(self.t - self.valor) 
        self.N1 = np.where(self.N==min(self.N))

        #Luego se elige los valores que se deben tomar 
        self.array = [self.t[self.N1], self.edo[self.N1]]


        return "La solución a la Ed de forma analitica es: \n{}\nEl valor para X={} da un valor para Y de {}".format(self.edo,self.valor,self.edo[self.N1][0][0]) 











