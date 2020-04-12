__all__= ['lst_vazia', 'lst_insIni', 'lst_insFin', 'lst_retIni', 'lst_retFin', 'lst_posIni', 'lst_prox']



def init():
    global lst, corrente
    lst = []
    corrente = 0

def lst_vazia():
    if(lst == []):
        return True
    else:
        return False

def lst_insIni(elem):
    lst.insert(0, elem)

def lst_insFin(elem):
    lst.append(elem)

def lst_retIni():
    if(lst_vazia() == True):
        return None
    else:
        return lst.pop(0)
    return

def lst_retFin():
    if(lst_vazia() == True):
        return None
    else:
        return lst.pop(-1)
    return

def lst_posIni():
    if(lst_vazia() == True):
        return None
    else:
        corrente = lst[0]
    return

def lst_prox():
    if(lst_vazia() == True):
        return None
    else:
        indice = lst.index(corrente)
        corrente = lst[indice + 1]
    return
lst = []
corrente = 0
init()