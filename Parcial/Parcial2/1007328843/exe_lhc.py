import lhc 
import matplotlib.pyplot as plt 
if __name__=='__main__':
    N = 10000
    exp = lhc.colisionador(10,10,100,N) # Se crea un objeto 
    val = exp.probabilidad()
    xe = range(0,N)
    plt.plot(xe, val)
    plt.show()