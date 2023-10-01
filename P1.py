'''
Se pide sumar los múltiplos de 3 y de 5
Los multiplos de 3 es la sumatoria de 3*i, Los de 5 es 5*i y se debe restar los múltiplos comunes
que en este caso son los múltiplos de 15.
'''
#Formula de sumatoria
def suma(n,a):
    if n%a==0: #Si uno de los números es divisor de n, no se incluye el último término.
        return int(a*(n//a-1)*(n//a)/2)
    else:
        return int(a*(n//a)*(n//a+1)/2)
#Maximo común divisor
def MCD(a,b):
    if b==0:
        return a
    return MCD(b,a%b)
#Minimo común múltiplo
def mcm(a,b):
    return int(a*b/MCD(a,b))
#Desarrollo punto1
def P1(n,a,b):
    return suma(n,a)+suma(n,b)-suma(n,mcm(a,b))

print(P1(10000,3,5))
