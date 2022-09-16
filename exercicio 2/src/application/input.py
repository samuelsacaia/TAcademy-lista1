from math import ceil
from src.application.config import PRECO_DO_BALDE, METRAGEM_POR_BALDE


def pega_area_pintura()->float:
    altura = float(input('Altura da superfície: '))
    largura = float(input('Largura da superfície: '))
    return altura * largura



