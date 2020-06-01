from tabelaModel import Tabela
from tabelaSuperiorView import ViewSuperior


class TabelaSuperior():
    def __init__(self, root):
        self.tabela = Tabela('Lucas')
        self.view = ViewSuperior(root, self.tabela)
        self.view.mostra()


