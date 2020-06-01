from tabelaModel import Tabela
from tabelaInferiorView import ViewInferior

class TabelaInferior():
    def __init__(self, root, tabela):
        self.tabela = tabela
        self.root = root
    
    
    def display(self):
        self.view = ViewInferior(self.root, self.tabela)
        self.view.mostra()

    def redisplay(self):
        self.view.update()
        self.view.mostra()