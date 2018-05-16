#renomear para ter extensão .py

import unittest



#faça uma função que recebe uma lista de números e retorna a média.
#ou seja, soma todos os números e divide pela quantidade de numeros

def media(lista):
    count = 0
    total = 0
    while count < len(lista):
        total += lista[count]
        count += 1
    return total/len(lista)

#faça uma função que acrescenta o proximo numero a uma lista.
#por exemplo cresce([7,8]) deve devolver [7,8,9]
def cresce(lista):
    finder = len(lista) - 1
    number = lista[finder] + 1
    lista.append(number)
    return lista

#faça uma função que cria um baralho.
#ela nao recebe nada e retorna uma lista.
#os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)
#as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
#O J de ouros, por exemplo, é representado pela string 'Jo'. 
#Assim 'Jo' é um dos elementos que deve aparecer na lista
def cria_baralho():
    baralho = []
    return  baralho

#Faça uma função que recebe uma lista, 
#e retorna todos os valores dessa lista que estao acima da média.
# Por exemplo, considerando [1,2,3,4,5], temos média 3. 
# Assim acima_da_media([1,2,3,4,5]) deve retornar a lista [4,5]
# Voce pode usar a sua funçao de média, que implementou antes
def acima_da_media(lista):
    resp = []
    count1 = 0
    total = 0
    while count1 < len(lista):
        total += lista[count1]
        count1 += 1
    media = total/len(lista)
    for c in lista:
        if lista[c] > media:
            resp.append(lista[c])
    return resp

# Uma loja está fazendo uma liquidaçao.
# A funçao liquidacao receberá duas listas. 
# Uma contém preços (em reais) e a outra descontos (tb em reais)
# Retorne uma terceira lista, dos preços já com desconto.
# Assim, por exemplo, liquidacao([2,4],[0,3]) 
# é uma situação em que o produto de preço 2 tem 0 reais de desconto 
# e o produto de preço 4 tem 3 reais de desconto
# A função deve retornar a lista [2,1]
def  liquidacao(precos,descontos):
    precos_finais = []
    return precos_finais

# Faça uma função que monta uma lista de compras
# Ela recebe uma lista e devolve uma string
# por exemplo, lista_de_compras(['agua','refri', 'oleo' ,'sal'])
# deve devolver a string 'agua, refri, oleo e sal'
# atençao: 
# no começo, os itens devem vir separados de ', ' 
# (virgula depois espaço)
# o ultimo item deve vir separado do penultimo por ' e '
# (espaço, depois a letra 'e', depois outro espaço)
# cuidado com listas de 1 ou 2 elementos!
def lista_de_compras(lista):
    return 'banana, leite e queijo'

#faça uma funcao que recebe uma string e troca os 'a' por 'q'
# ou seja, se ela receber 'agua', devolve 'qguq'
def lingua_do_q(string):
    return 'essq string nqo fqz muito sentido'

#faça uma funçao que recebe uma string e um dicionario,
#e troca as letras da string de acordo com o codigo do dicionário
# por exemplo, se o dicionario leva 'a' para 'q',
#a funcao deve trocar 'a' por 'q'
# a funcao devolve a string com as trocas
def codigo_secreto(string,codigo):
    return 'essq string nqo fqz muito sentido'

#faça uma funcao que conta as letras de uma string
#por exemplo, 'banana' tem 3 letras 'a'
# a funcao recebe uma string e devolve um dicionário
# por exemplo, conta_letras('banana') devolve {'b':1,'a':3,'n':2}
def conta_letras(string):
    dicti = {}
    return dicti

#faça uma funcao que decide se duas funções sao "embaralhamentos"
#uma da outra. 
#por exemplo, 'banana' e 'nabana' tem as mesmas letras, so muda
# a ordem. Dizemos que sao anagramas.
# note que a quantidade de cada letra importa: 'abb' e 'aab' 
# nao sao anagramas.
# a funcao deve recber duas strings e retornar True se elas sao
# anagramas, False caso contrário
# DICA: voce pode usar sua funcao de contar letras
def anagrama(string1,string2):
    return False



