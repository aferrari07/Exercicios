#O fatorial de 4 é 1*2*3*4
#A definição é a mesma para qualquer inteiro:
#fatorial de n = 1*2*3...*(n-1)*n
#a unica excessao é o zero. Definimos fatorial de 0 como sendo 1
#implemente uma funcao recursiva que calcula o fatorial

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return fatorial(n - 1) * n
#Uma definição simplista (e errada) de logaritmo:
#log é o número de vezes que posso dividir um número por 2,
#até obter 1 ou alguma coisa menor que 1
#por exemplo, log(4)=2 (pois 4/2 dá 2, 2/2 dá 1)
#outro exemplo, log(5)=3 (5/2 dá 2.5, 2.5/2 dá 1.25, 
#1.25/2 dá menos do que 1)

#defina uma funcao log_tosco, recursiva, de acordo com
#essa definição simplista de log

def log_tosco(n):
    if n <= 1:
        return 0 
    else:
        return 1+log_tosco(n/2)
#defina uma função recursiva que retorna o máximo de uma lista

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    maximo_resto = maximo(lista[1:])
    if (maximo_resto > lista[0]):
        return maximo_resto
    return lista[0]
#dica: uma coisa que você vai usar é o calculo recursivo do 
#maximo de lista[1:]
#ou seja, para resolver maximo([4,2,3]) voce vai resolver
#o maximo de lista[1:], que é o máximo([2,3])

#Defina uma função recursiva que recebe uma string e retorna
#a string invertida
def inverte(palavra):
    if len(palavra) == 0 or len(palavra) == 1:
        return palavra
    else:
        primeira_letra = palavra[0]
        resto = palavra[1:]
        invertida_menor = inverte(resto)
        invertida = invertida_menor+primeira_letra
    return invertida
#dica: faça assim: pegue a primeira letra (palavra[0])
# e o resto (palavra[1:])
# inverta o resto depois junte palavra[0]

'''
Imagine que estamos procurando um arquivo em
um computador.
Começamos pelo drive C, mas se nao achamos o arquivo,
devemos descer para as pastas presentes nele,
e tambem para as pastas presentes nas pastas.

Vamos implementar essa logica, procurando a string 'segredo'
em uma lista de listas. Ou seja: segredo pode estar
na lista principal, ou em uma lista dentro dela, ou em uma lista
dentro de uma lista dentro da lista principal (ou... bem, deve 
dar pra entender)

Rode os seguintes comandos no IDLE para entender o problema
Para gerar uma lista que contenha o segredo, use lista=gera(True)
Se ela não deve conter, use lista=gera(False)

Para imprimir uma lista, use imprime(lista)

Você deve implementar uma função recursiva que imprime True
se o segredo está na lista e False caso contrário

Pode gerar listas pra testar

Dica: implementei uma função eh_lista pra você usar.
'''

def acha_segredo(lista):
    return False


'''
Implemente uma função anagramas 
que recebe uma palavra e devolve uma lista com todos 
os seus "embaralhamentos" (anagramas)

Por exemplo, anagramas('ab') deve retornar ['ab','ba']
'''

def anagramas(palavra):
    return []

'''
A partir daqui, não tem nada pra você implementar
'''

import random

def gera(coloca_segredo):
    return gera_r(4,8,coloca_segredo)

def imprime(lista):
    pprint_list(lista)

