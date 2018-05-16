import requests


'''
Crie uma funcao que retorna True 
se um professor leciona uma disciplina
e False caso contrario

Se a disciplina nao existe, retorne :False,'inexistente'
'''

def leciona(id_professor, id_disciplina):
    r = requests.get('http://localhost:5000/leciona/' + str(id_professor) + '/' + str(id_disciplina) + '/')
    result = r.json()
    if result['response'] == 'True':
        if result['leciona'] == 'True':
            return True
        if result['leciona'] == 'False':
            return False
    return False, 'inexistente'

'''
Agora, de runtests.

Se esta tudo ok, (passou teste 002) siga para o arquivo 
sistema_atividades.py

A atividade de 07 de marco pode ser util para lembrar como usar a biblioteca requests
'''

