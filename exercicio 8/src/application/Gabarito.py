"""A Média das Notas da Turma.
Gabarito da Prova:
01 - A, 02 - B, 03 - C, 04 - D, 05 - E, 06 - E, 07 - D, 08 - C, 09 - B e 10- A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da
prova antes dos alunos usarem o programa."""

from dataclasses import dataclass

@dataclass
class DicionarioELista:
    dic_gabarito = {}
    lista_resposta = []

@dataclass
class Contadores:
    conta_acerto = 0
    conta_uso = 0
    maior_acerto = 0
    menor_acerto = 10


    

def insere_gabarito():
    for i in range(1, 11):
        DicionarioELista.dic_gabarito[i] = input(f'Insira o gabarito da questão {i}: ').split.upper

def insere_resposta():
    for i in range(1, 11):
        resposta = input(f'Insira a resposta da pergunta {i}: ').split.upper
        DicionarioELista.lista_resposta.append(resposta)

def compara_resposta_com_gabarito():
    for i in range(1, 11):
        if DicionarioELista.dic_gabarito[i] == DicionarioELista.lista_resposta[i - 1]:
            Contadores.conta_acerto += 1
    
def conta_uso():
    Contadores.conta_uso += 1

def conta_recordes():   
    if Contadores.conta_acerto > Contadores.maior_acerto:
        Contadores.maior_acerto = Contadores.conta_acerto
    elif Contadores.conta_acerto <= Contadores.menor_acerto:
        Contadores.menor_acerto = Contadores.conta_acerto

def exibe_resultado():
    print(f'Você obteve {Contadores.conta_acerto} acertos')
    Contadores.conta_acerto = 0
    DicionarioELista.lista_resposta = []

    