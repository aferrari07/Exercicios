from main import ex02

def test_ex_02():
    assert ex02("Cesar",20,"vitor",50,20) == 20
    assert ex02("Fronze", 20, "luiz", 80, 30) == 30
    assert ex02("asjdio", 23423, "djasl", 21, 80) == 80
