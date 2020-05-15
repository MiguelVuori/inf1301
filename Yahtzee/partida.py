from dado import *
from pontuacao import *
from utils import *

__all__ = ['cria_jogo', 'inicia_jogo', 'termina_jogo', 'inicia_vez', 'termina_vez']



def init():
    global jogadores
    global tabela
    tabela = {'Um': [False, 0], 'Dois': [False, 0], 'Três': [False, 0], 'Quatro': [False, 0], 'Cinco': [False, 0], 'Seis': [False, 0],
    'Total Seção Superior': 0, 'Bônus': False, 'Trinca': [False, 0], 'Quadra': [False, 0], 'Full House': [False, 0], 'Sequência Mínimo': [False, 0],
    'Sequência Máxima': [False, 0], 'YAHTZEE': False, 'Chance': [False, 0], 'Bônus Yahtzee': 0, 'Total Seção Inferior': 0} 
    
def cria_jogo():
    print("\nUse 'quit' como input para terminar o jogo\n")
    n_jogadores = input_handler(input("Número de jogadores: "), int)
    for n in range (0, n_jogadores):
        id = n + 1
        nome = input_handler(input("Nome do jogador %d: " % id), str)
        jogadores[id] = {
            'nome': nome,
            'tabela': tabela
            #'pontuacao' : 0
        }

def inicia_jogo():
        rodada = 1
        while True:
            print("\n\n")
            print(" RODADA %d ".center(48, "#") % rodada)
            for id_jogador in jogadores:
                inicia_vez(jogadores[id_jogador])
                termina_vez(jogadores[id_jogador])
            rodada = rodada + 1
            print("".center(48, "#"))


def termina_jogo():
    print("\n")
    print(" FIM DE JOGO ".center(48, "#"))
    print("\n")
    exit(0)

def inicia_vez(jogador):
        print("\n\n")
        print(" VEZ DO JOGADOR %s ".center(48, "-") % jogador["nome"].upper())

        for i in range(3):
        dados = []

            if i == 0:
                dados = joga_dado(5)

            else:
                j = 0
                d_escolhidos = []

                print(dados)

                d_escolhidos = (input_handler(input(
                    "Escolha quais dados quer relancar separados por espaco ou digite 0 para terminar acao: "), str)).split()
                if d_escolhidos[0] == '0':
                    atualiza_pontuacao(jogador, dados)
                    return
                else:
                    novos_val = joga_dado(len(d_escolhidos))

                    for numbers in d_escolhidos:
                        d_escolhidos[j] = int(numbers)
                        dados[d_escolhidos[j]] = novos_val[j]]
                        j = j + 1
                        
        categoria = input_handler(input("Escolha a categoria de pontucao: "), str)
        pontua(categoria,dados)


def termina_vez(jogador):
    mostra_tabela(jogador)
    print("".center(48, "-"))

jogadores = {}
init()