"""""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de
latas de tinta a serem compradas e o preço total.
"""


from http.client import PRECONDITION_FAILED


tamanho = float(input("O tamanho em  m² da área"))

litros = tamanho

latas = int(tamanho )

if (litros !=0):
	latas -=1

valor_total = latas * 80
print ("Quantidade de tinta a ser usada:", litros)
print ("Quantidade de tinta a ser usada:" ,latas)
print("Valor total em R$ a ser usada:", valor_total)


"""
tamanho =float (input("O tamanho em metros quadrados da área:"))
litro= tamanho/3
latas = litro /18
print(f" vai precisar de {latas} lata(s) e custará R${latas *80}")
"""