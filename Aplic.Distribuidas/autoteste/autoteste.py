#!bin/python
from flask import Flask,jsonify,abort
from flask import make_response
from flask import request


app = Flask(__name__)

questoes = [
    {
        'id': 1,
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro' ],
        'corretas': ['Remote procedure call']
    },
    {
        'id': 2,
        'pergunta': 'Quanto é 2**6?',
        'erradas': [12,36,26,32],
        'corretas': [64]

    }
]

respostas = {
        'marcio':{1:'Random Person Changer'},
        'maria':{1:'Remote Procedure Call', 2: 64},
        }

@app.route('/')
def index():
    return "Testes automáticos!"

'''
Ao acessar a URL /autoteste/questoes o usuario deve receber
uma lista completa de todas as questoes
'''
@app.route('/autoteste/questoes', methods=['GET'])
def get_questoes():
    return (jsonify(questoes),200)
@app.route('/autoteste/respostas',methods=['GET'])
def get_respostas():
    return (jsonify(respostas),200)
'''
Podemos acessar uma questao especifica na URL
/autoteste/questao/<int:q_id>

Se a questao existir, retorne a questao

Se nao existir, retorne um texto  de erro e o codigo 404
'''
@app.route('/autoteste/questao/<int:q_id>', methods=['GET'])
def get_search(q_id):
    search = 'not found'
    for quest in questoes:
        if quest['id'] == q_id:
            search = quest
    if search == 'not found':
        return make_response(jsonify({'error': 'Questão não encontrada'}),
                             404)
    return jsonify({'questoes': search })
'''

Ao usarmos o verbo POST na url autoteste/questao/

queremos criar uma nova questao.

no corpo da mensagem, enviamos o texto da questao,
uma lista de alternativas incorretas e uma lista
de alternativas corretas.

voce deve armazenar essa nova questao e retornar 
uma representacao JSON dela, com o codigo 201 (created)

Se um dos campos estiver faltando, voce deve retornar um 
texto de erro, e o codigo 400

'''
@app.route('/autoteste/questao/',methods=['POST'])
def new_questao():
    if not request.json:
        return make_response(jsonify({'error': 'Format not json'}),
                             400)
    
    if 'pergunta' not in request.json or request.json['pergunta'] == '':
        return 'sem pergunta', 400
    questao = {
        'id': questoes[-1]['id'] + 1,
        'pergunta': request.json['pergunta'],
        'erradas': request.json['erradas'],
        'corretas': request.json['corretas']
    }
    questoes.append(questao)
    
    return jsonify({'questoes': questoes}), 201

'''
Ao usarmos o verbo PUT na url 
/autoteste/questao/<int:q_id>/erradas

queremos adicionar mais alternativas erradas à questão.

enviamos, no corpo do request, uma lista de alternativas 
incorretas, e elas devem ser acrescentadas à questão.

(por exemplo:

    {"erradas":[1,2,3,4,5]}

)

Se a questao não existir, devemos retornar o codigo 404
e uma mensagem de erro

Se a questão existir, devemos retornar a questao modificada
'''
@app.route('/autoteste/questao/<int:q_id>/erradas',methods=['PUT'])
def update_erradas(q_id):
    finder = None
    for search in questoes: 
       if search['id'] == q_id:
           finder = search
         
    if finder == None:
        return 'Questão não encontrada',404
    finder['erradas'] += request.json.get('erradas')
    return jsonify({'finder': finder})


           
'''
faça o mesmo, adicionando alternativas corretas extras
'''
@app.route('/autoteste/questao/<int:q_id>/corretas',methods=['PUT'])
def update_corretas(q_id):
    finder = None
    for search in questoes: 
       if search['id'] == q_id:
           finder = search
         
    if finder == None:
        return 'Questão não encontrada',404
    finder['corretas'] += request.json.get('corretas')
    return jsonify({'finder': finder})

'''
(bonus)
Melhore suas funções de adição de alternativas,
fazendo com que nao sejam adicionadas alternativas repetidas
'''


'''
Respondendo às perguntas

Fazendo um PUT na URL http://localhost:5000/autoteste/responder/1
o usuario 'fulano' pode responder à pergunta de id 1

ele deve mandar um json como o seguinte:
    { "usuario": "fulano",
      "resposta": "Remote Procedure Call"}

A sua resposta deve ser armazenada no dicionario respostas
(veja exemplos no inicio do arquivo)

Se ele ja respondeu a pergunta, devemos retornar um erro 
descritivo e o codigo 409 (confito de edição)
(teste enviando a mesma varias vezes)

Se ele respondeu com uma alternativa que nao está
nem na lista de corretas nem na lista de incorretas
, devemos retornar
um erro descritivo e o codigo 400 (bad request)

Se o usuário nao está na lista de respostas, devemos adicionar
ele
'''

'''
O usuario deve poder ver quantas perguntas ainda nao
respondeu, quantas acertou e quantas errou.

Acessando a url http://localhost:5000/<username>/resultados/
O usuario deve receber um json como o seguinte:

    {
    "usuario": "fulano",
    "acertos": 3,
    "erros": 2,
    "nao respondidas": 2
    }

(o verbo http em questao é GET)
'''
       

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