class TestPartOne(unittest.TestCase):

    def test_01_ola_fulano(self):
        self.assertEqual(ola_fulano('joao','sabio'),
                         'ola joao, te acho sabio')
        self.assertEqual(ola_fulano('matheus','tolo'),
                         'ola matheus, te acho tolo')



    def test_02_relogio_segundos(self):
        self.assertEqual(relogio_segundos(3661),
                         '1 h, 1 min e 1 seg')
        self.assertEqual(relogio_segundos(3601),
                         '1 h, 0 min e 1 seg')
        self.assertEqual(relogio_segundos(3660),
                         '1 h, 1 min e 0 seg')
        self.assertEqual(relogio_segundos(3600),
                         '1 h, 0 min e 0 seg')
        self.assertEqual(relogio_segundos(61),
                         '0 h, 1 min e 1 seg')
        self.assertEqual(relogio_segundos(1),
                         '0 h, 0 min e 1 seg')
        self.assertEqual(relogio_segundos(60),
                         '0 h, 1 min e 0 seg')
        self.assertEqual(relogio_segundos(0),
                         '0 h, 0 min e 0 seg')

    def test_03_maximo(self):
        self.assertEqual(maximo(1,2,3),
                         3)
        self.assertEqual(maximo(2,3,1),
                         3)
        self.assertEqual(maximo(3,2,1),
                         3)
        self.assertEqual(maximo(3,2,2),
                         3)
        self.assertEqual(maximo(1,1,4),
                         4)
    def test_04_conta_iguais(self):
        self.assertEqual(conta_iguais(1,2,3),'diferentes')
        self.assertEqual(conta_iguais(1,1,3),'dois iguais')
        self.assertEqual(conta_iguais(1,3,1),'dois iguais')
        self.assertEqual(conta_iguais(3,1,1),'dois iguais')
        self.assertEqual(conta_iguais(3,3,3),'todos iguais')
    def test_05_senha_boa(self):
        self.assertEqual(senha_boa('banana'),
                         False)
        self.assertEqual(senha_boa('banana1A'),
                         True)
        self.assertEqual(senha_boa('1Aa'),
                         False)
        self.assertEqual(senha_boa('1111Aa'),
                         False)
        self.assertEqual(senha_boa('1234567890'),
                         False)
        self.assertEqual(senha_boa('123456789a'),
                         False)
        self.assertEqual(senha_boa('123456789A'),
                         False)
        self.assertEqual(senha_boa('abcdefghA'),
                         False)
        self.assertEqual(senha_boa('abcdefgh1'),
                         False)
        self.assertEqual(senha_boa('abcdefgh'),
                         False)

    def test_06_dois_resultados(self):
        self.assertEqual(dois_resultados(0),
                         (0,0))
        self.assertEqual(dois_resultados(1),
                         (1,1))
        self.assertEqual(dois_resultados(-1),
                         (-1,1))
        self.assertEqual(dois_resultados(2),
                         (2,4))
    
    def test_07_quatro_resultados(self):
        self.assertEqual(quatro_resultados(0),
                         (0,0,0,0))
        self.assertEqual(quatro_resultados(1),
                         (1,1,1,1))
        self.assertEqual(quatro_resultados(4),
                         (2,4,8,16))
        self.assertEqual(quatro_resultados(9),
                         (3,9,27,81))

