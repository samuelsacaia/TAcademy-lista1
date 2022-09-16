import math
from .config import SEGUNDOS_MINUTO, TAMANHO_BYTE

def recebe_tamanho()->float:
    arquivo =float(input('Qual é o tamanho do arquivo em MB? '))
    return arquivo

def recebe_velocidade()->float:
    tempo_aproximado =float(input('Qual é a velocidade da internet, em Mbp/s? '))
    return   tempo_aproximado

