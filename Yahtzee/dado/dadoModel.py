import random

__all__ = ['joga_dado', 'pega_dados']

def init():
    global dados
    global retries
    retries = 0
    dados = {}
    for i in range(0, 5):
        dados[i] = {'dado': None, 'selected': False, 'img': None, 'rect': None, 'x1': 15.0+96*i, 'x2': 48.0+96*i}
    random.seed()


def numeros_aleatorios(n_dados):
    res = []
    for i in range(n_dados):
        res.append(random.randint(1,6))
    return res 

def joga_dados(lista_de_indices):
    N = len(lista_de_indices)
    rands = numeros_aleatorios(N)
    rand_i = 0
    for indice in lista_de_indices:
        dados[indice]['dado'] = rands[rand_i]
        rand_i += 1
    return dados
    
def pega_dados():
    return dados

def pega_dados_int():
    dados = pega_dados()
    arr = []
    for dado in dados.values():
        arr.append(dado['dado'])
    return arr

init()