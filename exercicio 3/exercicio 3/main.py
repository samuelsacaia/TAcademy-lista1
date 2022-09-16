from src.application.input import inicio_de_dados
from src.application.domain import calcula_necessidade_litros,misturar_latas_e_galao,calcula_galao,calcula_lata
from src.application.output import mostra_resultado




if __name__ == "__main__":
    tamanho =inicio_de_dados()
    quant_litro=calcula_necessidade_litros(tamanho)
    quant_lata_arredondado=calcula_lata(quant_litro)
    quant_galao_arredondado=calcula_galao(quant_litro)
    quant_lata_pura,quant_galao_resto=misturar_latas_e_galao(quant_litro)
    mostra_resultado(quant_lata_arredondado,quant_galao_arredondado, quant_lata_pura,quant_galao_resto)



   




    """""
    metragem_area_parede=calcula_apenas_latas 
    metragem_area_parede = calcula_apenas_gallons 
    metragem_area_parede = calcula_latas_e_galoes 

    mostra_orcamentos (metragem_quadrada , metragem_area_parede,  metragem_area_parede,  metragem_area_parede, total_latas, total_galoes)  
    """