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

Por exemplo, para ver a raiz da arvore10, digite arvore10['raiz']

Para ver o numero da direita, digite arvore10['direita']['raiz']
'''

'''
Representar uma arvore vazia é bem fácil
'''

vazia = {}

'''
faça uma função em_ordem que recebe uma arvore, e retorna uma lista com 
todos os elementos da arvore em ordem

(dica: recursao ajuda bastante)
'''

ordem = []
def em_ordem(arvore):
    while arvore != {}:
        ordem.append(arvore['raiz'])
        if arvore['esquerda'] != {}:
            arvore = arvore['esquerda']
            return em_ordem(arvore)
        if arvore['direita'] != {}:
            arvore = arvore['direita']
            return em_ordem(arvore)
        return ordem
    else:
        return ordem

'''
Agora, façamos uma funcao pega_maior, que recebe uma arvore e retorna o maior
número na arvore (nao use a funcao em ordem! lembrando que ir "para a direita"
sempre aumenta o numero e ir "para a esquerda" diminui, a idéia é
simplesmente ir "para a direita" o máximo possível, sem nunca ir a esquerda)
'''

def pega_maior(arvore):
    while arvore['direita'] != {}: 
        arvore = arvore['direita']
    return arvore['raiz']    

'''
Agora, vamos fazer uma variacao de pega_maior.

Ao invés de retornar o número, queremos retornar o dicionario correspondente.

Ou seja, retornar algo como {'raiz':12,'esquerda'...} ao invés de 12.

Um detalhe: é importante que você não faça uma cópia do dicionário,
mas retorne o dicionário que de fato está sendo usado na arvore
'''
def pega_maior_no(arvore):
    while arvore['direita'] != {}:
        arvore = arvore['direita']
    return arvore

'''
O objetivo principal desse arquivo é fazer a remocao da arvore.

Para isso, precisamos saber alterar o conteudo de dicionarios.

Faça uma funcao que recebe um dicionario que tem as chaves
'raiz' e 'esquerda' e esvazia ele. Note que isso
NAO EH A MESMA COISA QUE RETORNAR UM DICIONARIO VAZIO.
Quando voce recebe uma variavel do tipo dicionario
(ou lista) e faz mudanças nela, todo mundo que conhecia a variavel
(inclusive a função que te chamou) vê as mudanças.

https://docs.python.org/3.5/library/stdtypes.html#mapping-types-dict (veja a funcao pop)
'''

def limpa(dicionario):
    dicionario.clear()
    return 'ok'

'''
Agora, vamos fazer outra funcao.

Ela recebe dois dicionarios, e deve copiar 'raiz', 'esquerda' e 'direita'
do segundo para o primeiro.

O retorno dela nao importa
'''
  
def copia(dicionario1, dicionario2):
    dicionario1['raiz'] = dicionario2['raiz']
    dicionario1['esquerda'] = dicionario2['esquerda']
    dicionario1['direita'] = dicionario2['direita']
    return 'ok'

'''
Agora, vamos fazer a função de remoção!

Primeiro, implementemos uma funcao remove relativamente simples,
depois vamos adicionando mais casos.

      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 

Por exemplo, o nó 30 é facil de remover,
é so alterar o dicionario {'raiz': 30, 'direita':{}, 'esquerda':{}}
para ser um dicionário vazio: {}

Vamos começar por ai: faça uma funcao remove, que recebe um nó
(um dicionário) e remove ele da arvore, supondo que ele nao tem 
filhos (que direita e esquerda sao dicionarios vazios)

Note que ela nao recebe a arvore, so o no. Vai dar tudo certo :)
'''
def remove(elemento):
    if (elemento['esquerda'] == {}) and (elemento['direita'] == {}):
        limpa(elemento)
        return 'pronto'
    if (elemento['esquerda'] == {}):
        subs = elemento['direita']
        elemento['direita'] = subs['direita']
        elemento['esquerda'] = subs['esquerda']
        elemento['raiz'] = subs['raiz']
        return 'ok'
    if (elemento['direita'] == {}):
        subs = elemento['esquerda']
        copia(elemento, subs)
        return 'xx'
    esquerda = elemento['esquerda']
    subs = pega_maior_no(esquerda)
    elemento['raiz'] = subs['raiz']
    remove(subs)
    return 'blz'
'''
Vamos adicionar um segundo caso à funcao remove:
Um cara que só tem um filho.


      10
        \
         20
        /  \
       12  30 

O 10 é fácil de remover. É só substituir sua raiz por 20,
sua esquerda pela esquerda que era do nó 20, e sua direita
pela direita que era do nó 20.

Altere a funcao remove. Ela ja funcionava no caso de nenhum
filho, e deve passar a funcionar no caso de um único filho
'''

'''
Por ultimo, temos o caso "feio", em que o nó a remover tem dois filhos.

Suponhamos que queremos remover o 10

      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 

