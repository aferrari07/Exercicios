#!bin/python
from flask import Flask,jsonify,abort
from flask import make_response, request


app = Flask(__name__)

@app.route('/')
def index():
        return "Funcoes matematicas!"

'''
defina uma url potencia de 2, de forma que 
chamar /matematica/potencia_de_dois/<int:expoente>
com o metodo GET calcule a potencia desejada.

Por exemplo, ao acessarmos 
http://localhost:5000/matematica/potencia_de_dois/5
devemos receber 
{ "resposta": 32 }
'''
'''
Quando não mandarmos o numero, retorne 
{'erro':'sem expoente'} e o codigo de erro 400
'''
@app.route('/matematica/potencia_de_dois/<int:expoente>', methods=['GET'])
def potencia_2(expoente):
    calc = 2**expoente
    return jsonify({'Reposta':calc})

@app.route('/matematica/potencia_de_dois/', methods=['GET'])
def request_invalida():
    return make_response(jsonify({'error': 'sem expoente'}),
                             400)

'''
Para a URL /matematica/soma, com o método POST,
queremos o seguinte:

Que ela receba um json no corpo (body) do request,
e esse json deve definir dois numeros (a e b)

Ela deve retornar um json {resposta: v} onde v=a+b

Se o json nao contiver as chaves a ou b, ela deve retornar
um erro 400 (request mal formado) e um texto de erro
'''
@app.route('/matematica/soma',methods=['POST'])
def soma():
    numbers = {
        'a': 0,
        'b': 0 
        }
    if 'a' and 'b' in request.json:
        numbers['a'] = request.json.get('a')
        numbers['b'] = request.json.get('b')
        soma = numbers['a'] + numbers['b']
        return jsonify({'V =':soma})
    else:
        return make_response(jsonify({'error': 'nome de chave errada'}),
                             400)



'''
Crie a mesma função soma, agora recebendo os parametros 
através da URL

Ou seja,

http://localhost:5000/matematica/soma?b=13&a=12

Deverá retornar

{
    "soma": 25
}

(esses parametros estao sendo mandados na URL de uma forma
padrao, e o flask dá suporte a isso.
Ja fizemos algo parecido no ex do TODO.
Nao deixe de rodar o soma get e o soma get invertido
no postman)
'''
@app.route('/matematica/soma',methods=['GET'])
def soma_get():
    a = request.args.get('a','')
    b = request.args.get('b','')
    soma = int(a) + int(b)
    
    return (jsonify({'soma': soma}),200)
    

    
'''
A partir daqui nao tem mais nada pra fazer
'''
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
