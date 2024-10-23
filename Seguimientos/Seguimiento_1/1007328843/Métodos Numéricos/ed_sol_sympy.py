import sympy as sp 

x = sp.symbols('x')
y = sp.Function('y')(x)

def f(x,y): 
    return 2*x*y

dyx = y.diff(x)
fun = sp.Eq(dyx, f(x,y))
sol =sp.dsolve(fun)
print("La solución a la EDO es: {}".format(sol))


