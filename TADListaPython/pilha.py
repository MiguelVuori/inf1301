from lista import *

__all__=['pilha_vazia', 'pilha_push', 'pilha_pop']


def pilha_vazia():
    return lst_vazia()

def pilha_push(elem):
    lst_insFin(elem)

def pilha_pop():
    return lst_retFin()