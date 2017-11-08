class Livro():

    def __init__(self,nome,qtdpaginas,autor,preco):
        self.nome = nome
        self.qtdpaginas = qtdpaginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        return self.preco

    def setPreco(self,altpreco):
        self.preco = altpreco
        return self.preco