Nesse caso, devemos:
    1. Pegar o maior nó a esquerda (no exemplo, o nó do 7)
    Ele é maior que todos os outros a esquerda do 10, 
    e menor que todos os caras à direita
    2. Sobreescrever o valor da raiz do 10 (no caso, de 10 para 7)
    3. Recursivamente, deletar o antigo "maior nó a esquerda" (no caso, o nó do 7)

Depois de fazer essa funcao completa, você deve passar do teste 8
'''

'''
Uma ultima função: dada uma arvore, gere uma lista dela "por andares".

Por exemplo,
      10
     /  \
    5    20
   /\   /  \
  2  7 12  30 

retornaria uma lista [10,5,20,2,7,12,30]
'''

def andares(arvore):
    return []

'''
Essas funcoes aqui eu vou usar, deixa elas quietas :P
'''
   

def insere(arvore,elemento):
    if 'raiz' not in arvore:
        arvore['raiz'] = elemento
        arvore['esquerda'] = {}
        arvore['direita'] = {}
        return arvore
    if arvore['raiz'] < elemento:
        insere(arvore['direita'],elemento)
    if arvore['raiz'] > elemento:
        insere(arvore['esquerda'],elemento)
    return arvore

def cria_simples(lista):
    arvore = {}
    for e in lista:
        insere(arvore,e)
    return arvore


ex1= {'direita': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 20}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 12}, 'raiz': 15}, 'esquerda': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 7}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 2}, 'raiz': 5}, 'raiz': 10}

ex2= {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 2}, 'raiz': 3}, 'raiz': 10} 

ex3 = {'direita': {'direita': {}, 'esquerda': {'direita': {}, 'esquerda': {}, 'raiz': 110}, 'raiz': 120}, 'esquerda': {'direita': {'direita': {}, 'esquerda': {}, 'raiz': 10}, 'esquerda': {}, 'raiz': 5}, 'raiz': 90}
import unittest

class TestStringMethods(unittest.TestCase):

    def test_00_em_ordem(self):
        self.assertEqual(em_ordem(ex1),[2,5,7,10,12,15,20])
        self.assertEqual(em_ordem(ex2),[2,3,10])
    
    def test_01_pega_maior(self):
        self.assertEqual(pega_maior(ex1),20)
        self.assertEqual(pega_maior(ex2),10)
        self.assertEqual(pega_maior(ex3),120)
    
    def test_02_pega_maior_no(self):
        self.assertEqual(pega_maior_no(ex1)['raiz'],20)
        self.assertEqual(pega_maior_no(ex2)['raiz'],10)
        self.assertEqual(pega_maior_no(ex3)['raiz'],120)
        self.assertTrue(pega_maior_no(ex3) is ex3['direita'])

    def test_03_limpa(self):
        a={'raiz':12,'esquerda':'nao tem biscoito'}
        limpa(a)
        self.assertEqual(a,{})


    def test_04_copia(self):
        a={'raiz':12,'esquerda':'nao tem biscoito', 'direita': 'ola'}
        b={'raiz':13,'esquerda':'tem biscoito'}
        c={}
        copia(c,a)
        self.assertEqual(a,c)
        self.assertFalse(a is c)
    


    def test_05_remove_simples(self):
        copia = cria_simples([10,5,20,2,7,12,30])
        arvore30 = copia['direita']['direita']
        remove(arvore30)
        self.assertEqual(copia,cria_simples([10,5,20,2,7,12]))

    def test_06_remove_simples2(self):
        copia = cria_simples([10,3,2])
        remove(copia)
        self.assertEqual(copia,cria_simples([3,2]))



    def test_07_remove_complicado(self):
        copia = cria_simples([10,5,20,2,7,12,30])
        no5 = copia['esquerda']
        remove(no5)
        self.assertEqual(copia,cria_simples([10,20,2,7,12,30]))
        no2 = copia['esquerda']
        remove(no2)
        self.assertEqual(copia,cria_simples([10,20,7,12,30]))
        no7 = copia['esquerda']
        remove(no7)
        self.assertEqual(copia,cria_simples([10,20,12,30]))
        remove(copia)
        self.assertEqual(copia,cria_simples([20,12,30]))
        remove(copia['esquerda'])
        self.assertEqual(copia,cria_simples([20,30]))
        remove(copia['direita'])
        self.assertEqual(copia,cria_simples([20]))
        remove(copia)
        self.assertEqual(copia,{})

    def test_08_mais_remove(self):
        copia = cria_simples([10,5,20,2,7,12,30,40,50])
        remove(copia)
        self.assertEqual(copia,cria_simples([7,5,20,2,12,30,40,50]))
        no30 = copia['direita']['direita']
        remove(no30)
        self.assertEqual(copia,cria_simples([7,5,20,2,12,40,50]))


    def test_09_por_andares(self):
        self.assertEqual(por_andares(ex1),[10,5,15,2,7,12,20])
        self.assertEqual(por_andares(arvore10),[10,5,20,2,7,12,30])
        self.assertEqual(por_andares(ex2),[10,3,2])



        
        

    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

