from aluno import *

aluno = Aluno(input("Digite o nome do aluno :"),input("Digite o curso que ele faz :"),int(input(" Esta quanto tempo sem dormir ? : ")))
aluno.Estudar(int(input("Quantas horas voce estudar ? :")))
dormir = aluno.Dormir(int(input("Quantas horas voce Dorme ? :")))
print(" Voce esta {}Hs sem dormir" .format(dormir))
