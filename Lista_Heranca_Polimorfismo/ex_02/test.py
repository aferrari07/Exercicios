from main import ex01

def test_ex_01():
    assert ex01("cesar",1500,10) == 1650
    assert ex01("vinicius", 1000, 10) == 1100
    assert ex01("lucas", 3500, 15) == 4025
