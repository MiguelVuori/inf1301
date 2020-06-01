
class Tabela():

    def __init__(self , nome):
        self.jogador = nome

        self.tabela = {
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

    def insere(self,campo,valor):
        if (campo in self.tabela) and (self.tabela[campo] == 0):
            self.tabela[campo] = valor
            return True
        else:
            return False

    def get(self,campo):
        if (campo in self.tabela):
            return self.tabela[campo]

    def reinicia(self):
        self.tabela = {
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

    def soma_pontuacao(self, indesejados):
        soma = 0

        for campo in self.tabela:
            if campo not in indesejados:
                soma += self.tabela[campo]
        return soma

    def get_nome(self):
        return self.jogador

    def checa_bonus_superior(self):
        soma = 0
        
        if self.soma_pontuacao(["Bônus_sup","Trinca","Quadra","Full House","Sequência Mínima","Sequência Máximo","YAHTZEE","Bônus_YAHTZEE","Total"]) >= 63:
            return True
        else:
            return False

        
    def checa_bonus_inferior(self):
        if self.get("YAHTZEE") == 0:
            return False
        else:
            return True

        