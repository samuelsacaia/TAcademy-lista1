from dataclasses import dataclass
from typing import List



@dataclass
class ItemCardapio:
    descricao: str = ""
    preco: float = 0

def pega_continua_pedido():
    reposta = input('Deseja fazer mais algum pedido?\n S/N')
    return reposta.upper()

def monta_cardapio()->dict:
    cardapio = dict()

    cardapio[100] = ItemCardapio("Cachorro Quente", 1.20)
    cardapio[101] = ItemCardapio("Bauru Simples", 1.30)
    cardapio[102]= ItemCardapio("Bauru com ovo", 1.50)
    cardapio[103]= ItemCardapio("Hambúrguer", 1.20)
    cardapio[104]= ItemCardapio("Cheeseburguer", 1.30)
    cardapio[105]= ItemCardapio("Refrigerante", 1.00)

    return cardapio

def mostra_tela_inicial()->None:
    NUMERO_REPETICOES = 40
    print ('*' * NUMERO_REPETICOES)
    print ('Cardápio'.center(NUMERO_REPETICOES))
    print ('_' * NUMERO_REPETICOES)
    print('Código  /  Especificação  /   Preço'.center(NUMERO_REPETICOES))
    print ('_' * NUMERO_REPETICOES )

def mostra_menu(cardapio: dict):
    for chave, item in cardapio.items():
        print(f' {chave} / {item.descricao:20s} / R$ {item.preco:.2f}')

    print ('_' * 40 )

def mostra_pedido(cardapio: dict, pedido: dict):
    print ('Seu pedido possui:')    
    preco_total = 0
    for chave, item in pedido.items():
        if item > 0:
            produto = cardapio[chave]
            preco_produto = produto.preco * item
            preco_total += preco_produto
            print(f'{item} unidades de {produto.descricao} no total de R${preco_produto:.2f}')

    print(f'O total do seu pedido é de R${preco_total:.2f}')

def pega_opcao_menu():
    return int(input('Escolha a sua opcão:'))

def pega_quantidade_desejada():
    return int(input('Quantas unidades deseja?'))

def inicia_pedido(cardapio: dict)->dict:
    retorno = dict()

    for chave in cardapio:
        retorno[chave] = 0
        
    return retorno

