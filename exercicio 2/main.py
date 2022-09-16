from src.application.input import pega_area_pintura
from src.application.output import  mostra_orcamento
from src.application.domain import calcula_orcamento

if __name__== '__main__':
   area_pintura = pega_area_pintura()
   orcamento = calcula_orcamento(area_pintura)
   mostra_orcamento(orcamento.preco_total, orcamento.quantidade_lata_tinta)