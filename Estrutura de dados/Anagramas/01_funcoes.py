'''Revisão de funções

1. Abra o arquivo no IDLE (clique com o botão direito e 
selecione edit with IDLE).
(você pode voltar a usar outro ambiente depois, mas quero 
garantir o funcionamento simples dessa vez)

2. Clique Run>Run Module

3. No novo terminal que abrir, digite soma(1,2). O resultado deverá ser 3.
Experimente soma(4,5), soma(100,1), soma(-4,6). Não altere a função soma
que está no arquivo!
'''
def soma(a,b):
    resultado = a+b    #linha1
    return resultado   #linha2

'''
4. O que aconteceu foi o seguinte: quando você digita soma(1,2) naquele novo
terminal, a função soma é chamada. Ela guarda o valor 1 na variavel a e o
valor 2 na variavel b, e começa a executar os comandos da função.
Na linha 2, ela devolveu um número. Foi esse número que
foi impresso no terminal.

5. Primeiro erro comum: algumas pessoas não estão sabendo passar
números para as funções e estão "testando" elas como no exemplo abaixo.
O jeito certo de passar números para funções
é chamar a função colocando os números no parenteses,
como fizemos no terminal do run module

Você não precisa E NAO DEVE colocar na propria função
'''
def soma_zoada(a,b):
    #linha 0
    a=2 #linha 1
    b=5 #linha 2
    resultado = a+b    
    return resultado   

'''
6. Lá no terminal do run module, rode soma_zoada1(100,10), depois
soma_zoada(12,1). Ela sempre devolve o mesmo número!

7. O que está acontecendo ao rodar soma_zoada1(100,10)?
Na linha 0, a vale 100 e b vale 10. Mas nas linhas 1 e 2, nós 
colocamos 2 no a e 5 no b. Assim, colocamos 7 no resultado.
Resumindo: os números não entram na hora que você monta a função.
Entram depois, quando você for usar a função.

8. O segundo erro comum é usar input. Novamente, os números devem
entrar no parênteses ao chamar a função. Não de outra forma.

9. Uma coisa muito util é chamar uma função dentro de outra.
Não que o exemplo a seguir seja muito útil :P
'''

def soma3(a,b,c):
    dois_primeiros = soma(a,b)
    resultado = soma(dois_primeiros,c)
    return resultado
'''
10. Vá no terminal do run module, e experimente soma3(4,2,1),
soma3(9,3,10)...

11. Usando o que você relembrou até agora, escreva uma função 
quadrado que recebe um número e o eleva ao quadrado.
No momento, a função está errada. Corrija
'''
def quadrado(a):
    a = a**2
    return a
'''
12. Clique Run>Run Module de novo. Você tem que fazer
isso toda vez que alterar o arquivo, para o python carregar suas
alterações.

13. Teste no terminal do run module (chame: quadrado(2), 
. Depois, SEM ALTERAR O ARQUIVO, SO MEXENDO NO TERMINAL
DO RUN MODULE, quadrado(3)). 

14. Faça mais testes, a gosto.

15. Agora que você testou, se sua função parece OK, rode,
no terminal do run module, a função runTests (faça isso digitando
runTests())

16. Se a sua função estava dando respostas certas, sem você ter
que mudar nada dentro dela, talvez o seu erro seja
que você usou print(resposta) ao invés de return resposta

17. Mas, se deu certo, vou definir uma função que usa a sua
'''
def pitagoras(cate1, cate2):
    return raiz(quadrado(cate1)+quadrado(cate2))

import math
def raiz(n):
    return math.sqrt(n)

'''
17. Teste a função pitagoras, fazendo
pitagoras(3,4) 
pitagoras(4,3) -> os dois tem que dar 5
pitagoras(1,1) -> tem que dar raiz de 2. Confira na calc. do celular

se nao estiver dando certo, você se lembrou de testar sua
função quadrado com o runTests? Se nao, volte para o passo 15
(ou mesmo para o 13)
'''

'''
18. Agora, sem olhar o codigo acima, tente definir uma função
soma_dos_quadrados que receba dois numeros
e devolva a soma dos seus quadrados.
'''

def soma_dos_quadrados(a,b):
    a = a**2
    b = b**2
    soma = a+b
    return soma

'''
19. Faça o run module de novo e teste a sua função lá

20. Faça o runTests
'''



import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_quadrado(self):
        self.assertEqual(quadrado(2), 4)
        self.assertEqual(quadrado(-1), 1)
        self.assertEqual(quadrado(0), 0)
        self.assertEqual(quadrado(10), 100)
    
    def test_02_soma_dos_quadrados(self):
        self.assertEqual(soma_dos_quadrados(2,0), 4)
        self.assertEqual(soma_dos_quadrados(-1,1), 2)
        self.assertEqual(soma_dos_quadrados(0,0), 0)
        self.assertEqual(soma_dos_quadrados(10,20), 500)
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

