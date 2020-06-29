import sys

sys.path.insert(1, 'dado/')
sys.path.insert(1, 'pontuacao/')
sys.path.insert(1, 'tabela/')

import random
import tkinter as tk
from tkinter import filedialog
from dadoController import Dado
from pontuacao import *
from tabelaModel import Tabela
from tabelaSuperiorController import TabelaSuperior
from tabelaInferiorController import TabelaInferior
from json import *

# ----- Variaveis Globais -----

Todas_Tabelas = []
rodada = 0
jogo = 0
jogador_atual = 0
n_jogadores = 0
jogou = False

# ----- Funções de callback -----
def trataNome(enNome):
    nome = enNome.get()

    for letra in nome:
        if letra != " " and not letra.isalpha():
            return False
    return True

def salvar_jogo():
    global Todas_Tabelas
    global rodada
    global jogador_atual
    global n_jogadores
    global jogou

    json_file = {}

    if (ct002()):
        json_file["Yahtzee"] = {}
        json_file["Yahtzee"]["Vez"] = jogador_atual
        json_file["Yahtzee"]["Num_jog"] = n_jogadores
        json_file["Yahtzee"]["Nome_jog"] = []
        json_file["Yahtzee"]["Tabelas"] = {}
        json_file["Yahtzee"]["Criterios"] = {}
        json_file["Yahtzee"]["Partida"] = jogo
        json_file["Yahtzee"]["Rodada"] = rodada
        for i in Todas_Tabelas:
            json_file["Yahtzee"]["Nome_jog"].append(i[0])
            json_file["Yahtzee"]["Tabelas"][i[0]] = i[1].get_tabela()
            json_file["Yahtzee"]["Criterios"][i[0]] = i[2]

        filename = tk.filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
        
        with open(filename, "w") as file:
            dump(json_file,file,indent = 2, ensure_ascii=False)



def add_player(nome):
    global n_jogadores
    global criterios_jogador
    if(ct004()):

        n_jogadores += 1
        objetoJogador = Tabela(nome)
        Todas_Tabelas.append([nome, 
                            objetoJogador,
                            [
                                "Um",
                                "Dois",
                                "Três",
                                "Quatro",
                                "Cinco",
                                "Seis",
                                "Trinca",
                                "Quadra",
                                "Full House",
                                "Sequência Mínima",
                                'Sequência Máxima',
                                "YAHTZEE",
                                "Chance"
                                ]
                            ])
    # ----- Popup de aviso de cadastro -----
        registro_root = tk.Toplevel()
        registro_root.geometry("300x100")
        registro_root.title("Registro")
        label = tk.Label(registro_root, text="Jogador adicionado!")
        label.pack(fill='x', padx=50, pady=5)
        button_close = tk.Button(registro_root, text="Fechar", command=registro_root.destroy)
        button_close.pack(fill='x', pady=10)

