
class Tabela():

    def __init__(self , nome):
        self.jogador = nome

        self.tabela = {
        "Um": [0,0,0,0,0,0],
        "Dois": [0,0,0,0,0,0],
        "Três": [0,0,0,0,0,0],
        "Quatro": [0,0,0,0,0,0],
        "Cinco": [0,0,0,0,0,0],
        "Seis": [0,0,0,0,0,0],
        "PONTUAÇÃO TOTAL": [0,0,0,0,0,0],
        "Bônus_sup": [0,0,0,0,0,0],
        "TOTAL (Da seção superior)": [0,0,0,0,0,0],
        "Trinca": [0,0,0,0,0,0],
        "Quadra": [0,0,0,0,0,0],
        "Full House": [0,0,0,0,0,0],
        "Sequência Mínima": [0,0,0,0,0,0],
        'Sequência Máxima': [0,0,0,0,0,0],
        "YAHTZEE": [0,0,0,0,0,0],
        "Chance": [0,0,0,0,0,0],
        "BÔNUS YAHTZEE": [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
        "TOTAL (da seção inferior)": [0,0,0,0,0,0],
        "TOTAL (da seção superior)": [0,0,0,0,0,0],
        "TOTAL GERAL": [0,0,0,0,0,0]
        }

    def get_tabela(self):
        return self.tabela


    def insere(self,campo,valor,rodada):
        if (campo in self.tabela) and (self.tabela[campo][rodada] == 0):
            
            # ----- Verifica se inseriu em cima -----
            if(campo in {"Um","Dois","Três","Quatro","Cinco","Seis"}):
                self.tabela[campo][rodada] = valor
                total = self.soma_pontuacao({"Um","Dois","Três","Quatro","Cinco","Seis"}, rodada)
                self.insere("PONTUAÇÃO TOTAL", total, rodada)
                if self.checa_bonus_superior(rodada) == True:
                    total += 35
                    self.insere("BÔNUS", 1, rodada)               
                self.insere("TOTAL (Da seção superior)", total , rodada)
                self.insere("TOTAL (da seção superior)", total, rodada)
                self.insere("TOTAL GERAL", total + self.get("TOTAL (da seção inferior)", rodada), rodada)
            # ----- Inseriu embaixo -----
            elif (campo in {"Trinca","Quadra","Full House","Sequência Mínima","Sequência Máximo","Chance","YAHTZEE"}):
                total = 0
                if(campo == "YAHTZEE"):
                    if self.checa_bonus_inferior(rodada) == True:
                        total += 100
                    else:
                        self.tabela[campo][rodada] = 50
                else:
                    self.tabela[campo][rodada] = valor
                total += self.soma_pontuacao({"Trinca","Quadra","Full House","Sequência Mínima","Sequência Máximo","Chance","YAHTZEE"}, rodada)
                self.insere("TOTAL (da seção inferior)", total, rodada)
                self.insere("TOTAL GERAL", total + self.get("TOTAL (Da seção superior)", rodada), rodada)
            else:
                self.tabela[campo][rodada] = valor
            return True
        else:
            return False

    def load(self,nova_tabela):
        self.tabela = nova_tabela

    def get(self,campo, rodada):
        if (campo in self.tabela):
            return self.tabela[campo][rodada]

    def reinicia(self):
        self.tabela = {
        "Um": [0,0,0,0,0,0],
        "Dois": [0,0,0,0,0,0],
        "Três": [0,0,0,0,0,0],
        "Quatro": [0,0,0,0,0,0],
        "Cinco": [0,0,0,0,0,0],
        "Seis": [0,0,0,0,0,0],
        "PONTUAÇÃO TOTAL": [0,0,0,0,0,0],
        "Bônus_sup": [0,0,0,0,0,0],
        "TOTAL (Da seção superior)": [0,0,0,0,0,0],
        "Trinca": [0,0,0,0,0,0],
        "Quadra": [0,0,0,0,0,0],
        "Full House": [0,0,0,0,0,0],
        "Sequência Mínima": [0,0,0,0,0,0],
        'Sequência Máxima': [0,0,0,0,0,0],
        "YAHTZEE": [0,0,0,0,0,0],
        "Chance": [0,0,0,0,0,0],
        "BÔNUS YAHTZEE": [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
        "TOTAL (da seção inferior)": [0,0,0,0,0,0],
        "TOTAL (da seção superior)": [0,0,0,0,0,0],
        "TOTAL GERAL": [0,0,0,0,0,0]
        }

    def soma_pontuacao(self, desejados, rodada):
        soma = 0
        for campo in self.tabela:
            if campo  in desejados:
                soma += self.tabela[campo][rodada]
        return soma

    def get_nome(self):
        return self.jogador

    def checa_bonus_superior(self, rodada):
        #if self.soma_pontuacao({"Bônus_sup","Trinca","Quadra","Full House","Sequência Mínima","Sequência Máximo","YAHTZEE","Bônus_YAHTZEE","Total"}) >= 63:
        if self.soma_pontuacao(["Um", "Dois", "Três", "Quatro", "Cinco", "Seis"], rodada) >= 63:
            return True
        else:
            return False

        
    def checa_bonus_inferior(self, rodada):
        if self.get("YAHTZEE") == 0:
            return False
        else:
            return True

        