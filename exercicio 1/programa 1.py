"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""


Valor_que_eu_ganho = float(input('Quanto voce ganha por hora? '))
Horas_que_eu_trabalho = int(input('Quantas horas você trabalha por mês? '))

salario_bruto = Valor_que_eu_ganho * Horas_que_eu_trabalho
print (' Salário Bruto : R$ %.2f' % (salario_bruto))


ir = salario_bruto * (11/ 100)
print (' IR: R$ %.2f' % (ir))


inss = salario_bruto * (8 /100)
print (' INSS: R$ %.2f' % (inss) )

sindicato = salario_bruto * (5 / 100)
print (' Sindicato: R$ %.2f' % (sindicato ))


print (' Salário Liquido : R$ %.2f' % (salario_bruto - ir - inss - sindicato))







"""""
quanto_voce_ganha = float (input("quanto voce ganha!"))
horas_trabalhada_no_mes = int(input("horas trabalhadas"))


salario_bruto = quanto_voce_ganha * horas_trabalhada_no_mes
print("+ salario_bruto: quanto voce ganta , horas de trabalho "%(salario_bruto))


ir = salario_bruto * (11/100)
print("-ir:quanto voce ganta , horas de trabalho "%(ir))

inss = salario_bruto * (8 /100)
print("-inss: quanto voce ganta , horas de trabalho" %(inss))

sindicato = salario_bruto * (5/100)
print("-sindicato: quanto voce ganta , horas de trabalho"%(sindicato))


print("salario liquido: quanto voce ganta , horas de trabalho "% (salario_bruto- ir- inss - sindicato))
"""



