def passa_vez(root):
    global jogador_atual
    global rodada
    global jogou
    global jogo

    
    # ----- Error handling -----
    if (ct001()):
        if jogador_atual + 1 == n_jogadores:
            rodada += 1

        jogador_atual = (jogador_atual + 1) % n_jogadores
        jogou = False

        if rodada == 12:
            
            rodada = 0
            jogo += 1


            if jogo == 6:
                root.destroy()
            else:
                maior_pontuacao = 0
                jogador_vencedor = ""
                list_labels = []
                root.destroy()
                root = tk.Tk()
                root.geometry("600x600")

                root.title("Fim de partida")
                Label_pontuacao = tk.Label(root, text = "Pontuação")
                Label_jogadores = tk.Label(root, text = "Jogadores")
                Label_jogadores.grid(row = 0, column = 0)
                Label_pontuacao.grid(row = 0, column = 2)

                for i,value in enumerate(Todas_Tabelas):
                    jogador = tk.Label(root, text = value[0])
                    pontuacao_jogador = tk.Label(root, text = (value[1]).get("TOTAL GERAL", 0))

                    if ((value[1]).get("TOTAL GERAL", 0) > maior_pontuacao):
                        jogador_vencedor = value[0]

                    jogador.grid(row = i + 1, column = 0)
                    pontuacao_jogador.grid(row = i + 1, column = 2)

                    list_labels.append([jogador,pontuacao_jogador])
                    
                    Todas_Tabelas[i][2] = [
                                "Um",
                                "Dois",
                                "Três",
                                "Quatro",
                                "Cinco",
                                "Seis",
                                "Trinca",
                                "Quadra",
                                "Full House",
                                "Sequência Mínima",
                                'Sequência Máxima',
                                "YAHTZEE",
                                "Chance"
                                ]

                Label_vencedor = tk.Label(root, text = "O jogador " + jogador_vencedor + " venceu!!")
                Label_vencedor.grid(row = 14, column = 1)

                # ----- Criação do botão de reiniciar Jogo -----
                
                btNovo = tk.Button(root, text = "Novo Jogo", width = 15)
                btNovo.grid(row = 15, column = 0)
                btNovo.config(command = lambda: menu_jogador(root))

                # ----- Criação do botão de terminar Jogo -----
                
                btTermina = tk.Button(root, text = "Terminar Jogo", width = 15)
                btTermina.grid(row = 15, column = 2)
                btTermina.config(command = lambda: terminar_jogo(root))

            
        else:
            menu_jogador(root)

def joga_dados():
    global dado
    if (ct005()):
        dadoToplevel = tk.Toplevel()
        dado = Dado(dadoToplevel)
        root.after(250, checa_termino_jogada)




def mostra_tabela(jogador):
    lista_jogadores = []
    for jogador in Todas_Tabelas:
        lista_jogadores.append(jogador[0])
    dropdown_root = tk.Toplevel()
    dropdown_root.geometry("175x100")
    dropdown_root.title("Jogador")
    jogador_escolhido = tk.StringVar(dropdown_root)
    jogador_escolhido.set(lista_jogadores[jogador_atual])
    dropdown_text = tk.Label(dropdown_root, text="Escolha um jogador").pack()
    dropdown = tk.OptionMenu(dropdown_root, jogador_escolhido, *lista_jogadores).pack()
    dropdown_button = tk.Button(dropdown_root, text="Confirmar", command=dropdown_root.destroy).pack()
    dropdown_root.wait_window(dropdown_root)
    escolhido = lista_jogadores.index(jogador_escolhido.get())
    objetoJogador = Todas_Tabelas[escolhido][1]
    upper = TabelaSuperior(tk.Toplevel(), objetoJogador)
    lower = TabelaInferior(tk.Toplevel(), objetoJogador)
    upper.display()
    lower.display()
    

def menu_jogador(root):
    root.destroy()
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Yahtzee")

    # ----- Label exibindo nome e rodada atual -----
    string_jogador = "Jogador atual: {0}".format(Todas_Tabelas[jogador_atual][0])
    string_rodada = "Rodada: {0}".format(rodada)
    label_jogador = tk.Label(root, text=string_jogador).pack()
    label_rodada = tk.Label(root, text=string_rodada).pack()
    
    # ----- Criação do botão de jogar dado -----
    btJogaDado = tk.Button(root, text = "Rolar os Dados", width = 15)
    btJogaDado.place(x = 130, y = 300)
    btJogaDado.config(command = lambda: joga_dados())
    

    # ----- Ver tabela -----
    btTabela = tk.Button(root, text = "Ver Tabela", width = 15)
    btTabela.place(x = 130, y = 240)
    btTabela.config(command = lambda: mostra_tabela(jogador_atual))
    

    # ----- Passar a vez -----
    btPassaVez = tk.Button(root, text = "Passar a Vez", width = 15)
    btPassaVez.place(x = 130, y = 180)
    btPassaVez.config(command = lambda: passa_vez(root))
    

    # ----- Salvar Jogo -----
    btSalvaJogo = tk.Button(root, text = "Salvar Jogo", width = 15)
    btSalvaJogo.place(x = 130, y = 120)
    btSalvaJogo.config(command = lambda: salvar_jogo())
   

