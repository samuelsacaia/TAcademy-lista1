from src.application. input import recebe_tamanho,  recebe_velocidade
from src.application.Domain import calcula_tempo
from src.application.output import mostra_dados

if __name__ == '__main__':
    arquivo = recebe_tamanho()
    tempo_aproximado = recebe_velocidade()
    download=calcula_tempo(arquivo, tempo_aproximado)
    mostra_dados(arquivo,tempo_aproximado,download)

    
