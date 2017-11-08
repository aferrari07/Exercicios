from livro import *

def ex02(nome,qtdpaginas,autor,preco,alt):
    livro = Livro(nome,qtdpaginas,autor,preco)
    #print("O preço do livro é R${}" .format(livro.getPreco()))
    preco = livro.setPreco(alt)
    #print("O novo preço do livro é R${}" .format(livro.getPreco()))
    return preco
