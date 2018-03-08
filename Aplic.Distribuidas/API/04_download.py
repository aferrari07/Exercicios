import requests as req 



def baixar_poster(id_filme):
    api_key = '1525c1ab'
    url = "http://img.omdbapi.com/?apikey={0}&i={1}".format(api_key, id_filme)
    retorno = req.get(url)
    if retorno.status_code == 404:
        return "id invalida"
    else:
        return "id valida"
    print(url)
    
    arquivo = open("Poster.jpg", "wb")
    arquivo.write(retorno.content)
    arquivo.close()
    
    
'''id_star_wars=tt0076759'''
'''tt0796366 é a id de star trek
tt1211837 é a id de doctor strange'''

'''
1) experimente a função, usando as ids acima
2) tente rodar a funcao com a id naonaonao. O que ocorreu?
3) corrija o problema: faça a função retornar 'id inválida' quando 
ela recebeu uma id invalida, e 'id valida' quando a id era valida
(dica, procure o codigo de status no postman)
(dica, procure como descobrir o codigo de status
com a biblioteca requests em
http://docs.python-requests.org/en/master/user/quickstart/)
'''

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_01_invalida(self):
        resposta = baixar_poster('tt0796366naoao')
        self.assertEqual(resposta,'id invalida')
        resposta = baixar_poster('bonde')
        self.assertEqual(resposta,'id invalida')
        resposta = baixar_poster('blackkamenrider')
        self.assertEqual(resposta,'id invalida')
        
    def test_02_valida(self):
        resposta = baixar_poster('tt0796366')
        self.assertEqual(resposta,'id valida')
    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


