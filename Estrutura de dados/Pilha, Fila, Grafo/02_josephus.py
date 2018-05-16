'''
O problema de Josephus é assim conhecido por causa da lenda 
de Flavius Josephus, um historiador que viveu no século 1. 
Segundo o relato de Josephus do cerco de Yodfat, 
ele e seus companheiros (40 soldados) foram presos em uma caverna, 
cuja saída foi bloqueada pelos romanos. 

Eles preferiram suicidar-se a serem capturados, 
e decidiram que iriam formar um círculo e começar a matar-se 
pulando de três em três. 
Josephus afirma que, por sorte ou talvez pela mão de Deus, 
ele permaneceu por último e preferiu 
entregar-se aos romanos a suicidar-se.

Em cada caso de teste de entrada haverá um par de números 
inteiros positivos "pessoas" e "pulo". O  número "pessoas" representa 
a quantidade de pessoas no círculo, 
numeradas de 1 até n. 
O número "pulo" representa o tamanho do salto 
de um homem até o próximo homem que será morto.

Junto desse arquivo, há uma imagem fazendo um exemplo,
com 5 homens e pulo = 2

Neste exemplo o elemento que restará após as eliminações é 3. 
'''

'''
Nesse arquivo, faremos o seguinte: criaremos uma funcao josephus
que recebe 2 numeros: o numero de pessoas e o pulo.

Lembrando que as pessoas tem "nomes" 1,2,3..n, a funcao
deve retornar o numero do sobrevivente 

A ideia é fazer isso da seguinte forma:
    comece com uma lista de 1,2,3...n (gerada com range: list(range(1,pessoas+1)))
    enquanto tem mais de uma pessoa na lista, vá retirando as pessoas pelo
    comeco da lista, e devolvendo no final.

    controle quantas pessoas voce esta tirando, de forma que, quando tiver tirado
    "pulo" pessoas, voce nao insira essa pessoa de volta
'''
def josephus(pessoas,pulo):
    #vivos = list(range(1,pessoas+1))
    #luck -= 1
    #kill = luck 
    #while (len(vivos) > 1):
    #    vivos.pop(kill)
    #    kill = (kill + pulo) % len(vivos)
    #return vivos[0]
    vivos = list(range(1,pessoas+1))
    luck = 1
    while (len(vivos) > 1):
        if luck != (pulo+1):
            luck +=1
            vivos.pop(0)
        else:
            safe = vivos.pop(0)
            vivos.append(safe)
            luck = 1
    return vivos[0]
        



import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_josephus(self):
        self.assertEqual(josephus(5,2),3)
        self.assertEqual(josephus(6,3),1)
        self.assertEqual(josephus(1234,233),25)

    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

