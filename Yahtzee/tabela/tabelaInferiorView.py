import tkinter as tk

class View():
    def __init__(self, root, tabela):
        self.root = root
        self.root.geometry("700x400")
        self.root.title("Seção Inferior")
        self.layout = [
        ["SEÇÃO INFERIOR","COMO PONTUAR", "JOGO #1", "JOGO #2", "JOGO #3", "JOGO #4", "JOGO #5", "JOGO #6"],
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

    def update(self):
        for i in range(12):
            for j in range(8):
                if(j > 1 and i > 0):
                        layout[i][j] = self.tabela.get(lst[i][0])

    def mostra(self):
        height = 12
        width = 8
        for i in range(height): #Rows
            for j in range(width): #Columns
                if (j == 1):
                    b = tk.Text(self.root, width=25, height=2, fg='black', font=('Arial',8))
                elif (j > 1 ):
                    b = tk.Text(self.root, width=10, height=2, fg='black', font=('Arial',8))
                else:
                    b = tk.Text(self.root, width=25, height=2, fg='black', font=('Arial',8))

                b.grid(row=i, column=j)
                b.insert(tk.END, self.layout[i][j])
                b.tag_configure("center", justify='center')