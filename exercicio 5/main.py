from src.application.exercicio5 import pega_continua_pedido, pega_quantidade_desejada, pega_continua_pedido, pega_opcao_menu
from src.application.exercicio5 import inicia_pedido, monta_cardapio
from src.application.exercicio5 import mostra_tela_inicial, mostra_menu, mostra_pedido

if __name__ == '__main__':
    cardapio = monta_cardapio()
    pedido = inicia_pedido(cardapio)
    opcoes_validas = [key for key, values in cardapio.items()]

    mostra_tela_inicial()
    
    opcao = 0
    while (True):
        mostra_menu(cardapio)    

        opcao = pega_opcao_menu() 
        if (opcao in opcoes_validas):
            pedido[opcao] += pega_quantidade_desejada() 
            if pega_continua_pedido() == 'N': break
        else: print ('Opção invalida')

    mostra_pedido(cardapio=cardapio, pedido=pedido)

