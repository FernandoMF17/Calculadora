def suma (a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a/b

# Pruebas de la funcion division
# Prueba 1: division normal
print(division(50, 10))   #Resultado esperado: 5.0

# Prueba 2: division entre cero
print(division(20, 0))    #Resultado esperado: "No se puede dividir entre cero"
