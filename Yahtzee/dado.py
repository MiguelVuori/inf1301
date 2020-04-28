import random

__all__ = ['joga_dado']

def init():
    random.seed()

def joga_dado():
    res = []
    print("------")
    n_dados = int(input("Número de dados a ser jogado: "))
    while(n_dados < 1 or n_dados > 5):
        print("------")
        print("Erro: número de dados a serem lançados tem que ser um inteiro de 1 a 5")
        print("------")
        n_dados = int(input("Número de dados a ser jogado: "))
    for dado in range(0, n_dados):
        res.append(random.randint(1,6))
    return res