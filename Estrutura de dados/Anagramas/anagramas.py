# Lucas Amorim de Lima RA: 1700283
# Vinicius Lucas Silvestre RA: 1700073

#renomeie para anagramas.py
import unittest

#aquecimento

#defina uma função máximo, que recebe uma lista com pelo menos 1 elemento  e retorna o maior elemento presente na lista
def maximo(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i 
    return max

#defina uma função soma, que recebe uma lista com pelo menos 0 elementos e retorna a soma de todos os elementos da lista
def soma(lista):
    sum = 0
    for i in lista:
        sum = sum + i 
    return sum

#anagramas
#dizemos que uma palavra2 é um anagrama de uma palavra1 quando palava2 é um "embaralhamento" das letras de palavra1.
#por exemplo 'banana' e 'nabana'.
#outro exemplo 'abb' e 'bba'.
#um exemplo que não  é anagrama: 'baa' e 'abb'
# implementaremos 3 (ou 4) formas diferentes de detectar se uma string2 é um anagrama de string1.

#crie uma função ordena e compara que recebe string1 e string2 e retorna True se elas sao anagramas uma  da outra.
#Faça  isso  da seguinte maneira: crie uma lista1 com as letras da string1, uma lista2, ordene ambas as listas e compare, elemento a elemento, para ver se todos sao iguais.
#Para ordenar uma lista, basta chamar "lista1.sort()". Ela será ordenada automaticamente.
# Note que é só lista1.sort(), nao lista1 = lista1.sort()
def ordena_e_compara(string1,string2):
    a = list(string1)
    b = list(string2)
    a.sort()
    b.sort()
    return a == b
#crie uma função conta e compara que recebe string1 e string2 e retorna True se elas sao anagramas uma  da outra.
#Faça isso da seguinte maneira: crie um dicionário d1 e um dicionario d2. Para cada caractere c, d1[c] deverá  conter o número de ocorrencias de c na string 1.
# Por exemplo, se string1='banana', então d1['a'] == 3
# Se as duas strings tiverem as mesmas letras, e cada letra ocorrendo o mesmo número de vezes, são anagramas uma  da outra.
# retorne 3 dados: True ou False (se as strings sao ou nao anagramas), d1 e d2.
# por exemplo, conta e compara('aab','abb') deve retornar (False,{'a':2,'b':1},{'a':1,'b':2})
def conta_e_compara(string1,string2):
    from collections import Counter
    a = list(string1)
    b = list(string2)
    Ac = Counter(a)
    Bc = Counter(b)
    return (Ac == Bc, Ac, Bc)
#dica:  use os exemplos para lembrar como manipular dicionarios
#    d1={}; cria dicionario vazio
#    d1['a'] = 15; coloca 15 na posicao a do dicionario
#    d2={'b':27}; cria um dicionario com 27 na posicao b
#    'c' in d1; Verifica se 'c' é uma posicao do dicionário
#crie uma função vai_apagando que recebe string1 e string2 e retorna True se elas sao anagramas uma da outra.
# Ela deve fazer isso da seguinte maneira:
# 1. Crie uma lista2 com cada um dos caracteres de string2 (se houver repetidos, eles devem aparecer na lista repetidos)
# 1a. A lista2 deve estar na mesma ordem da string2
# 2. Para cada caractere na string1, procure na lista2. Se ele estiver lá, troque a primeira ocorrência por ''
# 3. Se você conseguir achar os caracteres da string1, e não sobrou nenhum caractere na lista2, string1 e string2 eram anagramas.
# 4. Devolva: True ou False (se sao ou nao anagramas) e a lista2
# Por exemplo, vai_apagando('banana','ababnx') retorna (False, ['', '', '', 'b', '', 'x']). Ela não encontrou o segundo caracter 'n', e foi por isso que parou.
def vai_apagando(string1,string2):
    return(True,['','','n','','n',''])
#Dica lista2 = list(string2)



# DESAFIO crie uma função gera_e_compara que recebe string1 e string2 e retorna True se elas sao anagramas uma da outra.
# ISSO É UM DESAFIO, não vai ser fácil :)
# a função deve fazer o seguinte:
#1. Gerar todos os anagramas possiveis de string1 e colocá-los numa lista_de_anagramas
#2. Retornar True se string2 está na lista_de_anagramas, e False caso contrário
#3. Retornar também a lista de anagramas
# Por exemplo, gera_e_compara('abc','bca') retorna (True,['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
# Não se preocupe com a ordem da lista de anagramas, e pode repetir ou  não, como quiser.
def gera_e_compara(string1,string2):
    return (True,['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])


class TestStringMethods(unittest.TestCase):
    
    def test_01_max_simple(self):
        self.assertEqual(maximo([1,2,3]), 3)
        self.assertEqual(maximo([3,2,1]), 3)
        self.assertEqual(maximo([3,10,15,30,2,1]), 30)
    
    def test_02_max_neg(self):
        self.assertEqual(maximo([-1,-2,-3]), -1)
        self.assertEqual(maximo([3,4,-7]), 4)

    def test_03_max_small(self):
        self.assertEqual(maximo([-1]), -1)
        self.assertEqual(maximo([3]), 3)

    def test_04_sum_simple(self):
        self.assertEqual(soma([1,2,3]), 6)
        self.assertEqual(soma([3,2,1]), 6)
        self.assertEqual(soma([3,10,15,30,2,1]), 61)
    
    def test_05_sum_small(self):
        self.assertEqual(soma([-1]), -1)
        self.assertEqual(soma([3]), 3)
        self.assertEqual(soma([]), 0)

    def verifica_anagrama(self,func):
        self.assertEqual(func('banana','nabana'),True)
        self.assertEqual(func('banaaa','nabana'),False)
        self.assertEqual(func('banana','nabann'),False)
        self.assertEqual(func('',''),True)
        self.assertEqual(func('','a'),False)
        self.assertEqual(func('a',''),False)

    def test_06_ordena_e_compara(self):
        self.verifica_anagrama(ordena_e_compara)

    def test_07_conta_e_compara(self):
        def versao_true_false(string1,string2):
            return conta_e_compara(string1,string2)[0]
        self.verifica_anagrama(versao_true_false)
        a = conta_e_compara('banana','nabana')
        self.assertEqual(a[1],{'b':1,'a':3,'n':2})
        self.assertEqual(a[2],{'b':1,'a':3,'n':2})
        a = conta_e_compara('banana','nabann')
        self.assertEqual(a[2],{'b':1,'a':2,'n':3})
        
    def test_08_vai_apagando(self):
        def versao_true_false(string1,string2):
            return vai_apagando(string1,string2)[0]
        self.verifica_anagrama(versao_true_false)
        a  = vai_apagando('banana','melancia')
        self.assertEqual(a[1],list('melancia'))
        a  = vai_apagando('banana','banan')
        self.assertEqual(a[1],['']*5)
        a  = vai_apagando('banana','bananaa')
        self.assertEqual(a[1],['']*6+['a'])
        a  = vai_apagando('aaabbb','ca'*3)
        self.assertEqual(a[1],['c','']*3)

    def test_09_gera_e_compara(self):
        def versao_true_false(string1,string2):
            return gera_e_compara(string1,string2)[0]
        self.verifica_anagrama(versao_true_false)
        a = gera_e_compara('abc','cba')
        self.assertEqual(a[0],True)
        self.assertEqual(set(a[1]),set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        a = gera_e_compara('abcd','cbaa')
        self.assertEqual(a[0],False)
        self.assertEqual(set(a[1]),set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))
        a = gera_e_compara('abca','cbaa')
        self.assertEqual(a[0],True)
        self.assertEqual(set(a[1]),set(['abca', 'abac', 'acba', 'acab', 'aabc', 'aacb', 'baca', 'baac', 'bcaa', 'bcaa', 'baac', 'baca', 'caba', 'caab', 'cbaa', 'cbaa', 'caab', 'caba', 'aabc', 'aacb', 'abac', 'abca', 'acab', 'acba']))




    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

