#arquivoRel = open('twitter/tweets.txt')
# arquivoAbs = open('tweets.txt') 



# #Abre Leitura
# with open('saida.txt', 'r') as arquivo: # Quando o bloco terminar a execução, o with fecha o arquivo!
#     arquivo.write('texto 1\n')
#     arquivo.write('texto 2')    

# coding:utf-8
dic = {}

with open('tweets.txt') as arquivo: # Quando o bloco terminar a execução, o with fecha o arquivo!
    for linha in arquivo:
        #remove \n final da linha
        linha = linha.rstrip()
        #separar linha por espaço
        palavras = linha.split(' ')
        #percorre palavra para contar
        for palavra in palavras:
            if palavra in dic.keys():
                dic[palavra] = dic[palavra] + 1
            else:
                dic[palavra] = 1

#Abre escrita
with open('saida.txt', 'w') as arquivo:
    for chave, valor in dic.items():
        arquivo.write(chave + ' : '+str(valor)+'\n')

    
    
    # arquivo.write('texto 1\n')
    # arquivo.write('texto 2')


    # Realiza a leitura do arquivo
    # conteudo = arquivoAbs.read()
    # print(conteudo)


    # arquivoAbs.seek(1000)
    # conteudo = arquivoAbs.read()
    # print('\n\n\n------------------------------Segunda leitura')
    # print(conteudo)

    # print(arquivoAbs.tell())
    # arquivoAbs.close()

