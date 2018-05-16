'''
Como vimos na aula passada, uma arvore é uma estrutura como


      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 

Observe que 10 tem elementos a sua "esquerda" (5,2 e 3) e a sua "direita" (20, 12 e 30)

Os elementos a esquerda são números menores que 10, e os elementos a direita, maiores que 10.
(O mesmo vale para o 5: a direita, temos 2, que é menor, e a esquerda, 7, que é maior)
'''

'''
Para representar arvores em python, usamos dicionários.

Por exemplo, para representar uma árvore que apenas contém 2, fazemos
'''

arvore2= {'raiz':2,'direita':{},'esquerda':{}}
#e o mesmo para uma arvore que só tem 7
arvore7= {'raiz':7,'direita':{},'esquerda':{}}
'''
E ai, para representar

    5  
   / \ 
  2   7

usamos o dicionário
'''

arvore5 = {'raiz':5, 'esquerda':arvore2, 'direita': arvore7}

'''
Podemos fazer isso também para 
   20
  /  \
 12  30 
'''

arvore12= {'raiz':12,'direita':{},'esquerda':{}}
arvore30= {'raiz':30,'direita':{},'esquerda':{}}
arvore20 = {'raiz':20, 'esquerda':arvore12, 'direita': arvore30}

'''
E, por fim, para

      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 
'''

arvore10={'raiz':10,'direita':arvore20,'esquerda':arvore5}


'''
De uma olhada nessas arvores, no terminal do runTests
'''

'''
Representar uma arvore vazia é bem fácil
'''

vazia= {}

'''
A primeira coisa que vamos fazer nesse arquivo é definir uma funcao
que recebe uma arvore e retorna a sua raiz

Se ela for vazia, sua funcao deve retornar a string 'nao tem raiz'
'''

def raiz(arvore):
    if 'raiz' in arvore:
        root = arvore['raiz']
        return root
    else:
        return "nao tem raiz"
'''
Agora, façamos uma funcao que recebe uma arvore e um numero, e faz uma busca
para ver se o número está ou nao na arvore. 

Ela retorna True se o numero está na arvore, false caso contrário
'''

def busca(arvore,procurado):
    
    if (arvore == {}):
        return False
    if (arvore['raiz'] == procurado):
        return True
    if (arvore['raiz'] > procurado):
        arvore = arvore['esquerda']
        return busca(arvore,procurado)
    if (arvore['raiz'] < procurado):
        arvore = arvore['direita']
        return busca(arvore,procurado)


'''
Agora, vamos fazer uma funcao para calcular a soma de todos os numeros presentes
em uma arvore.
'''

def soma(arvore):
    if (arvore == {}):
        return 0
    return arvore['raiz'] + soma(arvore['esquerda']) + soma(arvore['direita'])

'''
Agora, vamos fazer uma funcao para inserir um elemento em uma arvore.

Por exemplo, ao pegarmos a arvore

      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 

e inserirmos o elemento 15, temos
      
      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 
        \
        15

(Estamos mantendo as propriedades: o 15 tem que estar a direita do 10, a esquerda do 20
e a direita do 12)

(outra coisa: se inserirmos o 5, nada acontece, porque ele já está na arvore)
'''

def insere(arvore,elemento):
    original = arvore
    while arvore != {}:
        if arvore['raiz'] == elemento:
            return original
        if arvore['raiz'] > elemento:
            arvore = arvore['esquerda']
        elif arvore['raiz'] < elemento:
            arvore = arvore['direita']
    arvore['raiz'] = elemento
    arvore['esquerda'] = {}
    arvore['direita'] = {}
    return original

'''
Agora, faça uma funcao que recebe uma arvore e diz quantos elementos ela tem
'''

def conta(arvore):
    count = 1
    if arvore == {}:
        return 0
    else:
        if arvore['esquerda'] != {}:
            count += conta(arvore['esquerda'])
        if arvore['direita'] != {}:
            count += conta(arvore['direita'])
    return count

'''
A partir daqui nao há nada mais pra fazer

'''

ex1= {'direita': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 20}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 12}, 'raiz': 15}, 'esquerda': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 7}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 2}, 'raiz': 5}, 'raiz': 10}

ex2= {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 2}, 'raiz': 3}, 'raiz': 10} 

ex3 = {'direita': {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 110}, 'raiz': 120}, 'esquerda': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 10}, 'esquerda': {}, 'raiz': 5}, 'raiz': 90}
import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_raiz(self):
        self.assertEqual(raiz(arvore5), 5)
        self.assertEqual(raiz(ex1), 10)
        self.assertEqual(raiz(ex2), 10)
        self.assertEqual(raiz(ex3), 90)
        self.assertEqual(raiz({}), 'nao tem raiz')
    
    def test_02_busca(self):
        self.assertTrue(busca(arvore5,5))
        self.assertTrue(busca(arvore10,20))
        self.assertFalse(busca(arvore10,15))
        self.assertTrue(busca(arvore10,7))
        self.assertTrue(busca(arvore10,10))
        self.assertFalse(busca(arvore10,15))
        self.assertFalse(busca(ex3,91))
        self.assertTrue(busca(ex3,90))
        
    def test_03_soma(self):
        self.assertEqual(soma(ex1),71)
        self.assertEqual(soma(ex2),15)
        self.assertEqual(soma(ex3),335)
        self.assertEqual(soma({}),0)

    def test_04_insere(self):
        t2 = insere({},2)
        self.assertEqual(t2, arvore2)
        t5 = insere(insere(insere({},5),2),7)
        self.assertEqual(t5, arvore5)
        t10 = insere(insere(insere(insere(insere(insere(insere({},10),5),2),7),20),12),30)
        self.assertEqual(t10, arvore10)

    def test_05_insere_repetida(self):
        t10 = insere(insere(insere(insere(insere(insere(insere({},10),5),2),7),20),12),30)
        insere(t10,10)
        insere(t10,5)
        insere(t10,20)
        insere(t10,30)
        self.assertEqual(t10, arvore10)

    def test_06_conta(self):
        self.assertEqual(conta(arvore10),7)
        self.assertEqual(conta(arvore5),3)
        self.assertEqual(conta(arvore2),1)
        self.assertEqual(conta({}),0)
        self.assertEqual(conta(ex3),5)


        
        

    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

