import random

class Model():
    def __init__(self):
        self.bloqueado = False
        self.jogadas = 0
        self.dados = {}
        for i in range(0, 5):
            self.dados[i] = {'dado': None, 'selected': False, 'img': None, 'rect': None, 'x1': 15.0+96*i, 'x2': 48.0+96*i}
        random.seed()

    def numeros_aleatorios(self, n_dados):
        res = []
        for i in range(n_dados):
            res.append(random.randint(1,6))
        return res 

    def joga_dados(self, lista_de_indices):
        N = len(lista_de_indices)
        rands = self.numeros_aleatorios(N)
        rand_i = 0
        for indice in lista_de_indices:
            self.dados[indice]['dado'] = rands[rand_i]
            rand_i += 1
    
    def seleciona_dados(self, dados):
        i = 0
        for dado in self.dados.values():
            dado['dado'] = dados[i]
            i += 1

    def pega_dados(self):
        return self.dados

    def pega_dados_int(self):
        arr = []
        for dado in self.dados.values():
            arr.append(dado['dado'])
        return arr

    def redefine_model(self):
        self.bloqueado = False
        self.jogadas = 0
        self.dados = {}
        for i in range(0, 5):
            self.dados[i] = {'dado': None, 'selected': False, 'img': None, 'rect': None, 'x1': 15.0+96*i, 'x2': 48.0+96*i}
