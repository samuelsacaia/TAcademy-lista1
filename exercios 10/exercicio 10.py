"""
10. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são
eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que
receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e
depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto edepois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo
de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""


from stringprep import in_table_c22


recebe_nome = input("Digita o nome do atleta:")
while True:
    notas_dos_jurados = []

    if recebe_nome !="":
        for i in range (7):
            nota=float(input("Digite a nota "))
            notas_dos_jurados.append(nota)

        print("resultado_final:")
        recebe_nome = str(input("Digita o nome do atleta:"))

        notas_dos_jurados.sort()

        nota_maior =max(notas_dos_jurados)
        nota_pior = min (notas_dos_jurados)

        media_do_atleta =sum (notas_dos_jurados)/len(notas_dos_jurados)
    
        print(f"nota_maior: {nota_maior}")
        print(f"nota_pior: {nota_pior}")
        print(f"media_do_atleta: {media_do_atleta}")
        break


        
    



