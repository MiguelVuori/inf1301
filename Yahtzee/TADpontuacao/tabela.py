__all__ = ["tab_ins","tab_ret","tab_get","tab_print"]


def init():
    global  tabela
    tabela = {}

def tab_ins(campos,valores):
    tpc = type(campos)
    tpv = type(valores)

    if (tpc == list) and (len(campos) == 2):
        tabela[campos[0]][campos[1]] = valores
    elif ((tpc == str or tpc == int or tpc == float) and (tpv == list or tpv == dict or tpv == str or tpv == int or tpv == float)):
        tabela[str(campos)] = valores
    else:
        print("Erro na criação da tabela: tamanho dos campos diferente do de valores")

def tab_ret(campos):
    tpc = type(campos)
    valores = []

    if (tpc == list):
        for ind,campo in enumerate(campos):
            try:
                valores.append(tabela.pop(str(campo)))
            except KeyError:
                print("Campo " + str(campo) + " não achado")
    elif ((tpc == str or tpc == int or tpc == float)):
        try:
            valores.append(tabela.pop(str(campos)))
        except KeyError:
            print("Campo " +str(campos) + " não achado")
    else:
        print("Campos possui typagem inválida, tente 'lis', 'str', 'float', 'int'")
    
    return valores

def tab_get(*campos):
    valor = None

    if len(campos) >= 1:
        for idx,campo in enumerate(campos):
            if idx == 0:
                try:
                    valor =  tabela[campo]
                except KeyError:
                    print("Caminho fornecido não existe")
            else:
                try:
                    valor = valor[campo]
                except KeyError:
                    print("Caminho fornecido não existe")
    
    return valor

def tab_print():
    print(tabela)

init()
tabela = {}