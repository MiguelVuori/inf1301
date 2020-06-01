from tabelaModel import Tabela
from tabelaSuperiorView import ViewSuperior


class TabelaSuperior():
    def __init__(self, root, tabela):
        self.tabela = tabela
        self.root = root

    
    def display(self):
        self.view = ViewSuperior(self.root, self.tabela)
        self.view.mostra()

    def redisplay(self):
        self.view.update()
        self.view.mostra()

