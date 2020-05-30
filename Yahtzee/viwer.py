from partida import *
from tkinter import *
import controller_partida
import sys

__all__ = ["cria_janela_cadastro"]

def fecha_Cadastro(root):
    root.destroy()
    root = Tk()
    root.geometry("400x400")
    root.title("Yahtzee")

    # ----- Criação do botão de jogar dado -----

    btJogaDado = Button(root, text = "Rola os Dados", width = 15)
    btJogaDado.place(x = 135, y = 200)
    btJogaDado.config(command = lambda: controller_partida.joga_dados())

    # ----- Ver tabela -----

    btTabela = Button(root, text = "Ver Tabela", width = 15)
    btTabela.place(x = 135, y = 175)
    btTabela.config(command = lambda: controller_partida.mostra_tabela())


    

# ----- Função para de callback na inserção dos jogadores -----
def trataNome(enNome):
    nome = enNome.get()

    for letra in nome:
        if letra != " " and not letra.isalpha():
            return False
    return True

def cria_janela_cadastro(root,inCadastro):
    # ----- Criação da janela secundaria -----
    root.geometry("400x400")
    root.title("Cadastro dos jogadores")

    # ----- Entrada dos nomes -----

    lbNome = Label(root, text = "Nome", width = 12 , anchor = "w")
    lbNome.place(x = 10, y = 50)
    enNome = Entry(root, width = 10)
    enNome.focus_set()
    enNome.config(validate = "focusout", validatecommand = lambda: trataNome(enNome))
    enNome.place(x = 75, y = 50)

    # ----- Criação do botão de inclusão -----

    btInclui = Button(root, text = "Incluir", width = 15)
    btInclui.place(x = 50, y = 350)
    btInclui.config(command = lambda: controller_partida.add_player(enNome))

    # ----- Criação do botão de finalizar cadastro e continuar para o jogo-----

    btContinua = Button(root, text = "Continuar", width = 15)
    btContinua.place(x = 200, y = 350)
    btContinua.config(command = lambda: fecha_Cadastro(root))

