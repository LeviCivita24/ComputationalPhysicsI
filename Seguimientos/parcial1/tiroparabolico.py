
import numpy as np    # importamos librerias.

## definimos clase tiro parabólico.

class TiroParabolico:

    ## definimos atributos, constante del problema y condiciones iniciales. 

    ## el comportamiento en x es similar al comportamiento en y, ya que ambos movimientos siguen un
     # movimient uniformente acelerado, se calculará primero para x y luego el movimiento en y hereda las 
     # caracteristicas del mov en x. 
     # finalmente se grafican la superposicion de los 2 movimientos.( en el archivo ejecutorio.)  

    def __init__(self,ang,v0,px0,ax,t):  ## (angulo,rapidezini,posxinicial,posyinicial,acelx,acelx,acely,tiempo) 

        self.ang = ang
        self.v0 = v0
        self.px0 = px0
       # self.py0 = py0
        self.ax = ax
        #self.ay= ay
        self.t = t


    ## ahora definamos métodos dentro de la clase.

    def velx(self):  ## velocidad en x en función del tiempo.

        self.vx = (self.v0) + (self.ax) * (self.t)

        return (self.vx)


    def posx(self):

        #self.px = (self.px0) + (self.v0)*(np.cos(self.ang))*(self.t) + (0.5)*(self.ax)*(self.t**2)

        #return (self.px)

        self.px = (self.px0) + (self.v0)*(self.t) + (0.5)*(self.ax)*((self.t)**2)

        return (self.px)


    ## para y.


    #def vely(self):  ## velocidad en x en función del tiempo.

        #self.vy = (self.v0)*(np.sin(self.ang)) + (self.ay) * (self.t)

        #return (self.vy)


    #  def posy(self):

        #self.py = self.py0 + (self.vo)*(np.sin(ang))*(self.t) + (0.5)*(ay)*((self.t)**2)

        #return (self.py)


    


    


    





    



    







