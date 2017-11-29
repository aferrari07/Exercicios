dic = {}
with open('nota_aluno.txt') as arquivo: # Quando o bloco terminar a execução, o with fecha o arquivo!
    for linha in arquivo: #remove \n final da linha
        linha = linha.rstrip() #separar palavra por ponto-virgula
        palavras = linha.split(';') #percorre palavra para contar
        print(palavras)
        for palavra in palavras:
            if palavra in dic.keys():
                dic[palavra] = dic[palavra] + 1
            else:
                dic[palavra] = 1
    print(dic)
