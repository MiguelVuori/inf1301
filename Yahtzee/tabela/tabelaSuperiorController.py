from tabelaModel import Tabela
from tabelaSuperiorView import View


class TabelaSuperior():
    def __init__(self, root, tabela):
        self.tabela = tabela
        self.root = root

    
    def display(self):
        self.view = View(self.root, self.tabela)
        self.view.update()
        self.view.mostra()

    #def redisplay(self): caso a gente queira fazer atualização enquanto a tabela estiver aberta a gente faz por aqui
    #    

