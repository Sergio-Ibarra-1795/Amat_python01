#Using simpy  
# SymPy is a Python library that allows you to compute mathematical objects symbolically.

# To install SymPy, type:
# pip install sympy
# Now let’s go over some of the amazing things that SymPy can do!
# Start with importing all methods provided by SymPy
# from sympy import *


from sympy import * 


x, y = symbols("x y")
expr = 3 * x + y
print(expr)


#Resolviendo una ecuación (encontrando raices)
eq = (2 * x + 1) * 3 * x
print(eq)
solution = solve(eq, x)
print(solution)


#Derivando una expresión 
expr2 = sin(x) ** 2 + 2 * x
print(f'La expresión original (primitiva es:) {expr2}')
derivada = diff(expr2)
print(f'La derivada es {derivada}')


#Integrando una expresión 
primitiva = integrate(derivada)
print(f'La primitiva es {primitiva}')


#Factiroal x 
factorial = factorial(5)
print(factorial)





