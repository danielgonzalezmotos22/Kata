from services.funciones import *

def test_calcular():
    assert calcular('') == 0
    assert calcular('0') == 0
    assert calcular('1') == 1
    assert calcular('1,2') == 3
    assert calcular('1,2,3') == 6