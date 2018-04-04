import requests as req


'''
coloque sua chave do omdb aqui.

Se voce nao criou ou nao lembra, pode pedir emprestado para um amigo
'''

chave_omdb='1525c1ab'

'''
Crie uma funçao existe_id de busca no OMDB, 
que dada uma id, retorna se a id existe na base do omdb ou nao.

(ou seja, True se existe e false caso contrário)

Essa função, você pode testar no run_module.


Por exemplo

existe_id('nao') deve retornar False
existe_id('tt1211837') deve retornar True

lembrando: a URL em questao eh
url = "http://www.omdbapi.com/?apikey={}&i={}".format(chave_omdb, id_omdb)

para pegarmos o json, fazemos
retorno = req.get(url).json()
e retorno eh um dicionario

se nao estiver funcionando, use print(url) e verifique o que o omdb esta
te mandando

'''

def existe_id(film_id):
    url = "http://www.omdbapi.com/?apikey={}&i={}".format(chave_omdb, film_id)
    retorno = req.get(url).json()
    if retorno['Response'] == 'True':
        return True
    if retorno['Response'] == 'False':
        return False
'''
Crie uma funcao pega_nome que, dada uma id do omdb, devolve o nome do filme

Ela é muito similar a funcao existe_id, so que acessa outra posicao do dicionario.

Alias, se a id nao existir, retorne 'id nao encontrada'
'''

def pega_nome(film_id):
    url = "http://www.omdbapi.com/?apikey={}&i={}".format(chave_omdb, film_id)
    retorno = req.get(url).json()
    if retorno['Response'] == 'False':
        return 'id invalida'
    else:
        dados = {
        'nome':retorno['Title'],
        'film_id': film_id
        }
        return dados

'''
relacionados, no formato
{
  'name': 'nome',
  'film_id': 'IMDB_id'
}
'''
def busca_filmes(texto_buscar):
    url = "http://www.omdbapi.com/?apikey={}&s={}&type=movie".format(chave_omdb, texto_buscar)
    retorno = req.get(url).json()
    resposta = []
    for filme in retorno['Search']:
        while len(resposta) < 10:
            result = {}
            result['Title'] = filme['Title']
            result['Year'] = filme['Year']
            result['imdbID'] = filme['imdbID']
            result['Type'] = filme['Type']
            result['Poster'] = filme['Poster']
            resposta.append(result)
    return result
