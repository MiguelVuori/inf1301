import sys

sys.path.insert(1, 'dado/')
sys.path.insert(1, 'pontuacao/')
sys.path.insert(1, 'tabela/')

import tkinter as tk
from dadoController import Dado
from pontuacao import *
from tabelaSuperiorController import TabelaSuperior
from tabelaInferiorController import TabelaInferior

def checa_termino_jogada():
    if dado.retorna_bloqueado():
        dados = dado.retorna_dados()
        categoria = input("Escolha a categoria de pontuacao: ")
        pontos = pnt_pontua(categoria,dados)
        dado.reinicia()

    root.after(250, checa_termino_jogada)

root = tk.Tk()

dadoToplevel = tk.Toplevel()
tabelaInferiorToplevel = tk.Toplevel()
tabelaSuperiorToplevel = tk.Toplevel()


dado = Dado(dadoToplevel)
tabelaInferior = TabelaInferior(tabelaInferiorToplevel)
tabelaSuperior = TabelaSuperior(tabelaSuperiorToplevel)


root.after(250, checa_termino_jogada)
root.mainloop()