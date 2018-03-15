'''rode essa funcao no começo da aula,
ela só está aqui para te lembrar de como o range funciona'''
def dica():
    for i in range(0,10):
        print(i)


'''implemente uma funcao troca, 
que recebe uma lista e duas posicoes,
e troca os valores das duas posicoes. 
Por exemplo, troca(['a','b','c'],0,2) deve retornar ['c','b','a']'''
def troca(lista,pos1,pos2):
    v1 = lista[pos1]
    v2 = lista[pos2]
    lista[pos1] = v2
    lista[pos2] = v1
    return lista

'''implemente uma funcao indice_menor, 
que recebe uma lista e devolve o indice do seu menor elemento. 
Se houver mais de um menor elemento, retorna o indice menor.
por exemplo, a=[2,3,1] indice_menor(a) retorna 2, pois a[2]==1'''
def indice_menor(lista):
    i_menor = 0
    for i in range(len(lista)):
        if lista[i] < lista[i_menor]:
            i_menor = i
    return i_menor

'''implemente uma funcao indice_menor2, 
que recebe uma lista e um numero de inicio, 
e devolve o indice do menor elemento do inicio para frente. 
Se houver mais de um menor elemento, retorne o indice menor.
por exemplo, a=[1,4,3] indice_menor(a,0) retorna 0, pois a[0]==1
por exemplo, a=[1,4,3] indice_menor(a,1) retorna 2, pois a[2]==3'''
def indice_menor2(lista,primeiro):
    i_menor = primeiro
    for i in range(primeiro,(len(lista))):
        if lista[i] < lista[i_menor]:
            i_menor = i
    return i_menor

'''implemente uma função selectionSort, 
que recebe uma lista e devolve uma lista ordenada. 

NAO USE O METODO lista.sort(). 
ISSO NAO SERA CONSIDERADO UMA SOLUCAO VALIDA.

Selection sort é o algoritmo que percorre a lista, 
acha o menor elemento e coloca na posicao 0. 
Depois, percorre a lista novamente, partindo da posicao 1, 
acha o menor elemento e o coloca na posicao 1, 
e vai fazendo isso até ordenar a lista

Veja: https://visualgo.net/bn/sorting, opcao SEL ou SELECTION SORT
'''
def selectionSort(lista):
    swap = list(range(0,len(lista)))
    for pos in swap:
        i_menor = indice_menor2(lista,pos)
        troca(lista,i_menor,pos)
    return lista

'''
implemente uma função bubbleSort, 
que recebe uma lista e devolve: 
* uma lista ordenada 
* o numero de trocas que o algoritmo fez. 

NAO USE O METODO lista.sort(). 
ISSO NAO SERA CONSIDERADO UMA SOLUCAO VALIDA.

bubble sort é o algoritmo que percorre a lista, 
olhando para cada elemento e o elemento seguinte,
e trocando quando adequado.

Ao comparar, por exemplo, a[4] e a[5], se a[4] for maior
o algoritmo troca os dois.

O algoritmo faz isso, para o par (0,1), depois (1,2), depois (2,3) 
até o fim da lista (o par (n-1,n))

Depois, ele faz isso novamente. Ele percorre toda a lista, 
dessa forma, n vezes.

Lembre-se de contar as trocas (como  
a troca entre a[4] e a[5] que demos de exemplo)

Veja: https://visualgo.net/bn/sorting, opcao BUB ou BUBBLE SORT
'''

def bubbleSort(lista):
    inversions = 0
    for i in range(0,len(lista)):
        for i in range(0,len(lista)-1):
            if(lista[i] > lista[i+1]):
                   troca(lista,i,i+1)
                   inversions += 1
                   
    return lista,inversions

'''DESAFIO
Entenda e implemente o algoritmo insertionSort
Ele deve receber uma lista e retornar uma lista ordenada.
veja: INS ou INSERTION SORT no site visualgo
'''

def insertionSort(lista):
    return lista



import unittest

class TestStringMethods(unittest.TestCase):
   
    def test_00_troca(self):
        self.assertEqual(
          troca([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],5,6), 
          [3,44,38,5,47,36,15,26,27,2,46,4,19,50,48])
        self.assertEqual(
          troca([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],5,5), 
          [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48])
        self.assertEqual(
          troca([3,44],0,1), 
          [44,3])
        self.assertEqual(
          troca([3],0,0), 
          [3])

    def test_01_indice_menor(self):
        self.assertEqual(
          indice_menor([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          9)
        self.assertEqual(
          indice_menor([3,44,38,5,47,15,36,26,27,46,4,19,50,48]), 
          0)
        self.assertEqual(
          indice_menor([44,38,5,47,15,36,26,27,46,4,19,50,48]), 
          9)
    
    def test_02_indice_menor2(self):
        self.assertEqual(
          indice_menor2([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],0), 
          9)
        self.assertEqual(
          indice_menor2([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],9), 
          9)
        self.assertEqual(
          indice_menor2([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],10), 
          11)
    
    def test_03_selection(self):
        self.assertEqual(
          selectionSort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
        self.assertEqual(
          selectionSort([46,1,18,35,18,9,6,26,47,24,4,29,38,26,30,23,49,5,44,6]), 
          [1, 4, 5, 6, 6, 9, 18, 18, 23, 24, 26, 26, 29, 30, 35, 38, 44, 46, 47, 49])
        self.assertEqual(
          selectionSort( [1,5,15,20,18,30,35,35,38,45,47,48,50]), 
          [1,5,15,18,20,30,35,35,38,45,47,48,50])

    def test_05_insertion(self):
        self.assertEqual(
          insertionSort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
        self.assertEqual(
          insertionSort([46,1,18,35,18,9,6,26,47,24,4,29,38,26,30,23,49,5,44,6]), 
          [1, 4, 5, 6, 6, 9, 18, 18, 23, 24, 26, 26, 29, 30, 35, 38, 44, 46, 47, 49])
        self.assertEqual(
          insertionSort( [1,5,15,20,18,30,35,35,38,45,47,48,50]), 
          [1,5,15,18,20,30,35,35,38,45,47,48,50])

    def test_04_bubblesort(self):
        self.assertEqual(
          bubbleSort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          ([2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50],44))
        self.assertEqual(
          bubbleSort([46,1,18,35,18,9,6,26,47,24,4,29,38,26,30,23,49,5,44,6]), 
          ( [1, 4, 5, 6, 6, 9, 18, 18, 23, 24, 26, 26, 29, 30, 35, 38, 44, 46, 47, 49] ,85))
        self.assertEqual(
          bubbleSort( [1,5,15,20,18,30,35,35,38,45,47,48,50]), 
          ([1,5,15,18,20,30,35,35,38,45,47,48,50],1))
    




    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

