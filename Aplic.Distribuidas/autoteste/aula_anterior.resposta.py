#!bin/python
from flask import Flask,jsonify,abort
from flask import make_response


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Fazer compras',
        'description': u'Leite, queijo, pizza, frutas',
        'done': False
    },
    {
        'id': 2,
        'title': u'Aprender flask',
        'description': u'http://flask.pocoo.org/docs/0.12/', 
        'done': False
    }
]

'''
Você consegue abrir a pagina que geramos abaixo?

E os seus colegas?

Troque o texto
'''
@app.route('/')
def index():
        return "Hello, World!"
'''
A url definida nesse @app.route recebe a resposta da função;
Ou seja, acessando a URL veremos a resposta da função.

Nesse caso, a resposta é texto. A função "jsonify" transforma
objetos python em texto que representa json equivalente
'''
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
     return jsonify(tasks)

'''
Note o uso do make_response, para retornar o codigo http 
para não encontrado e também um erro em formato json
'''
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    wanted_task = 'not found'
    for task in tasks: 
        if task['id'] == task_id:
            wanted_task = task
    if wanted_task == 'not found':
        return make_response(jsonify({'error': 'Task not found'}),
                             404)
    return jsonify({'task': wanted_task})

'''
Criar novas tarefas.

Veja que a URL é a mesma que a lista de tarefas.

O que muda é o  VERBO HTTP (lá era GET, aqui é POST)
'''
from flask import request
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json:
        return make_response(jsonify({'error': 'Format not json'}),
                             400)
    '''um erro 400 indica um request mal formado'''
    if 'title' not in request.json or request.json['title'] == '':
        return 'no title', 400
    task = {
        'id': tasks[-1]['id'] + 1,#temos um bom motivo para nao
#usar len(lista). Qual é?
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    '''201 é o codigo http para "recurso criado"'''
    return jsonify({'task': task}), 201
''' 
se quiser, de uma olhada em
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#2xx_Success
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_errors
'''







''' crie uma função update que recebe um json parcial de uma 
tarefa, e altera apenas os elementos recebidos
'''


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = 'nope'
    for candidate in tasks: 
       if candidate['id'] == task_id:
           task = candidate
         
    if task == 'nope':
        return 'tarefa não encontrada',404
    print(task)
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})
    #para que serve esse return?


'''crie uma funcao delete_task, que deleta uma tarefa
ela deve retornar erro se a tarefa não existir
'''
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = 'nope'
    for candidate in tasks: 
       if candidate['id'] == task_id:
           task = candidate
    if task == 'nope':
        return 'tarefa não encontrada',404
    tasks.remove(task)
    return jsonify({'result': True})

'''
Crie uma função de busca, que recebe uma string e retorna
todas as tarefas que contém essa string, ou no título
ou na descrição
'''
@app.route('/todo/api/v1.0/tasks/search', methods=['GET'])
def search_text():
    query = request.args.get('query',None)
    if (query == None):
       return jsonify({'error':'no query'}),400
    results = []
    for task in tasks:
        if (query in task['title'] 
           or query in task['description']):
           results.append(task)
    return jsonify({'results': results,'total':len(results)})

'''
adicione um erro quando tentamos criar uma tarefa sem título.

Ele deve retornar um codigo adequado de erro E um erro 
auto-explicativo para o usuário, no formato json
'''

'''
Torne sua função de busca de tarefas com um determinado texto
"case-insentive". Ou seja, ela deve ignorar quais letras
são maiusculas ou minusculas quando ela faz a busca
'''


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
