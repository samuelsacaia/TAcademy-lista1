from src.application.Gabarito import Contadores,insere_gabarito,insere_resposta,compara_resposta_com_gabarito,conta_uso,conta_recordes,exibe_resultado



if __name__ == "__main__":
    recebe_gabarito = insere_gabarito()

    while True:

        recebe_resposta = insere_resposta()
        processa_resposta = compara_resposta_com_gabarito()
        calcula_uso = conta_uso()
        calcula_recordes = conta_recordes()
        mostra_resultado = exibe_resultado()
                
        prompt_uso = input('Deseja continuar? [s] ou [n]')
        if (prompt_uso == 's') or (prompt_uso == 'S'):
            continue
        else:
            print(f'O total de usuários foi de { Contadores.conta_uso}, o maior número de acertos foi {Contadores.maior_acerto} e o menor foi {Contadores.menor_acerto}.')
            break