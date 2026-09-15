from ejercicio import division

def test_division():
    assert division(10, 2) == 5

def test_division_entre_cero():
    assert division(10, 0) == "No division entre 0"