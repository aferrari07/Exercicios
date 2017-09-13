def mdc(m,n):
    anterior = n
    atual    = m
    resto    = anterior % atual
    while resto != 0:
        anterior = atual
        atual    = resto
        resto    = anterior % atual

        return (atual)

def test_mdc():
    assert mdc(4,5) == 1
    assert mdc(40,20) == 20
    assert mdc(40,50) == 10
    assert mdc(17,35) == 1
    assert mdc(49,7) == 7
