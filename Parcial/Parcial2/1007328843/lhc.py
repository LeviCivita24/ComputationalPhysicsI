import numpy as np 

class colisionador: 
    def __init__(self, r1, r2, R, N): 
        self.r1 = r1 # Radio particula 1
        self.r2 = r2 # Radio particula 2 
        self.R = R # Radio del LHC
        self.N = N # Cantidad de experimentos

    # Para la partícula 1 
    def p1(self): 
        #las condiciones sobre x1 y y1 es para evitar que caiga fuera del circulo
        x1 = np.random.uniform(-self.R + self.r1, self.R - self.r1)  
        y1 = np.random.uniform( -self.R + self.r1, self.R - self.r1) 
        return x1, y1 
    
    def p2(self): 
        # las condiciones sobre x2 y y2 es para evitar que caiga fuera de un círculo 
        x2 = np.random.uniform(-self.R + self.r2, self.R - self.r2)
        y2 = np.random.uniform( -self.R + self.r2, self.R - self.r2) 
        return x2, y2     
    
    def colision(self): 
        x1, y1 = self.p1() 
        x2, y2 = self.p2() 
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5
    
    def probabilidad(self): 
        p = [] # probabilidad
        cc = [] # cuenta las colisiones
        while (self.N >=1):
            val = self.colision() 
            if val <= self.r1 + self.r2: 
                cc.append(1) 
            else: 
                cc.append(0)
            
            acum = sum(cc) / len(cc)
            p.append(acum)
            self.N = self.N - 1 
        return p 