from tabelaModel import Tabela
from tabelaInferiorView import ViewInferior

class TabelaInferior():
    def __init__(self, root):
        self.tabela = Tabela('Lucas')
        self.view = ViewInferior(root, self.tabela)
        self.view.mostra()
