from random import randint

# 1) crie uma função "soma" que recebe dois numeros e retorna sua soma
def soma(a,b):
    return a+b

#dica: a seguinte função recebe dois numero e retorna seu produto
#  def produto(a,b):
#      return a*b
#

# 2) crie uma função "lista_completa" que receba um número N, e retorne uma lista com todos os números de 0 a N.
# por exemplo, se ela receber 12, deve retornar 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def lista_completa(N):
    lista = []
    contador = 0
    while (contador <= N):
        lista.append(contador)
        contador = contador + 1
    return lista

#dica: para criar uma lista com o nome "numeros", usamos
#numeros=[]
#para adicionar um numero J em uma lista, usamos numeros.append(J)

# 3) crie uma função "lista_pulos" que receba um número N, e retorne uma lista com N numeros, em ordem, mas que aleatóriamente "pule" alguns.
# A diferença entre um número da lista e o próximo nunca deve ser maior do que 2. O primeiro numero da lista sempre deve ser 0.
# Por exemplo, lista_pulos(5) pode retornar [0,1,3,4,6] ou [0,2,4,6,7], mas não [0,2,5,6,7] porque a diferença entre 2 e 5 é grande demais
# Note o "aleatoriamente" significa que lista_pulos(5) pode retornar listas diferentes, quando chamada várias vezes. Isso é esperado.
import random
def lista_pulos(N):
    lista = []
    cont = 0
    while(len(lista) < N):
        lista.append(cont)
        contador = cont + randint(1,2)
    return lista

#dica1: para gerar um numero aleatório entre 0 e 1, voce deve usar random.randint(0,1). Nao esqueça do import random!
#dica2: para ver o comprimento de uma lista "numeros", voce pode usar len(numeros)

#4) crie uma função "busca simples" que recebe uma lista ordenada LISTA e um numero BUSCAR, verifica os elementos da lista UM A UM para ver se são iguais a BUSCAR até achar o número BUSCAR ou um numero maior.
# Ela deve retornar duas respostas: True ou False (dependendo se buscar está na lista ou não) e o número de passos que ela deu (o numero de elementos que ela comparou com BUSCAR)
# Por exemplo, busca_simples([1,4,5],4) retornaria (True,2)
# Já busca_simples([1,4,5],6) retornaria (False,3)
# Já busca_simples([1,3,4,5],2) retornaria (False,2)
def busca_simples(lista,buscar):
    return (False,42)
#dica voce pode usar lista_pulos para testar sua funcao

#5) (começo da busca binária)
# Conforme explicado em sala, a busca binária busca um número BUSCA em uma lista ordenada. Primeiro, olha para o meio da lista. Se achou o número, retorna True. Se não, entre procurar nos numeros anteriores ao meio ou nos posteriores.
# Faça uma funçao bb_inicio que, dados uma lista e um número a buscar, retorna:
# True se o numero está bem no meio
# A lista esquerda se o número é menor que o do meio
# A lista direita, se o número é maior que o do meio.
# Exemplo: bb_inicio([0,1,3,5,8],3) retorna True 
# Exemplo: bb_inicio([0,1,3,5,8],2) retorna [0,1]
# Exemplo: bb_inicio([0,1,3,5,8],5) retorna [5,8]
# Se a lista tiver um número par de elementos, arredonde para cima ao escolher o meio
# Exemplo: bb_inicio([0,2,5,6],3) compararia 3 com 5. Como 3 é menor que 5, retorna [0,2]
def bb_inicio(lista,buscar):
    return 42
#dica: para quebrar uma lista, procure "list slicing python" no google

#6)Implemente a busca binária:
# uma funcao busca_binaria, que recebe uma lista ordenada "lista" e um numero "buscar", e retorna True se o numero está na lista e False caso contrário.
# ela também deve retornar um segundo número: o número de comparaçõs entre "buscar" e o "número do meio"
# por exemplo, busca_binaria([1,2,3,4,5],3) retorna (True,1)
# por exemplo, busca_binaria([1,2,3,4,5],0) retorna (False,3)
def busca_binaria(lista,buscar):
    return (False,42)

