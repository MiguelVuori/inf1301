import sys
sys.path.insert(1, 'TADpontuacao/')
sys.path.insert(1, 'TADtabela/')
from dado import *
from pontuacao import *
from tabela import *
from utils import *

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
def cria_jogo():
    print("\nUse 'quit' como input para terminar o jogo\n")
    n_jogadores = input_handler(input("Número de jogadores: "), int)
    for n in range (0, n_jogadores):
        id = n + 1
        
        nome = input_handler(input("Nome do jogador %d: " % id), str)
        jogadores[id] = {
            'nome': nome
        }
        tab_ins(nome,tabela_Y)


def inicia_jogo():
        rodada = 1
        while True:
            print("\n\n")
            print(" RODADA %d ".center(48, "#") % rodada)
            for id_jogador in jogadores:
                inicia_vez(jogadores[id_jogador])
                termina_vez(jogadores[id_jogador])
            rodada = rodada + 1
            print("".center(48, "#"))


def termina_jogo():
    print("\n")
    print(" FIM DE JOGO ".center(48, "#"))
    print("\n")
    exit(0)

def inicia_vez(jogador):
        print("\n\n")
        print(" VEZ DO JOGADOR %s ".center(48, "-") % jogador["nome"].upper())

        for i in range(3):
        dados = []

            if i == 0:
                dados = joga_dado(5)

            else:
                j = 0
                d_escolhidos = []

                print(dados)

                d_escolhidos = (input_handler(input(
                    "Escolha quais dados quer relancar separados por espaco ou digite 0 para terminar acao: "), str)).split()
                if d_escolhidos[0] == '0':
                    categoria = input_handler(input("Escolha a categoria de pontuacao: "), str)
                    pontos = pnt_pontua(categoria, dados)
                    pnt_atualiza_pontuacao(jogador["nome"], categoria, pontos)
                    return
                else:
                    novos_val = joga_dado(len(d_escolhidos))
                    for numbers in d_escolhidos:
                        d_escolhidos[j] = int(numbers) - 1
                        dados[d_escolhidos[j]] = novos_val[j]
                        j = j + 1
        print(dados)
        categoria = input_handler(input("Escolha a categoria de pontuacao: "), str)
        pontos = pnt_pontua(categoria,dados)
        pnt_atualiza_pontuacao(jogador["nome"], categoria, pontos)


def termina_vez(jogador):
    tab_print()
    print("".center(48, "-"))

jogadores = {}
init()
