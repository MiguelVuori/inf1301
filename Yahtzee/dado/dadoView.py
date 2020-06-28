import tkinter as tk
from random import randint
import time

class View():
    def __init__(self, root, model, joga_dados, bloqueia, seleciona_dados):
        self.root = root
        self.root.geometry("450x220")
        self.root.title("Dados")
        self.root.configure(background='black')
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.controller_joga_dados = joga_dados
        self.controller_seleciona_dados = seleciona_dados
        self.bloqueia = bloqueia
        # ---- criação do frame
        self.frame = tk.Frame(root)
        self.frame.grid()

        # ---- criação do canvas
        self.canvas = tk.Canvas(self.frame, bg="black", width=448, height=64)
        self.canvas.grid()
        
        # ---- bind do clique à função seleciona_dados
        self.canvas.bind("<Button-1>", lambda event, model=model: self.seleciona_dados(event, model))
        # ---- criação de dicionário com imagens de cada dado
        self.imagens_dados = [
            tk.PhotoImage(file="./dado/img/dado_1.png"),
            tk.PhotoImage(file="./dado/img/dado_2.png"),
            tk.PhotoImage(file="./dado/img/dado_3.png"),
            tk.PhotoImage(file="./dado/img/dado_4.png"),
            tk.PhotoImage(file="./dado/img/dado_5.png"),
            tk.PhotoImage(file="./dado/img/dado_6.png")
        ]

        self.label_relancamentos = self.label_relancamentos = tk.Label(self.root, bg="black", fg="white", text="")
        self.n_loops = 0

    def joga_dados(self, model, lista_de_indices):
        if self.n_loops < 20:
            for indice in lista_de_indices:
                randomico = randint(1,6)
                mock_dado = self.canvas.create_image(32,32,image=self.imagens_dados[randomico - 1])
                self.canvas.move(mock_dado, 96*indice, 0)
            self.n_loops += 1    
            self.canvas.after(50, lambda model=model, lista_de_indices=lista_de_indices: self.joga_dados(model, lista_de_indices))
        else:
            self.n_loops = 0
            self.atualiza_dados(model, lista_de_indices)

    # ---- função para atualizar imagens dos dados
    def atualiza_dados(self, model, lista_de_indices):
        for indice in lista_de_indices:
            model.dados[indice]['selected'] = False
            model.dados[indice]["rect"] = self.canvas.create_rectangle(model.dados[indice]["x1"], 15, model.dados[indice]["x2"], 48, outline='black')
            model.dados[indice]['img'] = self.canvas.create_image(32,32,image=self.imagens_dados[model.dados[indice]['dado']-1])
            self.canvas.move(model.dados[indice]['img'], 96*indice, 0)

    # ---- função para captar eventos de clique nos dados
    def seleciona_dados(self, event, model):
        if event.y > 15.0 and event.y < 48.0:
            if event.x > model.dados[0]["x1"] and event.x < model.dados[0]["x2"]:
                if model.dados[0]["selected"]:
                    model.dados[0]["selected"] = False
                    model.dados[0]["rect"] = self.canvas.create_rectangle(model.dados[0]["x1"], 15, model.dados[0]["x2"], 48, outline='black')
                else:
                    model.dados[0]["selected"] = True
                    model.dados[0]["rect"] = self.canvas.create_rectangle(model.dados[0]["x1"], 15, model.dados[0]["x2"], 48, outline='white')
            if event.x > model.dados[1]["x1"] and event.x < model.dados[1]["x2"]:
                if model.dados[1]["selected"]:
                    model.dados[1]["selected"] = False
                    model.dados[1]["rect"] = self.canvas.create_rectangle(model.dados[1]["x1"], 15, model.dados[1]["x2"], 48, outline='black')
                else:
                    model.dados[1]["selected"] = True
                    model.dados[1]["rect"] = self.canvas.create_rectangle(model.dados[1]["x1"], 15, model.dados[1]["x2"], 48, outline='white')
            if event.x > model.dados[2]["x1"] and event.x < model.dados[2]["x2"]:
                if model.dados[2]["selected"]:
                    model.dados[2]["selected"] = False
                    model.dados[2]["rect"] = self.canvas.create_rectangle(model.dados[2]["x1"], 15, model.dados[2]["x2"], 48, outline='black')
                else:
                    model.dados[2]["selected"] = True
                    model.dados[2]["rect"] = self.canvas.create_rectangle(model.dados[2]["x1"], 15, model.dados[2]["x2"], 48, outline='white')
            if event.x > model.dados[3]["x1"] and event.x < model.dados[3]["x2"]:
                if model.dados[3]["selected"]:
                    model.dados[3]["selected"] = False
                    model.dados[3]["rect"] = self.canvas.create_rectangle(model.dados[3]["x1"], 15, model.dados[3]["x2"], 48, outline='black')
                else:
                    model.dados[3]["selected"] = True
                    model.dados[3]["rect"] = self.canvas.create_rectangle(model.dados[3]["x1"], 15, model.dados[3]["x2"], 48, outline='white')
            if event.x > model.dados[4]["x1"] and event.x < model.dados[4]["x2"]:
                if model.dados[4]["selected"]:
                    model.dados[4]["selected"] = False
                    model.dados[4]["rect"] = self.canvas.create_rectangle(model.dados[4]["x1"], 15, model.dados[4]["x2"], 48, outline='black')
                else:
                    model.dados[4]["selected"] = True
                    model.dados[4]["rect"] = self.canvas.create_rectangle(model.dados[4]["x1"], 15, model.dados[4]["x2"], 48, outline='white')

    def mock_dados(self, model):
        dados = [1,2,3,4,5,6]
        dados_selecionados = [1,1,1,1,1]
        dropdown_root = tk.Toplevel()
        dropdown_root.geometry("175x250")
        dropdown_root.title("Seleção de dados")
        dado_1 = tk.IntVar(dropdown_root)
        dado_1.set(dados[0])
        dado_2 = tk.IntVar(dropdown_root)
        dado_2.set(dados[0])
        dado_3 = tk.IntVar(dropdown_root)
        dado_3.set(dados[0])
        dado_4 = tk.IntVar(dropdown_root)
        dado_4.set(dados[0])
        dado_5 = tk.IntVar(dropdown_root)
        dado_5.set(dados[0])
        dropdown_text = tk.Label(dropdown_root, text="Escolha os dados").pack()
        dropdown = tk.OptionMenu(dropdown_root, dado_1, *dados).pack()
        dropdown = tk.OptionMenu(dropdown_root, dado_2, *dados).pack()
        dropdown = tk.OptionMenu(dropdown_root, dado_3, *dados).pack()
        dropdown = tk.OptionMenu(dropdown_root, dado_4, *dados).pack()
        dropdown = tk.OptionMenu(dropdown_root, dado_5, *dados).pack()
        dropdown_button = tk.Button(dropdown_root, text="Confirmar", command=dropdown_root.destroy).pack()
        dropdown_root.wait_window(dropdown_root)
        dados_selecionados[0] = dado_1.get()
        dados_selecionados[1] = dado_2.get()
        dados_selecionados[2] = dado_3.get()
        dados_selecionados[3] = dado_4.get()
        dados_selecionados[4] = dado_5.get()
        return dados_selecionados
        

    # ---- função para redefinir os botões depois do primeiro lançamento de dados
    def define_botoes_inicio(self):
        self.botao_joga_dados = tk.Button(self.root, bg="white", fg="black", text = "Jogar Dados", command = self.controller_joga_dados)
        self.botao_joga_dados.grid()
        self.botao_termina_jogada = tk.Button(self.root, bg="white", fg="black", text = "Terminar Jogada", command = self.bloqueia, state="disabled")
        self.botao_termina_jogada.grid()
        self.botao_seleciona_dados = tk.Button(self.root, bg="white", fg="black", text = "Selecionar Dados", command = self.controller_seleciona_dados)
        self.botao_seleciona_dados.grid()

    # ---- função para redefinir os botões depois do término da jogada 
    def redefine_botoes_inicio(self):
        self.botao_joga_dados.destroy()
        self.botao_termina_jogada.destroy()
        self.botao_seleciona_dados.destroy()
        self.botao_joga_dados = tk.Button(self.root, bg="white", fg="black", text = "Jogar Dados", command = self.controller_joga_dados)
        self.botao_joga_dados.grid()
        self.botao_termina_jogada = tk.Button(self.root, bg="white", fg="black", text = "Terminar Jogada", command = self.bloqueia, state="disabled")
        self.botao_termina_jogada.grid()
        self.botao_seleciona_dados = tk.Button(self.root, bg="white", fg="black", text = "Selecionar Dados", command = self.controller_seleciona_dados)
        self.botao_seleciona_dados.grid()
        self.redefine_label_relancamento(0)

    # ---- função para redefinir os botões depois do primeiro lançamento de dados
    def redefine_botoes_relancamento(self):
        self.botao_joga_dados.destroy()
        self.botao_termina_jogada.destroy()
        self.botao_seleciona_dados.destroy()
        self.botao_joga_dados = tk.Button(self.root, bg="white", fg="black", text = "Relançar Dados", command = self.controller_joga_dados)
        self.botao_joga_dados.grid()
        self.botao_termina_jogada = tk.Button(self.root, bg="white", fg="black", text = "Terminar Jogada", command = self.bloqueia)
        self.botao_termina_jogada.grid()
        self.botao_seleciona_dados = tk.Button(self.root, bg="white", fg="black", text = "Selecionar Dados", command = self.controller_seleciona_dados)
        self.botao_seleciona_dados.grid()

    # ---- função para redefinir os botões para só aceitar a finalização da jogada
    def redefine_botoes_termino(self):
        self.botao_joga_dados.destroy()
        self.botao_termina_jogada.destroy()
        self.botao_seleciona_dados.destroy()
        self.botao_joga_dados = tk.Button(self.root, bg="white", fg="black", text = "Relançar Dados", command = self.controller_joga_dados, state = 'disabled')
        self.botao_joga_dados.grid()
        self.botao_termina_jogada = tk.Button(self.root, bg="white", fg="black", text = "Terminar Jogada", command = self.bloqueia)
        self.botao_termina_jogada.grid()
        self.botao_seleciona_dados = tk.Button(self.root, bg="white", fg="black", text = "Selecionar Dados", command = self.controller_seleciona_dados)
        self.botao_seleciona_dados.grid()

    # ---- função para bloquear os botões depois do término da jogada
    def redefine_botoes_bloqueio(self):
        self.botao_joga_dados.destroy()
        self.botao_termina_jogada.destroy()
        self.botao_seleciona_dados.destroy()
        self.botao_joga_dados = tk.Button(self.root, bg="white", fg="black", text = "Jogar Dados", command = self.controller_joga_dados, state = "disabled")
        self.botao_joga_dados.grid()
        self.botao_termina_jogada = tk.Button(self.root, bg="white", fg="black", text = "Terminar Jogada", command = self.bloqueia, state="disabled")
        self.botao_termina_jogada.grid()
        self.botao_seleciona_dados = tk.Button(self.root, bg="white", fg="black", text = "Selecionar Dados", command = self.controller_seleciona_dados, state="disabled")
        self.botao_seleciona_dados.grid()

    def redefine_label_relancamento(self, jogadas):
        self.label_relancamentos.destroy()
        self.label_relancamentos = tk.Label(self.root, bg="black", fg="white", text="Lançamentos: {}".format(jogadas))
        self.label_relancamentos.grid(sticky="w")

    def reinicia(self):
        self.canvas.delete("all")
        self.redefine_botoes_inicio()
