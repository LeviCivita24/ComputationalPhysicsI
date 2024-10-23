import EDO as eu

if __name__ == '__main__':
    def f(x,y): 
        return 2*x*y
    v1 = eu.Metodos_Matematicos(1,1,0,5,f,2,0.1)
    print("Para el método de Euler \n",v1.Euler_listas())
    print("---***---"*30)
    print("Para el método de Rk4 \n",v1.RK4_listas())
    print("---***---"*30)
    print("Para el método análitico \n{}".format(v1.Analitico())) #--> No ha dado

    
    


