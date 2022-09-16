
from src.application.input import receber_nome, receber_nota
from src.application.negocio import pegar_a_maior_e_pior_nota,excluir_o_valor_max_valor_min_e_achar_a_media
from src.application.output import mostra_o_resultado
if __name__ == "__main__":
    nome_do_atleta=receber_nome()
    notas_jurados = receber_nota()
    valor_max , valor_min = pegar_a_maior_e_pior_nota(notas_jurados)
    media_notas =  excluir_o_valor_max_valor_min_e_achar_a_media(copia_lista_nota ,valor_max,valor_min)
    mostra_o_resultado( nome_do_atleta,notas_jurados,valor_max,valor_min, media_notas ) 