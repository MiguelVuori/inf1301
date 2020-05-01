__all__ = ["tab_ins","tab_ret"]



def tab_ins(campos,valores,tabela=None):
    tpc = type(campos)
    tpv = type(valores)

    if tabela == None:
        tabela = {}

    if (tpc == tpv == list) and (len(campos) == len(valores)):
        for ind,campo in enumerate(campos):
            tabela[str(campo)] = valores[ind]
    elif ((tpc == str or tpc == int or tpc == float) and (tpv == str or tpv == int or tpv == float)):
        tabela[str(campos)] = valores
    else:
        print("Erro na criação da tabela: tamanho dos campos diferente do de valores")
    
    return tabela

def tab_ret(campos,tabela):
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
