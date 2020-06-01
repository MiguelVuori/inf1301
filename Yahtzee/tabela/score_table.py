from tkinter import *


# ---- criação da janela principal
root = Tk()
root.geometry("800x800")
root.title("Tabela de pontuação")

# --- criação dos labels horizontais da parte superior
lst = [
    ["SEÇÃO SUPERIOR", "COMO PONTUAR", "JOGO #1", "JOGO #2", "JOGO #3", "JOGO #4", "JOGO #5", "JOGO #6"],
    ["Um", "Marque a soma dos valores dos dados com o nº 1", "", "", "", "", "", ""],
    ["Dois", "Marque a soma dos valores dos dados com o nº 2", "", "", "", "", "", ""],
    ["Três", "Marque a soma dos valores dos dados com o nº 3", "", "", "", "", "", ""],
    ["Quatro", "Marque a soma dos valores dos dados com o nº 4", "", "", "", "", "", ""],
    ["Cinco", "Marque a soma dos valores dos dados com o nº 5", "", "", "", "", "", ""],
    ["Seis", "Marque a soma dos valores dos dados com o nº 5", "", "", "", "", "", ""],
    ["PONTUAÇÃO TOTAL", "------------->", "", "", "", "", "", ""],
    ["BÔNUS (se pontuação for 63 ou mais)", " MARQUE 35", "", "", "", "", "", ""],
    ["TOTAL (Da seção superior)", "------------->", "", "", "", "", "", ""],
    ["SEÇÃO INFERIOR", "||||||||||||||||||||||||||||||||||||||||||||||||||", "|||||||||||||", "|||||||||||||", "|||||||||||||", "|||||||||||||", "|||||||||||||", "|||||||||||||"],
    ["Trinca", "Adicione o Total dos 5 dados", "", "", "", "", "", ""],
    ["Quadra", "Adicione o Total dos 5 dados", "", "", "", "", "", ""],
    ["Full House", "MARQUE 25", "", "", "", "", "", ""],
    ["Sequência Mínima", "MARQUE 30", "", "", "", "", "", ""],
    ["Sequência Máxima", "MARQUE 40", "", "", "", "", "", ""],
    ["YAHTZEE (Quina)", "MARQUE 50", "", "", "", "", "", ""],
    ["Chance", "Marque o total dos 5 dados", "", "", "", "", "", ""],
    ["BÔNUS YAHTZEE", "", "", "", "", "", "", ""],
    ["TOTAL (da seção inferior)", "------------->", "", "", "", "", "", ""],
    ["TOTAL (da seção superior)", "------------->", "", "", "", "", "", ""],
    ["TOTAL GERAL", "------------->", "", "", "", "", "", ""],
]

height = 22
width = 8
for i in range(height): #Rows
    for j in range(width): #Columns
        if (j == 1):
            b = Text(root, width=25, height=2, fg='black', font=('Arial',8))
        elif (j > 1 ):
            b = Text(root, width=10, height=2, fg='black', font=('Arial',8))
        else:
            b = Text(root, width=25, height=2, fg='black', font=('Arial',8))

        b.grid(row=i, column=j)
        b.insert(END, lst[i][j])
        b.tag_configure("center", justify='center')



root.mainloop()