#7)(Extra) Implemente a busca binaria, usando indices ao invés de list slicing.
# Ou seja, ao invés de ir atualizando a lista, mantenha dois numeros (inicio e fim) que representam o inicio e o fim da lista.
def busca_binaria_indices(lista,buscar):
    return (False,42)
#lista com pulos: produz listas válidas (inclusive atenção ao:: N) e nao produz sempre a mesma




    
testes = [([0, 1, 3, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 21, 22], 3, [0, 1, 3, 4, 6, 8, 10], (True, 3), (True, 4)), ([0, 2, 4, 6, 8, 9, 11, 12, 13, 14, 16, 18, 20, 21, 23], 14, [13, 14, 16, 18, 20, 21, 23], (True, 10), (True, 3)), ([0, 1, 3, 4, 5, 6, 8, 9, 11, 13, 14, 15, 17, 19, 21], 11, [11, 13, 14, 15, 17, 19, 21], (True, 9), (True, 4)), ([0, 2, 4, 6, 7, 8, 9, 11, 13, 15, 17, 19, 21, 22, 23], 11, True, (True, 8), (True, 1)), ([0, 1, 2, 4, 5, 7, 9, 10, 12, 13, 14, 15, 16, 17, 19], 3, [0, 1, 2, 4, 5, 7, 9], (False, 4), (False, 4)), ([0, 1, 3, 5, 6, 7, 9, 10, 12, 13, 15, 16, 17, 19, 20], 1, [0, 1, 3, 5, 6, 7, 9], (True, 2), (True, 3)), ([0, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18], 8, [0, 2, 3, 4, 5, 7, 8], (True, 7), (True, 4)), ([0, 2, 4, 6, 8, 10, 11, 12, 14, 16, 18, 20, 21, 23, 25], 2, [0, 2, 4, 6, 8, 10, 11], (True, 2), (True, 3)), ([0, 2, 3, 5, 6, 7, 9, 10, 12, 14, 16, 17, 18, 20, 21], 2, [0, 2, 3, 5, 6, 7, 9], (True, 2), (True, 3)), ([0, 2, 4, 6, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 21], 10, [0, 2, 4, 6, 8, 9, 11], (False, 7), (False, 4)), ([0, 1, 3, 4, 6, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22], 1, [0, 1, 3, 4, 6, 7, 8], (True, 2), (True, 3)), ([0, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 20], 13, [9, 11, 12, 14, 16, 18, 20], (False, 12), (False, 4)), ([0, 1, 3, 4, 5, 7, 8, 9, 11, 13, 14, 16, 18, 19, 21], 6, [0, 1, 3, 4, 5, 7, 8], (False, 6), (False, 4)), ([0, 1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14, 16, 17], 15, [10, 11, 12, 13, 14, 16, 17], (False, 14), (False, 4)), ([0, 2, 4, 6, 8, 9, 10, 12, 14, 15, 17, 19, 21, 22, 23], 3, [0, 2, 4, 6, 8, 9, 10], (False, 3), (False, 4)), ([0, 2, 3, 5, 6, 7, 9, 11, 12, 13, 15, 16, 17, 18, 20], 10, [0, 2, 3, 5, 6, 7, 9], (False, 8), (False, 4)), ([0, 2, 4, 5, 7, 9, 10, 12, 13, 15, 17, 19, 20, 22, 23], 4, [0, 2, 4, 5, 7, 9, 10], (True, 3), (True, 4)), ([0, 2, 4, 6, 7, 8, 9, 10, 12, 14, 15, 17, 19, 21, 23], 0, [0, 2, 4, 6, 7, 8, 9], (True, 1), (True, 4)), ([0, 1, 2, 3, 5, 7, 9, 11, 12, 13, 15, 17, 19, 21, 22], 10, [0, 1, 2, 3, 5, 7, 9], (False, 8), (False, 4)), ([0, 2, 4, 5, 7, 9, 11, 12, 13, 14, 15, 17, 18, 20, 22], 8, [0, 2, 4, 5, 7, 9, 11], (False, 6), (False, 4)), ([0, 1, 3, 4, 6, 8, 10, 11, 13, 15, 16, 18, 20, 21, 23], 7, [0, 1, 3, 4, 6, 8, 10], (False, 6), (False, 4)), ([0, 1, 3, 5, 7, 9, 10, 12, 14, 15, 17, 18, 19, 20, 21], 0, [0, 1, 3, 5, 7, 9, 10], (True, 1), (True, 4)), ([0, 1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 16, 18, 19], 13, [9, 11, 12, 14, 16, 18, 19], (False, 12), (False, 4)), ([0, 1, 3, 5, 6, 7, 8, 10, 11, 13, 15, 16, 18, 19, 21], 1, [0, 1, 3, 5, 6, 7, 8], (True, 2), (True, 3)), ([0, 2, 4, 6, 8, 10, 12, 13, 14, 15, 16, 17, 19, 20, 22], 7, [0, 2, 4, 6, 8, 10, 12], (False, 5), (False, 4)), ([0, 1, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 18, 20, 21], 9, True, (True, 8), (True, 1)), ([0, 2, 3, 4, 5, 6, 8, 9, 11, 13, 14, 16, 18, 20, 21], 1, [0, 2, 3, 4, 5, 6, 8], (False, 2), (False, 4)), ([0, 2, 4, 6, 8, 10, 12, 13, 15, 17, 19, 21, 22, 24, 25], 2, [0, 2, 4, 6, 8, 10, 12], (True, 2), (True, 3)), ([0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 16, 18, 19, 21, 23], 14, [12, 14, 16, 18, 19, 21, 23], (True, 10), (True, 3))]
       
