from math import ceil
from .config import *

class RetornoOrcamento():
    def __init__(self, preco_total: float, quantidade_lata_tinta: int):
        self.preco_total = preco_total
        self.quantidade_lata_tinta = quantidade_lata_tinta

def calcula_orcamento(area: float)->RetornoOrcamento:
    quantidade_lata_tinta = ceil(area / METRAGEM_POR_BALDE) 
    preco_total = PRECO_DO_BALDE * quantidade_lata_tinta
    orcamento =  RetornoOrcamento(preco_total, quantidade_lata_tinta)
    return orcamento