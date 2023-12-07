from calculadora import Calculadora


# testes soma
def test_01_soma_0_0():
    calc = Calculadora()
    assert calc.soma(0, 0) == 0


def test_01_soma_10_0():
    calc = Calculadora()
    assert calc.soma(10, 0) == 10
    assert calc.soma(0, 10) == 10


def test_01_soma_3_5():
    calc = Calculadora()
    assert calc.soma(3, 5) == 8
    assert calc.soma(5, 3) == 8


# testes subitração

def test_01_subi_0_0():
    calc = Calculadora()
    assert calc.subi(0, 0) == 0


def test_01_subi_10_0():
    calc = Calculadora()
    assert calc.subi(10, 0) == 10
    assert calc.subi(0, 10) == -10


def test_01_subi_3_5():
    calc = Calculadora()
    assert calc.subi(3, 5) == -2
    assert calc.subi(5, 3) == 2


# testes multiplicação


def test_01_mult_0_0():
    calc = Calculadora()
    assert calc.mult(0, 0) == 0


def test_01_mult_10_0():
    calc = Calculadora()
    assert calc.mult(10, 0) == 0
    assert calc.mult(0, 10) == 0


def test_01_mult_3_5():
    calc = Calculadora()
    assert calc.mult(3, 5) == 15
    assert calc.mult(5, 3) == 15
