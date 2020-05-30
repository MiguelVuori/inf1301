import sys
sys.path.insert(1, 'pontuacao/')
sys.path.insert(1, 'tabela/')
sys.path.insert(1, 'dado/')

import dadoController
#import pontuacaoController

__all__ = ['cria_jogo', 'inicia_jogo', 'termina_jogo', 'inicia_vez', 'termina_vez']



def init():
    global jogadores
    global tabela_Y
    tabela_Y = {
        "Um": 0,
        "Dois": 0,
        "Três": 0,
        "Quatro": 0,
        "Cinco": 0,
        "Seis": 0,
        "Bônus_sup": 0,
        "Trinca": 0,
        "Quadra": 0,
        "Full House": 0,
        "Sequência Mínima": 0,
        'Sequência Máxima': 0,
        "YAHTZEE": 0,
        "Bônus_YAHTZEE": [0,0,0],
        "Total": 0
    }

def inicia_jogo():
        rodada = 1
        while True:
            for id_jogador in jogadores:
                inicia_vez(jogadores[id_jogador])
            rodada = rodada + 1


def inicia_vez():

        dadoController.inicia_view()
        dados = dadoController.pega_dados()
        print(dados)

        categoria = input_handler(input("Escolha a categoria de pontuacao: "), str)
        pontos = pnt_pontua(categoria,dados)
        pnt_atualiza_pontuacao(jogador["nome"], categoria, pontos)


def termina_vez(jogador):
    tab_print()
    print("".center(48, "-"))

jogadores = {}
init()
