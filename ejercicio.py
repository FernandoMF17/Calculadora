def suma (a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def potencia(a, b):
    resul = 1
    for i in range(b):
        resul=resul*a
        return resul
assert potencia(2,3)==8
assert potencia(5,2)==25
assert potencia(10,0)==1