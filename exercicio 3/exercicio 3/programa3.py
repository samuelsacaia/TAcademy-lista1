""""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
 quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
 quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6
 litros, que custam R$ 25,00.
 Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
 situações:
 comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias.
"""


tamanho = float(input("Entre com o tamanho em m² área: "))




litro= tamanho 
latas = litro

if latas % (18 != 0):
    latas += 1
preco1 = latas * (80)

print("Apenas as latas de 18 litros :" ,  preco1) 

galoes = litro / 3.0
if galoes % (3.6 != 0):
    galoes += 1

preco2 = galoes * (25)
print("Apenas galões de 3.6 litros: ", preco2)

# mistura de latas e galoes
mistura_lata = int(litro / 18.0)
mistura_galao = int((litro - mistura_lata * 18) / 3.6)

if litro - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print('Mistura: %d latas e %d galoes = %.2f' % (mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))
