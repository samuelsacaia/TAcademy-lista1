"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa
deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e
assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o
sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem
respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema"""

from src.application.respostas_de_prova import exibe_resultado_geral, pega_respostas, compara_resposta_com_gabarito, exibe_resultado

if __name__ == "__main__":
    gabarito = {1: 'a', 2: 'a', 3: 'a', 4: 'a', 5: 'a', 6: 'a', 7: 'a', 8: 'a', 9: 'a', 10: 'a'}
    numero_alunos = 0
    maior_acertos = -1
    menor_acertos = 999999

    while True:
        respostas = pega_respostas(len(gabarito))
        numero_acertos = compara_resposta_com_gabarito(gabarito, respostas)
        if (numero_acertos > maior_acertos): maior_acertos = numero_acertos
        if (numero_acertos < menor_acertos): menor_acertos = numero_acertos
        
        numero_alunos += 1
        exibe_resultado(numero_acertos)
        prompt_uso = input('Deseja continuar? [s] ou [n]')
        if (prompt_uso == 'N') or (prompt_uso == 'n'):
            break
    
    
    exibe_resultado_geral(numero_alunos, maior_acertos, menor_acertos)

    