def gera_r(max_subdirs,max_arquivos,coloca_segredo):
    subdirs,arquivos = 0,0
    lista = []
    if (max_subdirs > 0):
       subdirs = random.randint(max_subdirs//2,max_subdirs)
    for i in range(subdirs):
        lista2 = gera_r(max_subdirs-1,max_arquivos-1,False)
        lista.append(lista2)
    if (max_arquivos > 0):
       arquivos = random.randint(max_arquivos//2,max_arquivos)
    for i in range(arquivos):
        lista.append(random.randint(0,arquivos))
    if (coloca_segredo):
        adiciona_segredo(lista)
    return lista

def adiciona_segredo(lista):
    plana = aplaina(lista)#uma lista com todas as listas
    posicao = random.randint(0,len(plana)-1)
    plana[posicao].append('segredo')

def aplaina(lista):
    plana = []
    plana.append(lista)
    for a in lista:
        if eh_lista(a):
            plana.extend(aplaina(a))
    return plana

def eh_lista(a):
    return isinstance(a,list)


def pprint_list(lista):
   pprint_list_r(lista,0)

def pprint_list_r(lista,profund):
    arquivos = []
    sublistas = []
    espaco = '|    '
    for i in lista:
        if not eh_lista(i):
            arquivos.append(str(i))
        else:
            sublistas.append(i)
    print(espaco*profund+', '.join(arquivos))
    for l in sublistas:
       print(espaco*profund+'/pasta:')
       pprint_list_r(l,profund+1)
       print(espaco*profund+r'\ ')


import unittest
import sys

class TestStringMethods(unittest.TestCase):
    
    def test_01_fatorial_funciona(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(2), 2)
        self.assertEqual(fatorial(5), 1*2*3*4*5)
        self.assertEqual(fatorial(10), 1*2*3*4*5*6*7*8*9*10)
        self.assertEqual(fatorial(50), 
                30414093201713378043612608166064768844377641568960512000000000000
                )

    def test_02_fatorial_recursivo(self):
        sys.setrecursionlimit(50)
        #self.fail('a sua função é recursiva?')
        try:
            fatorial(60)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_03_log_tosco_funciona(self):
        self.assertEqual(log_tosco(1), 0)
        self.assertEqual(log_tosco(2), 1)
        self.assertEqual(log_tosco(5), 3)
        self.assertEqual(log_tosco(128), 7)
        self.assertEqual(log_tosco(1000), 10)
    
    def test_04_log_eh_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            log_tosco(2**60)
            self.fail('a sua função log é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_05_max(self):
        self.assertEqual(maximo([1,2,3]), 3)
        self.assertEqual(maximo([3,2,1]), 3)
        self.assertEqual(maximo([3,10,15,30,2,1]), 30)
    
    def test_06_max_um_elemento(self):
        self.assertEqual(maximo([-1]), -1)
        self.assertEqual(maximo([3]), 3)
    
    def test_07_max_eh_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            maximo(list(range(100)))
            self.fail('a sua função maximo é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao maximo é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_08_inverte(self):
        self.assertEqual(inverte('abb'), 'bba')
        self.assertEqual(inverte('ab'), 'ba')
        self.assertEqual(inverte('aba'), 'aba')
    
    def test_09_inverte_pequeno(self):
        self.assertEqual(inverte('a'), 'a')
        self.assertEqual(inverte(''), '')

    
    def test_10_inverte_eh_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            inverte('a'*100)
            self.fail('a sua função inverte é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao inverte é recursiva')
        finally:
            sys.setrecursionlimit(1000)

    def test_90_acha_segredo(self):
        for i in range(0,100):
            if (i%2 == 0):
               segredo = True
            else:
               segredo = False
            pasta = gera(segredo)
            self.assertEqual(acha_segredo(pasta),segredo)

    def test_91_anagramas(self):
        a = anagramas('abc')
        self.assertEqual(set(a),set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        a = anagramas('abcd')
        self.assertEqual(set(a),set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))
        a = anagramas('abca')
        self.assertEqual(set(a),set(['abca', 'abac', 'acba', 'acab', 'aabc', 'aacb', 'baca', 'baac', 'bcaa', 'bcaa', 'baac', 'baca', 'caba', 'caab', 'cbaa', 'cbaa', 'caab', 'caba', 'aabc', 'aacb', 'abac', 'abca', 'acab', 'acba']))




    


    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

import unittest

    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

