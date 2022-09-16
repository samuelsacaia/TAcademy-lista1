from math import ceil,floor

litro_lata = 18  
litro_galao = 3.6

def calcula_necessidade_litros(tamanho):
    quant_litro = tamanho/6
    return quant_litro

def calcula_lata(quant_litro):
    quant_lata_arredondado=ceil(quant_litro/litro_lata)
    return quant_lata_arredondado
    

def calcula_galao(quant_litro):
    quant_galao_arredondado=ceil(quant_litro/litro_galao)
    return quant_galao_arredondado


def misturar_latas_e_galao(quant_litro):
    quant_lata_pura=floor(quant_litro/litro_lata)
    galao_resto=quant_litro%litro_lata
    resultado_galao_resto = ceil(galao_resto/litro_galao)


    return quant_lata_pura,resultado_galao_resto

    




    













