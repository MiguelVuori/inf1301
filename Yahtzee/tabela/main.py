from tabela import *

tab_ins(["um","dois","tres"],[1,2,3])
tab_print()

tab_ins(["um","dois","tres"],[1,2])
tab_print()

tab_ins(["tres","quatro",3.0,"lista"],[1.0,"um",3,["sl",2,4]])
tab_print()

tab_ins("um",2)
tab_print()

tab_ret(["um","tres"])
tab_print()

tab_ret("dois")
tab_print()

tab_ret("dois")
tab_print()

print(tab_get("lista",0))
tab_print()