def fecha_Cadastro(root,load = True):
    global Todas_Tabelas
    nomes = ''
    n = 1
    if (ct003()):
        if load == True :
            random.shuffle(Todas_Tabelas)
        for tabela in Todas_Tabelas:
            nomes += "%d. "%n + tabela[0] + "\n"
            n += 1
        sorteio_root = tk.Toplevel()
        sorteio_root.geometry("400x300")
        sorteio_root.title("Sorteio das vezes")
        label = tk.Label(sorteio_root, text=nomes)
        label.pack(fill='x', padx=50, pady=5)
        btInicia = tk.Button(sorteio_root, text = "Iniciar jogo", width = 15)
        btInicia.pack(fill='x', pady=10)
        btInicia.config(command = lambda: menu_jogador(root))


def novo_jogo():
    global root

    root.destroy()
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Yahtzee")

    # ----- Entrada dos nomes -----

    lbNome = tk.Label(root, text = "Nome", width = 12 , anchor = "w")
    lbNome.place(x = 10, y = 50)
    enNome = tk.Entry(root, width = 10)
    enNome.focus_set()
    enNome.config(validate = "focusout", validatecommand = lambda: trataNome(enNome))
    enNome.place(x = 75, y = 50)

    # ----- Criação do botão de inclusão -----

    btInclui = tk.Button(root, text = "Incluir", width = 15)
    btInclui.place(x = 50, y = 350)
    btInclui.config(command = lambda: add_player(enNome.get()))

    # ----- Criação do botão de finalizar cadastro e continuar para o jogo-----

    btContinua = tk.Button(root, text = "Continuar", width = 15)
    btContinua.place(x = 200, y = 350)
    btContinua.config(command = lambda: fecha_Cadastro(root))

    # ----- Fim da criação do cadastro -----

def terminar_jogo(root):
    root.destroy()

def carrega_jogo():
    global btNovo
    global btCarrega
    global root
    global Todas_Tabelas
    global rodada
    global jogador_atual
    global n_jogadores
    global jogo
    arquivo = None

    btNovo.destroy()
    btCarrega.destroy()

    
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))

    with open(root.filename, "r") as json_file:
        arquivo = loads(json_file.read())

    rodada = arquivo["Yahtzee"]["Rodada"]
    jogador_atual = arquivo["Yahtzee"]["Vez"]
    n_jogadores = arquivo["Yahtzee"]["Num_jog"]
    jogo = arquivo["Yahtzee"]["Partida"]

    tabelas = arquivo["Yahtzee"]["Tabelas"]

    for nome in arquivo["Yahtzee"]["Nome_jog"]:
        objetoJogador = Tabela(nome)
        objetoJogador.load(arquivo["Yahtzee"]["Tabelas"][nome])
        Todas_Tabelas.append([nome, 
                            objetoJogador,
                            arquivo["Yahtzee"]["Criterios"][nome]
                            ])
    
    fecha_Cadastro(root,load = False)


# ----- Fim das funcoes de callback -----

def checa_termino_jogada():
    global rodada
    global criterios_jogador
    global jogador_atual
    global jogou
    if dado.retorna_bloqueado():
        jogou = True
        dados = dado.retorna_dados()
        dropdown_root = tk.Toplevel()
        dropdown_root.geometry("175x100")
        dropdown_root.title("Critério")
        criterio_escolhido = tk.StringVar(dropdown_root)
        criterio_escolhido.set(Todas_Tabelas[jogador_atual][2][0])
        dropdown_text = tk.Label(dropdown_root, text="Escolha um critério").pack()
        dropdown = tk.OptionMenu(dropdown_root, criterio_escolhido, *Todas_Tabelas[jogador_atual][2]).pack()
        dropdown_button = tk.Button(dropdown_root, text="Confirmar", command=dropdown_root.destroy).pack()
        dropdown_root.wait_window(dropdown_root)
        escolhido = criterio_escolhido.get()
        pontos = pnt_pontua(escolhido, dados)
        if(escolhido == "YAHTZEE"):
            if(pontos == 0):
                Todas_Tabelas[jogador_atual][1].insere(escolhido, pontos, jogo)
            else:
                Todas_Tabelas[jogador_atual][1].insere(escolhido, 5*dados[0], jogo)
        else:
            Todas_Tabelas[jogador_atual][1].insere(escolhido, pontos, jogo)
            Todas_Tabelas[jogador_atual][2].remove(escolhido)
        return

    root.after(250, checa_termino_jogada)


