from ejercicio import potencia

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 2) == 25
    assert potencia(10, 0) == 1

test_potencia()
print('Todas las pruebas pasaron')