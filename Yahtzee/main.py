import sys

sys.path.insert(1, 'dado/')
sys.path.insert(1, 'pontuacao/')
sys.path.insert(1, 'tabela/')

import tkinter as tk
from dadoController import Dado
from pontuacao import *
from tabelaModel import Tabela
from tabelaSuperiorController import TabelaSuperior
from tabelaInferiorController import TabelaInferior

# ----- Variaveis Globais -----

Todas_Tabelas = []
rodada = 0
jogador_atual = 0
n_jogadores = 0

# ----- Funções de callback -----
def trataNome(enNome):
    nome = enNome.get()

    for letra in nome:
        if letra != " " and not letra.isalpha():
            return False
    return True

def add_player(nome):
    global n_jogadores
    global criterios_jogador
    n_jogadores += 1
    objetoJogador = Tabela(nome)
    Todas_Tabelas.append([nome, 
                          objetoJogador,
                          [
                            "Um",
                            "Dois",
                            "Três",
                            "Quatro",
                            "Cinco",
                            "Seis",
                            "Trinca",
                            "Quadra",
                            "Full House",
                            "Sequência Mínima",
                            'Sequência Máxima',
                            "YAHTZEE",
                            "Chance"
                            ]
                        ])

def joga_dados():
    global dado
    dadoToplevel = tk.Toplevel()
    dado = Dado(dadoToplevel)
    root.after(250, checa_termino_jogada)


def mostra_tabela(jogador):
    lista_jogadores = []
    for jogador in Todas_Tabelas:
        lista_jogadores.append(jogador[0])
    dropdown_root = tk.Toplevel()
    dropdown_root.geometry("175x100")
    dropdown_root.title("Jogador")
    jogador_escolhido = tk.StringVar(dropdown_root)
    jogador_escolhido.set(lista_jogadores[jogador_atual])
    dropdown_text = tk.Label(dropdown_root, text="Escolha um jogador").pack()
    dropdown = tk.OptionMenu(dropdown_root, jogador_escolhido, *lista_jogadores).pack()
    dropdown_button = tk.Button(dropdown_root, text="Confirmar", command=dropdown_root.destroy).pack()
    dropdown_root.wait_window(dropdown_root)
    escolhido = lista_jogadores.index(jogador_escolhido.get())
    objetoJogador = Todas_Tabelas[escolhido][1]
    upper = TabelaSuperior(tk.Toplevel(), objetoJogador)
    lower = TabelaInferior(tk.Toplevel(), objetoJogador)
    upper.display()
    lower.display()
    

def fecha_Cadastro(root):
    root.destroy()
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Yahtzee")

    # ----- Label exibindo nome e rodada atual -----
    string_jogador = "Jogador atual: {0}".format(Todas_Tabelas[jogador_atual][0])
    string_rodada = "Rodada: {0}".format(rodada)
    label_jogador = tk.Label(root, text=string_jogador).pack()
    label_rodada = tk.Label(root, text=string_rodada).pack()

    # ----- Criação do botão de jogar dado -----

    btJogaDado = tk.Button(root, text = "Rolar os Dados", width = 15)
    btJogaDado.place(x = 135, y = 200)
    btJogaDado.config(command = lambda: joga_dados())

    # ----- Ver tabela -----

    btTabela = tk.Button(root, text = "Ver Tabela", width = 15)
    btTabela.place(x = 135, y = 175)
    btTabela.config(command = lambda: mostra_tabela(jogador_atual))




# ----- Fim das funcoes de callback -----

def checa_termino_jogada():
    global rodada
    global criterios_jogador
    global jogador_atual
    if dado.retorna_bloqueado():
        dados = dado.retorna_dados()
        dropdown_root = tk.Toplevel()
        dropdown_root.geometry("175x100")
        dropdown_root.title("Critério")
        criterio_escolhido = tk.StringVar(dropdown_root)
        criterio_escolhido.set(Todas_Tabelas[jogador_atual][2][0])
        dropdown_text = tk.Label(dropdown_root, text="Escolha um critério").pack()
        dropdown = tk.OptionMenu(dropdown_root, criterio_escolhido, *Todas_Tabelas[jogador_atual][2]).pack()
        dropdown_button = tk.Button(dropdown_root, text="Confirmar", command=dropdown_root.destroy).pack()
        dropdown_root.wait_window(dropdown_root)
        escolhido = criterio_escolhido.get()
        pontos = pnt_pontua(escolhido, dados)
        Todas_Tabelas[jogador_atual][1].insere(escolhido, pontos, rodada)
        Todas_Tabelas[jogador_atual][2].remove(escolhido)
        dado.reinicia()
        if jogador_atual < n_jogadores - 1:
            jogador_atual += 1
        elif jogador_atual == n_jogadores - 1:
            rodada += 1
            jogador_atual = 0
        if rodada == 5:
            pass # termina a partida

    root.after(250, checa_termino_jogada)
# ---- Inicialização das Janelas -----

root = tk.Tk()

# ----- Criação da janela -----
root.geometry("400x400")
root.title("Cadastro dos jogadores")

# ----- Entrada dos nomes -----

lbNome = tk.Label(root, text = "Nome", width = 12 , anchor = "w")
lbNome.place(x = 10, y = 50)
enNome = tk.Entry(root, width = 10)
enNome.focus_set()
enNome.config(validate = "focusout", validatecommand = lambda: trataNome(enNome))
enNome.place(x = 75, y = 50)

# ----- Criação do botão de inclusão -----

btInclui = tk.Button(root, text = "Incluir", width = 15)
btInclui.place(x = 50, y = 350)
btInclui.config(command = lambda: add_player(enNome.get()))

# ----- Criação do botão de finalizar cadastro e continuar para o jogo-----

btContinua = tk.Button(root, text = "Continuar", width = 15)
btContinua.place(x = 200, y = 350)
btContinua.config(command = lambda: fecha_Cadastro(root))

# ----- Fim da criação do cadastro -----



root.mainloop()
