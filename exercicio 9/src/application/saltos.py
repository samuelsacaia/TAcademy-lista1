from dataclasses import dataclass


@dataclass
class Listas:
    lista_salto = []
    lista_salto_ordenada = []

@dataclass
class Contadores:
    somatorio = 0
    contador = 0

def recebe_dados() -> str:
    nome_atleta = input('Insira o nome do atleta: ')
    if nome_atleta == '':
        print(10/0)
    for i in range (1, 6):
        nota = float(input(f'Insira o {i}º salto do atleta {nome_atleta}.\n'))
        Listas.lista_salto.append(nota)
    return nome_atleta

def processa_saltos_e_records():
    Listas.lista_salto_ordenada = Listas.lista_salto.copy()  
    tamanho_lista = len(Listas.lista_salto_ordenada)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(tamanho_lista - 1):
            if Listas.lista_salto_ordenada[i] > Listas.lista_salto_ordenada[i + 1]:
                Listas.lista_salto_ordenada[i], Listas.lista_salto_ordenada[i + 1] = Listas.lista_salto_ordenada[i + 1], Listas.lista_salto_ordenada[i]
                ordenado = False
    melhor_salto = Listas.lista_salto_ordenada[tamanho_lista-1]
    pior_salto = Listas.lista_salto_ordenada[0]
    return melhor_salto, pior_salto
        

def tira_media():
    tamanho_lista = len(Listas.lista_salto_ordenada)
    Listas.lista_salto_ordenada.pop(tamanho_lista-1)
    Listas.lista_salto_ordenada.pop(0)
    tamanho_lista = len(Listas.lista_salto_ordenada)
    for salto in Listas.lista_salto_ordenada:
        Contadores.somatorio += salto
    media_salto = Contadores.somatorio / tamanho_lista
    return media_salto

def mostra_atleta(nome_atleta):
    return f'Os resultados do atleta {nome_atleta} foram:'

    

def mostra_resultado(nome_atleta, melhor_salto, pior_salto, media_salto):
    return f'O atleta {nome_atleta} teve como melhor salto {melhor_salto}m, como pior salto {pior_salto}m, e média de saltos válidos {media_salto:.2f}.'
