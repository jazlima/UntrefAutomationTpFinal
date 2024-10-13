#Escribir una función que dado el ingreso de 3 variables (a, b, c) 
#retorne las raíces resultantes de una ecuación cuadrática.

def ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        raiz1 = (-b + (discriminante)**0.5) / (2*a)
        raiz2 = (-b - (discriminante)**0.5) / (2*a)
        return f"Las raíces son reales y diferentes: {raiz1}, {raiz2}"
    
    elif discriminante == 0:
        raiz = -b / (2*a)
        return f"Hay una raíz real doble: {raiz}"
    
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = (abs(discriminante))**0.5 / (2*a)
        return f"Las raíces son complejas: {parte_real} + {parte_imaginaria}i, {parte_real} - {parte_imaginaria}i"
    

a = 1
b = -3
c = 2
print(ecuacion_cuadratica(a, b, c))