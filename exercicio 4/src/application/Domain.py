
import math


def calcula_tempo(arquivo: float, tempo_aproximado: float)->float:
    download =float(math.ceil((arquivo / (tempo_aproximado/ 8)) / 60))
    return download