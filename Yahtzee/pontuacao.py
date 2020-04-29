from dado import *

__all__ = ['pontua', 'atualiza_pontuacao', 'soma_pontuacao', 'testa_bonus', 'mostra_tabela']



def init():
    pass
    
def pontua(jogador):
    pass

def atualiza_pontuacao(jogador, pontos):
    jogador["pontuacao"] += pontos

def soma_pontuacao(jogador):
    pass

def testa_bonus(jogador):
    pass

def mostra_tabela(jogador):
    print("\n")
    print("Pontuação:".center(48, " "))
    print("%d".center(48, " ") % jogador["pontuacao"])

init()