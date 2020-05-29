from tkinter import *
import dadoController

# ---- função para atualizar imagens dos dados
def atualiza_dados(lista_de_indices):
    dados = dadoController.pega_dados()
    for indice in lista_de_indices:
        if dados[indice]['selected']:
            dados[indice]['selected'] = False
            dados[indice]["rect"] = canvas.create_rectangle(dados[indice]["x1"], 15, dados[indice]["x2"], 48, outline='black')
        dados[indice]['img'] = canvas.create_image(32,32,image=dict_dice_imgs[dados[indice]['dado']-1])
        canvas.move(dados[indice]['img'], 96*indice, 0)

# ---- função para captar eventos de clique nos dados
def seleciona_dados(event):
    dados = dadoController.pega_dados()
    if event.y > 15.0 and event.y < 48.0:
        if event.x > dados[0]["x1"] and event.x < dados[0]["x2"]:
            if dados[0]["selected"]:
                dados[0]["selected"] = False
                dados[0]["rect"] = canvas.create_rectangle(dados[0]["x1"], 15, dados[0]["x2"], 48, outline='black')
            else:
                dados[0]["selected"] = True
                dados[0]["rect"] = canvas.create_rectangle(dados[0]["x1"], 15, dados[0]["x2"], 48, outline='white')
        if event.x > dados[1]["x1"] and event.x < dados[1]["x2"]:
            if dados[1]["selected"]:
                dados[1]["selected"] = False
                dados[1]["rect"] = canvas.create_rectangle(dados[1]["x1"], 15, dados[1]["x2"], 48, outline='black')
            else:
                dados[1]["selected"] = True
                dados[1]["rect"] = canvas.create_rectangle(dados[1]["x1"], 15, dados[1]["x2"], 48, outline='white')
        if event.x > dados[2]["x1"] and event.x < dados[2]["x2"]:
            if dados[2]["selected"]:
                dados[2]["selected"] = False
                dados[2]["rect"] = canvas.create_rectangle(dados[2]["x1"], 15, dados[2]["x2"], 48, outline='black')
            else:
                dados[2]["selected"] = True
                dados[2]["rect"] = canvas.create_rectangle(dados[2]["x1"], 15, dados[2]["x2"], 48, outline='white')
        if event.x > dados[3]["x1"] and event.x < dados[3]["x2"]:
            if dados[3]["selected"]:
                dados[3]["selected"] = False
                dados[3]["rect"] = canvas.create_rectangle(dados[3]["x1"], 15, dados[3]["x2"], 48, outline='black')
            else:
                dados[3]["selected"] = True
                dados[3]["rect"] = canvas.create_rectangle(dados[3]["x1"], 15, dados[3]["x2"], 48, outline='white')
        if event.x > dados[4]["x1"] and event.x < dados[4]["x2"]:
            if dados[4]["selected"]:
                dados[4]["selected"] = False
                dados[4]["rect"] = canvas.create_rectangle(dados[4]["x1"], 15, dados[4]["x2"], 48, outline='black')
            else:
                dados[4]["selected"] = True
                dados[4]["rect"] = canvas.create_rectangle(dados[4]["x1"], 15, dados[4]["x2"], 48, outline='white')

# ---- função para redefinir os botões depois do primeiro lançamento de dados
def redefine_botoes_relancamento():
    global botao_joga_dados
    global botao_termina_jogada
    botao_joga_dados.destroy()
    botao_joga_dados = Button(root, text = "Relançar Dados", command = dadoController.joga_dados)
    botao_joga_dados.grid()
    botao_termina_jogada.destroy()
    botao_termina_jogada = Button(root, text = "Terminar Jogada", command = dadoController.finaliza_dados)
    botao_termina_jogada.grid()

# ---- função para redefinir os botões para só aceitar a finalização da jogada
def redefine_botoes_termino():
    global botao_joga_dados
    global botao_termina_jogada
    botao_joga_dados.destroy()
    botao_joga_dados = Button(root, text = "Relançar Dados", command = dadoController.joga_dados, state = 'disabled')
    botao_joga_dados.grid()
    botao_termina_jogada.destroy()
    botao_termina_jogada = Button(root, text = "Terminar Jogada", command = dadoController.finaliza_dados)
    botao_termina_jogada.grid()

# ---- loop
def inicia_view():
    global root
    global frame
    global canvas
    global botao_joga_dados
    global botao_termina_jogada
    global dict_dice_imgs

    # ---- criação da janela principal
    root = Tk()
    root.geometry("450x200")
    root.title("Canvas de Dados")
    root.configure(background='black')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # ---- criação do frame
    frame = Frame(root)
    frame.grid()

    # ---- criação do canvas
    canvas = Canvas(frame, bg="black", width=448, height=64)
    canvas.grid()

    # ---- criação dos botões iniciais
    botao_joga_dados = Button(root, text = "Jogar Dados", command = dadoController.joga_dados)
    botao_joga_dados.grid()
    botao_termina_jogada = Button(root, text = "Terminar Jogada", command = dadoController.finaliza_dados, state="disabled")
    botao_termina_jogada.grid()

    # ---- criação de dicionário com imagens de cada dado
    dict_dice_imgs = [
        PhotoImage(file="img/dado_1.png"),
        PhotoImage(file="img/dado_2.png"),
        PhotoImage(file="img/dado_3.png"),
        PhotoImage(file="img/dado_4.png"),
        PhotoImage(file="img/dado_5.png"),
        PhotoImage(file="img/dado_6.png")
    ]
    # ---- bind do clique à função seleciona_dados
    canvas.bind("<Button-1>", seleciona_dados)

    root.mainloop()

