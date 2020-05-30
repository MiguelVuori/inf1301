from partida import *
from pontuacao import *
from dado import *
from utils import *
from viwer import *
from tkinter import *

global inCadastro 
inCadastro = True
#cria_jogo()
#inicia_jogo()

root = Tk()


cria_janela_cadastro(root, inCadastro)

root.mainloop()



