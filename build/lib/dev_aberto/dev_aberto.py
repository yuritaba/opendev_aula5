from datetime import datetime

def hello():
    # Retorna valores hardcoded para data e nome
    print("Função hello chamada corretamente.")
    
    # Converte a string para um objeto datetime.date
    date = datetime.strptime('2023-01-01', '%Y-%m-%d').date()  # Converte a data para o tipo datetime.date
    
    # Retorna a data no formato correto e o nome
    return date, 'Autor Desconhecido'