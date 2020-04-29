from dado import *
from pontuacao import *
from utils import *

__all__ = ['cria_jogo', 'inicia_jogo', 'termina_jogo', 'inicia_vez', 'termina_vez']



def init():
    global jogadores

def cria_jogo():
    print("\nUse 'quit' como input para terminar o jogo\n")
    n_jogadores = input_handler(input("Número de jogadores: "), int)
    for n in range (0, n_jogadores):
        id = n + 1
        nome = input_handler(input("Nome do jogador %d: " % id), str)
        jogadores[id] = {
            'nome': nome,
            'pontuacao' : 0
        }

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

        atualiza_pontuacao(jogador, joga_dado())


def termina_vez(jogador):
    mostra_tabela(jogador)
    print("".center(48, "-"))

jogadores = {}
init()