from pilha import *

pilha_push([3.0,3.0])
pilha_push([2.0,2.0])
pilha_push([1.0,1.0])
while not pilha_vazia():
    e = pilha_pop()
    print("%.1f,%.1f"%(e[0],e[1]))