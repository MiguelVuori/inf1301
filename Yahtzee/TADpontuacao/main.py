import sys
sys.path.insert(1, '../TADtabela/')
from tabela import *
from pontuacao import *

criterios = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Trinca", "Quadra", "Full House", "Sequência Mínima", "Sequência Máxima", "Chance"]
lista_nomes = ["miguel","lucas","gabriel"]
tabela_Y = {
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
for nome in lista_nomes:

    tab_ins(nome,tabela_Y)

print("\n\n\n")
tab_print()
print("\n\n\n")

pontos = 0
for i in range(1,6):

    pontos = pnt_pontua(criterios[i-1],[i,i,i,i,i])
    pnt_atualiza_pontuacao("miguel",criterios[i-1],pontos)

pontos = pnt_pontua("YAHTZEE",[6,6,6,6,6])
pnt_atualiza_pontuacao("miguel","YAHTZEE",pontos)

tab_print()
print(pnt_testa_bonus("miguel","superior"))

