from jogador import Jogador
from dado import *
from pontuacao import *

__all__ = ['cria_jogo', 'inicia_jogo', 'termina_jogo', 'inicia_vez', 'termina_vez']



def init():
    global jogadores

def cria_jogo(n_jogadores):
    for n in range (0, n_jogadores):
        jogadores.append(Jogador(n))

def inicia_jogo():
    for jogador in jogadores:
        inicia_vez(jogador)
        termina_vez(jogador)

def termina_jogo():
    pass

def inicia_vez(jogador):
    print("\n\nVez do jogador %s"%jogador.id)
    jogador.pontuacao.append(joga_dado())

def termina_vez(jogador):
    mostra_tabela(jogador)
    print("---------------")
    
jogadores = []
init()