from typing import Tuple, Union


def pegar_a_maior_e_pior_nota(notas_jurados)-> Tuple[int, int]:
    valor_max=max(notas_jurados)
    valor_min=min(notas_jurados)
    return valor_max, valor_min



def  excluir_o_valor_max_valor_min_e_achar_a_media(notas_jurados,valor_max,valor_min):
    copia_lista_nota = notas_jurados.copy()
    copia_lista_nota.remove(valor_max )
    copia_lista_nota.remove(valor_min)

    if (len(copia_lista_nota) == 0): return 0

    media_notas = sum(copia_lista_nota)/len(copia_lista_nota)
    return media_notas




