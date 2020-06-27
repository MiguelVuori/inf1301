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
criterios = [
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
rodada = 0

# ----- Funções de callback -----
def trataNome(enNome):
    nome = enNome.get()

    for letra in nome:
        if letra != " " and not letra.isalpha():
            return False
    return True

def add_player(nome):
    global Tabelas_Superiores
    objetoJogador = Tabela(nome)
    Todas_Tabelas.append([nome, objetoJogador])

def joga_dados():
    global dado
    dadoToplevel = tk.Toplevel()
    dado = Dado(dadoToplevel)
    root.after(250, checa_termino_jogada)


def mostra_tabela():
    for vet in Todas_Tabelas:
        if True:
            objetoJogador = vet[1]
    upper = TabelaSuperior(tk.Toplevel(), objetoJogador)
    lower = TabelaInferior(tk.Toplevel(), objetoJogador)
    upper.display()
    lower.display()
    

def fecha_Cadastro(root):
    root.destroy()
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Yahtzee")

    # ----- Criação do botão de jogar dado -----

    btJogaDado = tk.Button(root, text = "Rolar os Dados", width = 15)
    btJogaDado.place(x = 135, y = 200)
    btJogaDado.config(command = lambda: joga_dados())

    # ----- Ver tabela -----

    btTabela = tk.Button(root, text = "Ver Tabela", width = 15)
    btTabela.place(x = 135, y = 175)
    btTabela.config(command = lambda: mostra_tabela())




# ----- Fim das funcoes de callback -----

def checa_termino_jogada():
    global rodada
    if dado.retorna_bloqueado():
        dados = dado.retorna_dados()
        dropdown_root = tk.Toplevel()
        dropdown_root.geometry("175x100")
        dropdown_root.title("Critério")
        criterio_escolhido = tk.StringVar(dropdown_root)
        criterio_escolhido.set(criterios[0])
        dropdown_text = tk.Label(dropdown_root, text="Escolha um critério").pack()
        dropdown = tk.OptionMenu(dropdown_root, criterio_escolhido, *criterios).pack()
        dropdown_button = tk.Button(dropdown_root, text="Confirmar", command=dropdown_root.destroy).pack()
        dropdown_root.wait_window(dropdown_root)
        escolhido = criterio_escolhido.get()
        pontos = pnt_pontua(escolhido, dados)
        Todas_Tabelas[0][1].insere(escolhido, pontos, rodada) # trocar os indices aqui
        criterios.remove(escolhido)
        dado.reinicia()
        rodada += 1

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
