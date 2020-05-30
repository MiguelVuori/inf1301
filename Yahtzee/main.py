# ESSE ARQUIVO DEVERIA SER O PARTIDA.PY MAS FIZ AQUI, POR ISSO SEPAREI DE BRANCH

import sys

sys.path.insert(1, 'dado/')
sys.path.insert(1, 'pontuacao/')

import tkinter as tk
from dadoController import Controller
from pontuacao import *

def checa_termino_jogada():              # Sem essa função a gente não consegue retornar o "resultado"
    if dado.retorna_bloqueado():         # final da jogada sem fechar a view dos dados, achei que ficaria
        dados = dado.retorna_dados()     # mais bonito se fosse feito assim.
        print(dados)
        categoria = input("Escolha a categoria de pontuacao: ")
        pontos = pnt_pontua(categoria,dados)
        print(pontos)
        dado.reinicia()

    root.after(250, checa_termino_jogada) # checa a cada 250 ms se o round terminou

root = tk.Tk()
dado = Controller(root)

root.after(250, checa_termino_jogada)
root.mainloop()