class TestPartTwo(unittest.TestCase):

    def test_08_media(self):
        self.assertEqual(media([1]),
                         1)
        self.assertEqual(media([1,2]),
                         1.5)
        self.assertEqual(media([1,2,3]),
                         2)

    def test_09_cresce(self):
        self.assertEqual(cresce([1]),
                         [1,2])
        self.assertEqual(cresce([5]),
                         [5,6])
        self.assertEqual(cresce([5,6]),
                         [5,6,7])
        self.assertEqual(cresce([5,6,7,8,9]),
                         [5,6,7,8,9,10])

    def test_10_cria_baralho(self):
        baralho_correto = set(['Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ae', '2e', '3e', '4e', '5e', '6e', '7e', '8e', '9e', '10e', 'Je', 'Qe', 'Ke', 'Ao', '2o', '3o', '4o', '5o', '6o', '7o', '8o', '9o', '10o', 'Jo', 'Qo', 'Ko', 'Ap', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', 'Jp', 'Qp', 'Kp'])
        baralho_gerado = set(cria_baralho())
        self.assertEqual(baralho_gerado,baralho_correto)

    def test_11_acima_da_media(self):
        self.assertEqual(set(acima_da_media([1,2,3])),{3})
        conj_vazio = set()
        self.assertEqual(set(acima_da_media([2,2,2])),conj_vazio)
        self.assertEqual(set(acima_da_media([-2,0,1])),{0,1})

       
    def test_12_liquidacao(self):
        precos=[10,10,10],[0],[10,20,30],[1,2,3,4]
        descontos=[1,1,1],[0],[9,8,7],[1,1,1,1]
        final=[9,9,9],[0],[1,12,23],[0,1,2,3]
        for i in range(0,len(precos)):
            self.assertEqual(liquidacao(precos[i],descontos[i])
                                ,final[i])

    def test_13_lista_de_compras(self):
        listas = [['abacaxi'],['abacaxi','morango'],['abacaxi','morango','frango']]
        listas.append([str(i) for i in range(10)])
        respostas = 'abacaxi', 'abacaxi e morango', 'abacaxi, morango e frango','0, 1, 2, 3, 4, 5, 6, 7, 8 e 9' 
        for i in range(len(listas)):
             self.assertEqual(lista_de_compras(listas[i]),
                                   respostas[i])


class TestPartThree(unittest.TestCase):

    def test_14_lingua_do_q(self):
        palavras='','aaa','abcdea'
        pqlqvrqs='','qqq','qbcdeq'
        for i in range(len(palavras)):
             self.assertEqual(lingua_do_q(palavras[i]),
                                   pqlqvrqs[i])

    def test_15_codigo_secreto(self):
        testes=(('abc',{'a':'a','b':'d','c':'c'},'adc'),
                ('abc',{'a':'a','c':'a','b':'x'},'axa'),
                ('',{'c':'a'},''))
        for teste in testes:
             self.assertEqual(codigo_secreto(teste[0],teste[1]),
                                   teste[2])
    def test_16_codigo_secreto_dicionario_incompleto(self):
        testes=(('abc',{'b':'d'},'adc'),
                ('abc',{'c':'a','b':'x'},'axa'),
                ('',{'c':'a'},''))
        for teste in testes:
             self.assertEqual(codigo_secreto(teste[0],teste[1]),
                                   teste[2])

    def test_17_conta_letras(self):
        testes = [('banana',{'b':1,'a':3,'n':2}),
                  ('nabana',{'b':1,'a':3,'n':2}),
                  ('abb',{'b':2,'a':1}),
                  ('baa',{'b':1,'a':2}),
                  ('',{})
                  ]
        for teste in testes:
             self.assertEqual(conta_letras(teste[0]),
                                   teste[1])


    
    def test_18_verifica_anagrama(self):
        self.assertEqual(anagrama('banana','nabana'),True)
        self.assertEqual(anagrama('banaaa','nabana'),False)
        self.assertEqual(anagrama('banana','nabann'),False)
        self.assertEqual(anagrama('abb','bba'),True)
        self.assertEqual(anagrama('abb','aab'),False)
        self.assertEqual(anagrama('abab','baba'),True)
        self.assertEqual(anagrama('',''),True)
        self.assertEqual(anagrama('','a'),False)
        self.assertEqual(anagrama('a',''),False)

        


def runTests1():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartTwo)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

def runTests2():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartThree)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


