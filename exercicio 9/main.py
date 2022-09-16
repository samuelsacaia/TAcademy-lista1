"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de
saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média
dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias
alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima
informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para
armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O
programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve
ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Melhor salto: 6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m
Resultado final:
Rodrigo Curvêllo: 5.9 m"""

from src.application.saltos import recebe_dados, mostra_atleta, mostra_resultado, tira_media, processa_saltos_e_records, Listas, Contadores

if __name__ == "__main__":

    insere_dados = recebe_dados()
    processa_melhor_salto, processa_pior_salto = processa_saltos_e_records()
    calcula_media = tira_media()
    print(mostra_atleta(insere_dados))
    for i in range(1, 6):
        print(f'{i}º salto foi: {Listas.lista_salto[i-1]}m')
    print(mostra_resultado(insere_dados, processa_melhor_salto, processa_pior_salto, calcula_media))



