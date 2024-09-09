from datetime import datetime

def hello():
    # Retorna valores hardcoded para data e nome    
    # Converte a string para um objeto datetime.date
    date = datetime.strptime('2023-01-01', '%Y-%m-%d').date()  # Converte a data para o tipo datetime.date
    # Retorna a data no formato correto e o nome
    return date, 'Autor Desconhecido'

"""import requests


def hello():
    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    commit_info = info[0]['commit']['author']
    return commit_info['date'], commit_info['name']
""""""