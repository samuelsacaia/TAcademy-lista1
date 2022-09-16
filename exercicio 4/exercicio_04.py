"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este
link (em minutos)"""
import math

tamanho_arquivo = float(input('Qual é o tamanho do arquivo em MB? '))
velocidade_internet = float(input('Qual é a velocidade da internet, em Mbp/s? '))
tempo_de_download = math.ceil((tamanho_arquivo / (velocidade_internet / 10)) / 60)

print(f'O tempo de download do arquivo com tamanho {tamanho_arquivo}MB em uma velocidade {velocidade_internet}Mbp/s é de aproximadamente {tempo_de_download} minutos.')