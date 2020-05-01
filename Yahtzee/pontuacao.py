from dado import *

__all__ = ['pontua', 'atualiza_pontuacao', 'soma_pontuacao', 'testa_bonus', 'mostra_tabela','tabela']



def init()

def pontua(criterio, res):
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

def atualiza_pontuacao(jogador, pontos):
    jogador["pontuacao"] += pontos

def soma_pontuacao(jogador):
    pass

def testa_bonus(jogador):
    pass

def mostra_tabela(jogador):
    print("\n")
    print("Pontuação:".center(48, " "))
    print("%d".center(48, " ") % jogador["pontuacao"])

init()