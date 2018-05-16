from flask import Flask,jsonify,abort
from flask import make_response, request, url_for
from acesso import leciona
from flask import redirect
app = Flask(__name__)
atividades = [
        {
            'id_atividade':1,
            'id_disciplina':1,
            'enunciado': 'crie um app de todo em flask',
            'respostas': [
                {'id_aluno': 1, 'resposta':'todo.py', 'nota':9},
                {'id_aluno': 2, 'resposta':'todo.zip.rar'}
                ]
        },

        {
            'id_atividade':2,
            'id_disciplina':1,
            'enunciado': 'crie um servidor que envia email em Flask',
            'respostas': []
        },

        ]

'''
Você consegue abrir a pagina que geramos abaixo?

Troque o texto!
'''
@app.route('/')
def index():
        return "Sistema de entrega de atividades"
'''
Vou deixar a primeira URL definida, pra facilitar o debug.
Nao mude ela em nada
'''
@app.route('/atividades/ver_tudo/', methods=['GET'])
def get_all():
     return jsonify(atividades)

'''
Crie uma URL para exibir uma atividade,
em /atividade/<int:id_atividade>

Ela deve retornar 
{'response': 'True', 'atividade': atividade_com_o_campo_extra_URL}
Se a atividade existir

E
{'response': 'False', 'erro': 'atividade nao encontrada'} com codigo de status 404 caso contrario

Cuidado para nao alternar a atividade 'no banco'!
'''
@app.route('/atividade/<int:id_atividade>/')
def atividade(id_atividade):
    for atividade in atividades:
        query = request.args.get('id_professor','')
        bypass = atividade['id_disciplina']
        if (atividade['id_atividade'] == id_atividade) and (query == ''):
            return jsonify({'response':'True','atividade':atividade}),200
        if atividade['id_atividade'] != id_atividade:
            return jsonify({'response':'False','erro':'atividade nao encontrada'}),404
        if leciona(bypass,query) == True:
            copia = dict(atividade)
            copia['url'] = url_for('atividade', id_atividade=copia['id_atividade'])
            retorno = jsonify({'response':'True','atividade':copia})
            return retorno, 200
        else:
            copia = dict(atividade)
            copia['url'] = url_for('atividade',id_atividade=copia['id_atividade'])
            del copia['respostas']
            retorno = jsonify({'response':'True','atividade':copia})
            return retorno, 200


'''
Agora, vamos alterar o comportamento da URL anterior.

Ela deve receber como parametro de query uma id_professor.
Ela só deve retornar as respostas dos alunos se o professor
for um professor da disciplina. Caso contrario, deve suprimir
as respostas
'''

'''
Desafio: o que acontece com a sua funcao de atividades quando 
o servidor de pessoas esta caido?

Seria conveniente que o sistema automaticamente considerasse
o professor inválido. Faça isso!
'''


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0',port=5050)
