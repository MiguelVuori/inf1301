import random
from utils import *

__all__ = ['joga_dado']

def init():
    random.seed()

def soma_pontos(pontos):
    soma = 0
    for ponto in pontos:
        soma += ponto
    return soma

def joga_dado():
    res = []
    n_dados = input_handler(input("Número de dados a ser jogado: "), int)
    while(n_dados < 1 or n_dados > 5):
        print("\nERRO: número de dados a serem lançados tem que ser um inteiro de 1 a 5\n")
        n_dados = input_handler(input("Número de dados a ser jogado: "), int)
    for dado in range(0, n_dados):
        res.append(random.randint(1,6))
    return soma_pontos(res)

init()