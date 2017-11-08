class Aluno():

    def __init__(self,nome,curso,tempSdormir):
        self.nome = nome
        self.curso = curso
        self.tempSdormir = tempSdormir

    def Estudar(self,estudar):
        self.tempSdormir = estudar-(self.tempSdormir)
        return self.tempSdormir

    def Dormir(self,dormir):
        self.tempSdormir = dormir+(self.tempSdormir)
        return self.tempSdormir
