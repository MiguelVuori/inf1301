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
        if (trinca == 0):
            print("Critério Quadra não aceito")
            return False
        else:
            for i in range(5):
                pontos += res[i]
    elif (criterio == 'Full House'):
        pontos = 0
    elif (criterio == 'Sequência Mínima'):
        pontos = 0
    elif (criterio == 'Sequência Máxima'):
        res.sort()
        for i in range(4):
            if res[i] != res[i+1]+1:
                print("Critério Sequência Máximo não aceito")
                return False
            else:
                pontos += res[i]
        pontos += res[4]
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