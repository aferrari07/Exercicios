class Triangulo():

    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcperimetro(self):
        self.result = self.ladoA + self.ladoB + self.ladoC
        return self.result

    def Lmaior(self):
        self.maiorlado = max(self.ladoA, self.ladoB, self.ladoC)
        return self.maiorlado