# ------ Casos de Teste Unitários -----

'''

CT001 - Passar a vez:

'''

def ct001():
    if (jogou == True):
        return True
    else:
        error_message_root = tk.Toplevel()
        error_message_root.geometry("400x100")
        error_message_root.title("Erro!")
        label = tk.Label(error_message_root, text="Você precisa pontuar antes de passar a vez!")
        label.pack(fill='x', padx=50, pady=5)
        button_close = tk.Button(error_message_root, text="Fechar", command=error_message_root.destroy)
        button_close.pack(fill='x', pady=10)
        return False

'''

CT002 - Salvar o jogo:

'''

def ct002():
    if (jogou == True):
        return True
    else:
        error_message_root = tk.Toplevel()
        error_message_root.geometry("400x100")
        error_message_root.title("Erro!")
        label = tk.Label(error_message_root, text="Jogue os dados antes de salvar o jogo!")
        label.pack(fill='x', padx=50, pady=5)
        button_close = tk.Button(error_message_root, text="Fechar", command=error_message_root.destroy)
        button_close.pack(fill='x', pady=10)
        return False
'''

CT003 - Registro mínimo:

'''

def ct003():
    if (n_jogadores >= 2):
        return True
    else:
        error_message_root = tk.Toplevel()
        error_message_root.geometry("400x100")
        error_message_root.title("Erro!")
        label = tk.Label(error_message_root, text="Necessário no mínimo dois jogadores!")
        label.pack(fill='x', padx=50, pady=5)
        button_close = tk.Button(error_message_root, text="Fechar", command=error_message_root.destroy)
        button_close.pack(fill='x', pady=10)
        return False
'''

CT004 - Registro máximo:

'''

def ct004():
    if (n_jogadores < 6):
        return True
    else:
        error_message_root = tk.Toplevel()
        error_message_root.geometry("400x100")
        error_message_root.title("Erro!")
        label = tk.Label(error_message_root, text="Número máximo de jogadores atingido!")
        label.pack(fill='x', padx=50, pady=5)
        button_close = tk.Button(error_message_root, text="Fechar", command=error_message_root.destroy)
        button_close.pack(fill='x', pady=10)
        return False
'''

CT005 - Jogar os dados:

'''

def ct005():
    if (jogou == False):
        return True
    else:
        error_message_root = tk.Toplevel()
        error_message_root.geometry("400x100")
        error_message_root.title("Erro!")
        label = tk.Label(error_message_root, text="Já jogou nessa rodada")
        label.pack(fill='x', padx=50, pady=5)
        button_close = tk.Button(error_message_root, text="Fechar", command=error_message_root.destroy)
        button_close.pack(fill='x', pady=10)
        return False


# ---- Inicialização das Janelas -----

root = tk.Tk()

# ----- Criação da janela -----
root.geometry("400x400")
root.title("Menu Inicial")

# ----- Criação do botao de novo jogo do menu inicial -----

btNovo = tk.Button(root, text = "Novo Jogo", width = 15)
btNovo.place(x = 130, y = 100)
btNovo.config(command = lambda: novo_jogo())


# ----- Criação do botão de carregar e continuar para o jogo-----

btCarrega = tk.Button(root, text = "Carregar Jogo", width = 15)
btCarrega.place(x = 130, y = 175)
btCarrega.config(command = lambda: carrega_jogo())


root.mainloop()
