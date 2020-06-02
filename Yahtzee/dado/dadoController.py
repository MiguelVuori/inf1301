from dadoModel import Model
from dadoView import View

class Dado():
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self.model, self.joga_dados, self.bloqueia)
        self.view.define_botoes_inicio()
        self.view.redefine_label_relancamento(self.model.jogadas)

    def joga_dados(self):
        if self.model.jogadas == 0:
            self.model.joga_dados([0,1,2,3,4])
            self.view.joga_dados(self.model, [0,1,2,3,4])
            self.model.jogadas += 1
            self.view.redefine_botoes_relancamento()
            self.view.redefine_label_relancamento(self.model.jogadas)
        elif self.model.jogadas < 3:
            selecionados = []
            i = 0
            for dado in self.model.dados.values():
                if dado['selected']:
                    selecionados.append(i)
                i += 1
            self.model.joga_dados(selecionados)
            self.view.joga_dados(self.model, selecionados)
            self.model.jogadas += 1
            self.view.redefine_label_relancamento(self.model.jogadas)
            if self.model.jogadas == 3:
                self.view.redefine_botoes_termino()
                self.view.redefine_label_relancamento(self.model.jogadas)
                self.view.atualiza_dados(self.model, [0,1,2,3,4])

    def retorna_dados(self):
        return self.model.pega_dados_int()
    
    def retorna_bloqueado(self):
        return self.model.bloqueado

    def bloqueia(self):
        self.model.bloqueado = True
        self.view.redefine_botoes_bloqueio()
        self.view.redefine_label_relancamento(self.model.jogadas)

    def reinicia(self):
        self.model.redefine_model()
        self.view.reinicia()
