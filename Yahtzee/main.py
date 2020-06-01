import sys

sys.path.insert(1, 'dado/')
sys.path.insert(1, 'pontuacao/')

import tkinter as tk
from dadoController import Dado
from pontuacao import *

def checa_termino_jogada():
    if dado.retorna_bloqueado():
        dados = dado.retorna_dados()
        categoria = input("Escolha a categoria de pontuacao: ")
        pontos = pnt_pontua(categoria,dados)
        dado.reinicia()

    root.after(250, checa_termino_jogada)

root = tk.Tk()

dado = Dado(tk.Toplevel())

root.after(250, checa_termino_jogada)
root.mainloop()