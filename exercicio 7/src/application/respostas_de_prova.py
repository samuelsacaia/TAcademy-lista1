from dataclasses import dataclass

def pega_respostas(numero_respostas: int) -> dict:
    retorno = {}
    for i in range(1, numero_respostas+1):
        resposta = input(f'Insira a resposta da pergunta {i}: ')
        retorno[i] = resposta

    return retorno

def compara_resposta_com_gabarito(gabarito, resposta)->int:
    acertos = 0
    for i in range(1, len(gabarito)+1):
        if gabarito[i] == resposta[i]:
            acertos += 1

    return acertos

def exibe_resultado(acertos: int) -> None:
    print(f'Você obteve {acertos} acerto(s)')

def exibe_resultado_geral(numero_alunos: int, maior_acertos: int, menor_acertos: int) -> None:
    print(f'O total de usuários foi de {numero_alunos}, o maior número de acertos foi {maior_acertos} e o menor foi {menor_acertos}.')
