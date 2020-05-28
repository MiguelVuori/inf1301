from tkinter import *
from dado import *

# ---- criação da janela principal
root = Tk()
root.geometry("450x200")
root.title("Canvas de Dados")
root.configure(background='black')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = Frame(root)
frame.grid()

canvas = Canvas(frame, bg="black", width=448, height=64)
canvas.grid()

dados = {}
for i in range(0, 5):
    dados[i] = {'selected': False, 'img': None, 'rect': None, 'x1': 15+96*i, 'x2': 48+96*i}

dict_dice_imgs = [
    PhotoImage(file="dado_1.png"),
    PhotoImage(file="dado_2.png"),
    PhotoImage(file="dado_3.png"),
    PhotoImage(file="dado_4.png"),
    PhotoImage(file="dado_5.png"),
    PhotoImage(file="dado_6.png")
    ]

def selecionaDados(event):
    if event.y > 15.0 and event.y < 48.0:
        if event.x > 15.0 and event.x < 48.0:
            if dados[0]["selected"] == True:
                dados[0]["selected"] = False
                dados[0]["rect"] = canvas.create_rectangle(15, 15, 48, 48, outline='black')
            else:
                dados[0]["selected"] = True
                dados[0]["rect"] = canvas.create_rectangle(15, 15, 48, 48, outline='white')
        if event.x > 111.0 and event.x < 144.0:
            if dados[1]["selected"]:
                dados[1]["selected"] = False
                dados[1]["rect"] = canvas.create_rectangle(111, 15, 144, 48, outline='black')
            else:
                dados[1]["selected"] = True
                dados[1]["rect"] = canvas.create_rectangle(111, 15, 144, 48, outline='white')
        if event.x > 207.0 and event.x < 240.0:
            if dados[2]["selected"]:
                dados[2]["selected"] = False
                dados[2]["rect"] = canvas.create_rectangle(207, 15, 240, 48, outline='black')
            else:
                dados[2]["selected"] = True
                dados[2]["rect"] = canvas.create_rectangle(207, 15, 240, 48, outline='white')
        if event.x > 303.0 and event.x < 336.0:
            if dados[3]["selected"]:
                dados[3]["selected"] = False
                dados[3]["rect"] = canvas.create_rectangle(303, 15, 336, 48, outline='black')
            else:
                dados[3]["selected"] = True
                dados[3]["rect"] = canvas.create_rectangle(303, 15, 336, 48, outline='white')
        if event.x > 399.0 and event.x < 432.0:
            if dados[4]["selected"]:
                dados[4]["selected"] = False
                dados[4]["rect"] = canvas.create_rectangle(399, 15, 432, 48, outline='black')
            else:
                dados[4]["selected"] = True
                dados[4]["rect"] = canvas.create_rectangle(399, 15, 432, 48, outline='white')
def relancaDados():
    i = 0
    for dado in dados.values():
        if dado["selected"]:
            novo_dado = joga_dado(1)
            dado["img"] = canvas.create_image(32,32,image=dict_dice_imgs[novo_dado[0]-1])
            canvas.move(dado["img"], 96*i, 0)
            dado["selected"] = False
            dado["rect"] = canvas.create_rectangle(dado["x1"], 15, dado["x2"], 48, outline='black')
        i+=1

def jogaDados():
    global botao_joga_dados
    global dados
    dados_int = joga_dado(5)
    i = 0
    for dado in dados_int:
        dados[i]["img"] = canvas.create_image(32,32,image=dict_dice_imgs[dado-1])
        i += 1
    for i in range(0,5):
        canvas.move(dados[i]["img"], 96*i, 0)
    botao_joga_dados.destroy()
    canvas.bind("<Button-1>", selecionaDados)
    botao_joga_dados = Button(root, text ="Relançar Dados / Terminar Jogada", command = relancaDados)
    botao_joga_dados.grid()

botao_joga_dados = Button(root, text = "Jogar Dados", command = jogaDados)
botao_joga_dados.grid()

root.mainloop()