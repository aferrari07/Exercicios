class Funcionario():

    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def AumentaSalario(self,Psalario):
        self.Psalario = ((self.salario*Psalario)/100)+self.salario
        return self.Psalario
