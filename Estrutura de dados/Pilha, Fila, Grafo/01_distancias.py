'''
podemos descrever um "mapa" de salas de um jogo
a da seguinte forma: montamos uma matriz nxn (onde
n é o número de salas do jogo) e marcamos 1 nas posicoes
em que há uma porta, 0 caso contrário

Ou seja, se existe uma porta entre a sala 3 e a 5,
a posicao matriz[3][5] será 1. Se não existe, será 0.
'''

mapinha = [
 [0, 1, 1],
 [1, 0, 0],
 [1, 0, 0]]

'''
por exemplo, essa variavel diz que a sala 0 tem porta para a sala 1
e a sala 2, mas as salas 1 e 2 nao tem porta entre si.
 voce pode ver isso ao digitar (no terminal do run module)
 mapinha[0][1] (que é essa posicao aqui
mapinha = 
[[0, X, 1],
 [1, 0, 0],
 [1, 0, 0]]
 e vale 1)
'''

'''
A primeira funcao que vamos fazer recebe um mapa e duas salas,
e retorna True se existe uma porta entre elas (False caso contrario)
'''

def tem_porta(mapa, sala1, sala2):
    if mapa[sala1][sala2] == 1:
        return True
    else:
        return False

'''
A segunda funcao retorna o numero de salas de um mapa
'''

def salas(mapa):
    total = len(mapa)
    return total



'''
Agora, vamos manipular filas (representadas atraves de listas
de python)

Para inserir, vamos inserir no fim da fila, usando lista.append

Para remover, vamos remover do começo da fila, usando lista.pop(0)

Primeiramente, crie uma funcao insere, que recebe uma fila e um elemento,
e retorna a fila com esse novo elemento inserido
'''

def insere(fila,elemento):
    fila.append(elemento)
    return fila

'''
Agora, crie a funcao remove, que recebe uma fila, e retorna 
duas coisas: a fila (sem o primeiro elemento) 
e o primeiro elemento
'''

def remove(fila):
    last = fila.pop(0)
    return fila,last

'''
Agora, vamos implementar uma funcao distancias, usando a ideia
discutida na aula passada.

Ela recebe um grafo (um mapa como o mapinha) e dois vertices,
e devolve a distancia entre eles.

A distancia é o menor numero de portas possivel, quando a gente
vai de uma das salas pra outra
(ou, dito na linguagem dos grafos:
    o numero de arestas do menor caminho entre os dois vertices)

relembrando: a ideia é usar a fila.
voce insere o primeiro elemento (um dos vertices)
depois remove um elemento da lista, adiciona os vizinhos
e marca a distancia dos vizinhos.

no fim das contas, retorna a distancia pedida.
'''

def vizinho(mapa,sala):
    sides = mapa[sala]
    resposta = []
    for i in range(len(sides)):
        if sides[i] == 1:
            resposta.append(i)
    return resposta

            
def distancia(mapa,sala1, sala2):
    steps = {}
    steps[sala1] = 0
    fila = []
    fila.append(sala1)
    while (len(fila) > 0):
        atual = fila.pop(0)
        prox = vizinho(mapa,atual)
        for v in prox:
            if v not in steps:
                fila.append(v)
                steps[v] = steps[atual] + 1
    return steps[sala2]











import unittest

vazio = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        ]

completo = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        ]

linha = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        ]

estrela = [
        [0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        ]

ciclo = [
        [0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0],
        ]

bobo = [[0]]

class TestGraph(unittest.TestCase):



    
    
    def test_00_tem_porta(self):
        self.assertTrue(tem_porta(completo,1,2))
        self.assertTrue(tem_porta(completo,2,3))
        self.assertFalse(tem_porta(vazio,1,2))
        self.assertTrue(tem_porta(linha,1,2))
        self.assertFalse(tem_porta(linha,1,3))

    def test_01_salas(self):
        self.assertEqual(salas(completo),5)
        self.assertEqual(salas(linha),5)
        self.assertEqual(salas(ciclo),6)
        self.assertEqual(salas(estrela),6)
        self.assertEqual(salas(vazio),7)
        self.assertEqual(salas(bobo),1)
    
    def test_02_insere(self):
        self.assertEqual(insere([1,2,3],4), [1,2,3,4])
        self.assertEqual(insere([1]*15,1), [1]*16)
        self.assertEqual(insere([],12), [12])
    
    def test_03_remove(self):
        self.assertEqual(remove([1,2,3]), ([2,3],1))
        self.assertEqual(remove([2,3]), ([3],2))
        self.assertEqual(remove([2,3]*5), ([3]+[2,3]*4,2))
        self.assertEqual(remove([2]), ([],2))
    
    def test_04_distancia(self):
        self.assertEqual(distancia(completo,1,2),1)
        self.assertEqual(distancia(linha,1,3),2)
        self.assertEqual(distancia(linha,0,3),3)
        self.assertEqual(distancia(ciclo,0,1),1)
        self.assertEqual(distancia(ciclo,0,2),2)
        self.assertEqual(distancia(ciclo,0,3),3)
        self.assertEqual(distancia(ciclo,0,4),2)
        self.assertEqual(distancia(ciclo,0,5),1)
    
    def test_05_distancia_mesmo_vertice(self):
        self.assertEqual(distancia(completo,1,1),0)

    def test_06_distancia_mesmo_vertice_ex_bobo(self):
        self.assertEqual(distancia(bobo,0,0),0)
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGraph)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

