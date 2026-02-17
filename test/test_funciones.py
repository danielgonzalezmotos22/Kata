from services.funciones import *


def test_vacio_y_0():
    assert calcular('') == 0 #si la lista esta vacia
    assert calcular('0') == 0 #si te da o
def test_1():
    assert calcular('1') == 1 
def test_suma_varios():
    assert calcular('1,2') == 3 
    assert calcular('1,2,3') == 6

def test_salto_de_linea():
    assert calcular('1\n2,3') == 6