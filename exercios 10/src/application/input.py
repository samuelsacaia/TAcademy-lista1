from typing import List

def receber_nome()->str:
    nome_do_atleta= str(input("digite o nome do atleta? "))
    return nome_do_atleta

def receber_nota()->List[int]:
    notas_jurados = []
    for i in range(7): 
       notas = float(input("digitar nota"))
       notas_jurados.append(notas)
    return notas_jurados