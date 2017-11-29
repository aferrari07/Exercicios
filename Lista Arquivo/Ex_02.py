# coding=utf-8
dic = {}
with open('animais.txt') as arquivo:
    for linha in arquivo:
        linha = linha.rstrip()
        palavras = linha.split(' ')
        for palavra in palavras:
            if palavra in dic.keys():
                dic[palavra] = dic[palavra] + 1
            else:
                dic[palavra] = 1
# sorted(d, key=d.get, reverse=True)
with open('saida.txt', 'w') as arquivo:
    for chave, valor in sorted(dic.items()):
        arquivo.write(chave+": "+str(valor)+"\n")
