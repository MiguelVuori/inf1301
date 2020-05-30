import sys
sys.path.insert(1, '../TADtabela/')
#from dado import *
from tabela import *

__all__ = ['pnt_pontua', 'pnt_atualiza_pontuacao', 'pnt_soma_pontuacao', 'pnt_testa_bonus', 'pnt_mostra_tabela']


def init():
    global criterios
    criterios = []
    #tab_ins(criterios,[0,0,0,0,0,0,0,0,0,0,0,0])

def pnt_pontua(criterio, res):
    pontos = 0
    if (criterio == 'Um'):
        for i in range(5):
            if res[i] == 1:
                pontos += 1

    elif (criterio == 'Dois'):
        for i in range(5):
            if res[i] == 2:
                pontos += 2

    elif (criterio == 'Três'):
        for i in range(5):
            if res[i] == 3:
                pontos += 3

    elif (criterio == 'Quatro'):
        for i in range(5):
            if res[i] == 4:
                pontos += 4

    elif (criterio == 'Cinco'):
        for i in range(5):
            if res[i] == 5:
                pontos += 5

    elif (criterio == 'Seis'):
        for i in range(5):
            if res[i] == 6:
                pontos += 6

    elif (criterio == 'Trinca'):
        trinca = 0
        res.sort()
        for i in range(3):
            if (res[i] == res[i+1] == res[i+2]):
                trinca = 1
        if (trinca == 0):
            print("Critério Trinca não aceito")
            return False
        else:
            for i in range(5):
                pontos += res[i]
    elif (criterio == 'Quadra'):
        quadra = 0
        res.sort()
        for i in range(3):
            if (res[i] == res[i+1] == res[i+2]):
                quadra = 1
        if (quadra == 0):
            print("Critério Quadra não aceito")
            return False
        else:
            for i in range(5):
                pontos += res[i]
    elif (criterio == 'Full House'):
        tmp = res
        if tmp.count(tmp[0]) == 3:
            tmp[:] = (value for value in tmp if value != tmp[0])
            if tmp.count(tmp[0]) == 2:
                pontos += 25
            else:
                return False
        elif tmp.count(tmp[0] == 2):
            tmp[:] = (value for value in tmp if value != tmp[0])
            if tmp.count(tmp[0]) == 3:
                pontos += 25
            else:
                return False
        else:
            return False
    elif (criterio == 'Sequência Mínima'):
        res.sort()
        count = 0
        for i in range(0,4):
            if res[i+1] == res[i] + 1:
                count += 1
            if count == 3:
                pontos += 30
        if count < 3:
            return False
    elif (criterio == 'Sequência Máxima'):
        res.sort()
        count = 0
        for i in range(0,4):
            if res[i+1] == res[i] + 1:
                count += 1
            if count == 4:
                pontos += 40
        if count < 4:
            return False
    elif (criterio == 'YAHTZEE'):
        soma = 0
        for i in range(len(res)):
            soma += res[i]
        if (soma != res[i]*5):
            print("Critério YAHTZEE não aceito")
            return False
        else:
            pontos = soma
    elif (criterio == 'Chance'):
        for i in range(5):
            pontos += res[i]  
    return pontos

def pnt_atualiza_pontuacao(jogador, criterio, pontos):
    tab_ins([jogador,criterio],pontos)

#soma pontuacao ate a parada desejada menos a lista de campos não desejados
def pnt_soma_pontuacao(jogador,parada,lista = []):
    soma = 0

    for campo in tab_get(jogador):
        if campo not in (lista):
            soma += tab_get(jogador,campo)
            if campo == parada:
                break

    return soma

#Testa se existe bonus superior ou inferior retorna true ou false
def pnt_testa_bonus(jogador,tipo):
    soma = 0

    if tipo == "superior":
        soma = pnt_soma_pontuacao(jogador,"Seis")
        if soma >= 63:
            return True
        else:
            return False
    elif tipo == "inferior":
        if tab_get(jogador,'YAHTZEE') == 0:
            return False
        else:
            return True
    pass

def pnt_mostra_tabela(jogador):
    print("\n")
    print("Pontuação:".center(48, " "))
    print("%d".center(48, " ") % jogador["pontuacao"])

init()