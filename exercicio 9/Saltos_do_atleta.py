
"""""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de
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
Rodrigo Curvêllo: 5.9 
"""
import math
# Lista com o nome de cada salto
texto_salto = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

while True:
    # Lista com o valor dos saltos
    saltos_do_atleta = [0.0, 0.0, 0.0, 0.0, 0.0]

    # Outras variáveis
    melhor_salto = pior_salto = media_saltos = 0

    # Solicitado o nome do atleta
    atleta = input("\nAtleta: ")

    # Verificando se o nome do atleta foi digitado
    if atleta != "":
        for i in range(0, 5):
            saltos_do_atleta[i] = float(input(f"{texto_salto[i]} salto: "))

        # Ordenando a lista de saltos
        saltos_do_atleta.sort()

        # Melhor, Pior e Média
        melhor_salto = max(saltos_do_atleta)
        pior_salto   = min(saltos_do_atleta)

        # Excluindo o melhor e o pior salto da média
        media_saltos = (saltos_do_atleta[1] + saltos_do_atleta[2] + saltos_do_atleta[3])/3    

        # Mostrando os resultados
        
        print(f"Melhor salto............: {melhor_salto}")
        print(f"Pior salto..............: {pior_salto}")
        print(f"Media dos de mais saltos.: {media_saltos}")
        print("Resultado final: ")
        print(f"{atleta}: {media_saltos}")
    else:
        print("Informe o nome do atleta")

    print("Deseja enviar os dados de outro atleta?")

    opcao = int(input("Opções: 1- Sim e 2 -Não"))
    if opcao == 2:
        break