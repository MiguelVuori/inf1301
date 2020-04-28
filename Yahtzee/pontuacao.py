from jogador import Jogador
from dado import *

__all__ = ['pontua', 'atualiza_pontuacao', 'soma_pontuacao', 'testa_bonus', 'mostra_tabela']



def init():
    pass
    
def pontua(jogador):
    pass

def atualiza_pontuacao(jogador, pontos):
    jogador.adiciona_pontos()

def soma_pontuacao(jogador):
    pass

def testa_bonus(jogador):
    pass

def mostra_tabela(jogador): # Fiz printando só a lista toda, sem lógica
    print("------")
    print("Pontuação: ")
    print(jogador.pontuacao)
