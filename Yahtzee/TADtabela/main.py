from tabela import *

tabela = {}
tabela_1 = tab_ins(["um","dois","tres"],[1,2,3])
print(tabela_1)

tabela_2 = tab_ins(["um","dois","tres"],[1,2])
print(tabela_2)

tabela_3 = tab_ins(["tres","quatro",3.0,"lista"],[1.0,"um",3,["sl",2,4]],tabela)
print(tabela_3)

tabela_4 = tab_ins("um",2)
print(tabela_4)

tabela_5 = tabela_1
tab_ret(["um","tres"],tabela_5)
print(tabela_5)

tab_ret("dois",tabela_5)
print(tabela_5)

tab_ret("dois",tabela_5)
print(tabela_5)