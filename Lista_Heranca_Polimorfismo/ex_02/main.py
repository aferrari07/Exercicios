from funcionario import *

def ex01(nome,salario,aumento):
    funcionario = Funcionario(nome,salario)
    asalario = funcionario.AumentaSalario(aumento)
    #print(" O novo salario sera de R${}" .format(asalario))
    return asalario
