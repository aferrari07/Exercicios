produtos = {
    'tomate' :  [100,2.3],
    'alface' :  [500,0.45],
    'laranja' : [300,1.3],
    'cenoura' : [130,2.1],
    'manga' : [75,3.45]
}

tupla_produtos = tuple(produtos.keys())

def entrada_produtos(nome_produto, qtd):
    #nome_produto = input('Nome do produto: ')
    if not nome_produto in tupla_produtos:
        if nome_produto == 'fim':
            return -1
    elif not nome_produto in tupla_produtos:
        return None
    else:
        #qtd = int(input('quantidade: '))
        produto = produtos[nome_produto]
        dic_retorno = {nome_produto: [qtd, produto[1]]}
        return dic_retorno

def realiza_venda(lista_produtos):
    dic_retorno = {}
    for produto in lista_produtos:
        chave = list(produto.keys())[0]
        produtos[chave][0]  = produtos[chave][0] -1
        dic_retorno[chave] = {
            'quantidade' : produto[chave][0],
            'valor_u' : produto[chave][1],
            'valor_t' : produto[chave][0] * produto[chave][1]
        }

if __name__ == "__main__":
    retorno = 0
    lista_compra = []
    while retorno != -1:
        nome_produto = input("Nome do produto: ")
        if nome_produto != 'fim':
            qtd = int(input('Quantidade: '))
        retorno = entrada_produtos(nome_produto, qtd)
        if retorno != -1 and retorno != None:
            lista_compra.append(retorno)
    print(lista_compra)