def testa_bb_inicio():
    for teste in testes:
       lista = teste[0]
       elemento = teste[1]
       inicio = teste[2]
       simples = teste[3]
       binaria = teste[4]
       resultado = bb_inicio(lista,elemento)
       desejado = inicio
       if resultado != desejado:
          print('retornou', resultado, "para", lista, elemento, "esperavamos", desejado)
          return False
       return True

def testa_simples():
    for teste in testes:
       lista = teste[0]
       elemento = teste[1]
       inicio = teste[2]
       simples = teste[3]
       binaria = teste[4]
       resultado = busca_simples(lista,elemento)
       desejado = simples
       if resultado != desejado:
          print('retornou', resultado, "para", lista, elemento, "esperavamos", desejado)
          return False
       return True

def testa_binaria():
    for teste in testes:
       lista = teste[0]
       elemento = teste[1]
       inicio = teste[2]
       simples = teste[3]
       binaria = teste[4]
       resultado = busca_binaria(lista,elemento)
       desejado = binaria
       if resultado != desejado:
          print('retornou', resultado, "para", lista, elemento, "esperavamos", desejado)
          return False
       return True


def testa_soma():
    for i in range(1,100):
        a = randint(1,100)
        b = randint(1,100)
        if soma(a,b) != a+b:
            print("parametros",a,b,"sua soma",soma(a,b))
            return False
    return True
            
def testa_lista_completa():
    for i in range(1,100):
        a = randint(1,20)
        lista = lista_completa(a)
        if (len(lista) != a+1):
            print("parametro", a,"sua lista",lista_completa(a))
            return False
        if (lista[0] != 0):
            print("parametro", a,"sua lista",lista_completa(a))
            return False
        for i in range(0,a):
            if lista[i+1] != lista[i]+1:
               print("parametro", a,"sua lista",lista_completa(a))
               return False
    return True
            
def testa_lista_pulos():
    for i in range(1,100):
        a = randint(1,20)
        lista = lista_pulos(a)
        if (len(lista) != a):
            print("parametro", a,"sua lista",lista)
            return False
        if (lista[0] != 0):
            print("parametro", a,"sua lista",lista)
            return False
        for i in range(0,a-1):
            if lista[i+1] not in (lista[i]+1,lista[i]+2):
               print("parametro", a,"sua lista",lista)
               return False
    return True
