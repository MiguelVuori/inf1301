import tkinter as tk

class View():
    def __init__(self, root, tabela):
        self.root = root
        self.root.geometry("650x325")
        self.root.title("Seção Superior")
        self.layout = [
            ["SEÇÃO SUPERIOR", "COMO PONTUAR", "JOGO #1", "JOGO #2", "JOGO #3", "JOGO #4", "JOGO #5", "JOGO #6"],
            ["Um", "Marque a soma dos valores dos dados com o nº 1", "", "", "", "", "", ""],
            ["Dois", "Marque a soma dos valores dos dados com o nº 2", "", "", "", "", "", ""],
            ["Três", "Marque a soma dos valores dos dados com o nº 3", "", "", "", "", "", ""],
            ["Quatro", "Marque a soma dos valores dos dados com o nº 4", "", "", "", "", "", ""],
            ["Cinco", "Marque a soma dos valores dos dados com o nº 5", "", "", "", "", "", ""],
            ["Seis", "Marque a soma dos valores dos dados com o nº 5", "", "", "", "", "", ""],
            ["PONTUAÇÃO TOTAL", "------------->", "", "", "", "", "", ""],
            ["BÔNUS (se pontuação for 63 ou mais)", " MARQUE 35", "", "", "", "", "", ""],
            ["TOTAL (Da seção superior)", "------------->", "", "", "", "", "", ""]
        ]
    
    def update(self):
        for i in range(12):
            for j in range(8):
                if(j > 1 and i > 0):
                        layout[i][j] = self.tabela.get(lst[i][0])

    def mostra(self):
        height = 10
        width = 8
        for i in range(height): #Rows
            for j in range(width): #Columns
                if (j == 1):
                    b = tk.Text(self.root, width=26, height=2, fg='black', font=('Arial',8))
                elif (j > 1 ):
                    b = tk.Text(self.root, width=8, height=2, fg='black', font=('Arial',8))
                else:
                    b = tk.Text(self.root, width=26, height=2, fg='black', font=('Arial',8))

                b.grid(row=i, column=j)
                b.insert(tk.END, self.layout[i][j])
                b.tag_configure("center", justify='center')
