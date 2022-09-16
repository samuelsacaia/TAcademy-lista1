from .config import PERCENTUAL_INSS, PERCENTUAL_IR, PERCENTUAL_SINDICATO
from .dtos import CalculaSalarioResponse

def entrada_dados()->float:
    v_hora = float(input('Digite o valor da hora trabalhada : '))
    hr_trabalhadas = float(input('Digite o números de horas trabalhadas no mês: '))
    
    return v_hora * hr_trabalhadas

def  calcula_salario_e_impostos(salario_bruto: float)->CalculaSalarioResponse:
    retorno = CalculaSalarioResponse()
    if (isinstance(salario_bruto, float)  == False ):
        return retorno

    if (salario_bruto < 0):
        return retorno

    retorno.salario_bruto = salario_bruto
    retorno.desconto_IR = salario_bruto * PERCENTUAL_IR
    retorno.desconto_INSS = salario_bruto  * PERCENTUAL_INSS
    retorno.desconto_sindicato = salario_bruto * PERCENTUAL_SINDICATO
    retorno.salario_liquido = salario_bruto - retorno.desconto_IR - retorno.desconto_INSS - retorno.desconto_sindicato

    return retorno

def mostra_resultado(info_salario: CalculaSalarioResponse):
    print(f'Salario Bruto : R$ {info_salario.salario_bruto}')
    print(f'DESCONTO DE 11% IR : R$ {info_salario.desconto_IR}')
    print(f'DESCONTO DE 8%  INSS: R$ {info_salario.desconto_INSS}')
    print(f'DESCONTO DE 5% SINDICATO: R$ {info_salario.desconto_sindicato}')
    print(f'SALARIO LIQUIDO: R$ {info_salario.salario_liquido}')