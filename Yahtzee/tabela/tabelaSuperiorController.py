from tabelaModel import Tabela
from tabelaSuperiorView import ViewSuperior
from tkinter import messagebox


class TabelaSuperior():
    def __init__(self, root , nome):
        self.tabela = Tabela(nome)
        self.view = ViewSuperior(root, self.tabela)
        self.view.mostra()

        messagebox.showinfo("Inclusão Efetuada")


