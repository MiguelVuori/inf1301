from tkinter import *
from tkinter import messagebox
from partida import *
sys.path.insert(1, 'dado')
import dadoView as dv

def add_player(enNome):
    nome = enNome.get()
    ptd_adiciona_player(nome)
    messagebox.showinfo("Inclusão Efetuada")

def joga_dados():
    dv.inicia_view()
