

class Pontuacao():
    def __init__(self):
        self.criterios = ["Um","Dois","Três","Quatro","Cinco","Seis","Trinca","Quadra","Full House","Sequência Mínima","Sequência Máxima","YAHTZEE","Chance"]

        def calcula_pontuacao(criterio, res):
            pontos = 0
            
            if (criterio == 'Um'):
                for i in range(5):
                    if res[i] == 1:
                        pontos += 1

            elif (criterio == 'Dois'):
                for i in range(5):
                    if res[i] == 2:
                        pontos += 2

            elif (criterio == 'Três'):
                for i in range(5):
                    if res[i] == 3:
                        pontos += 3

            elif (criterio == 'Quatro'):
                for i in range(5):
                    if res[i] == 4:
                        pontos += 4

            elif (criterio == 'Cinco'):
                for i in range(5):
                    if res[i] == 5:
                        pontos += 5

            elif (criterio == 'Seis'):
                for i in range(5):
                    if res[i] == 6:
                        pontos += 6

            elif (criterio == 'Trinca'):
                trinca = 0
                res.sort()
                for i in range(3):
                    if (res[i] == res[i+1] == res[i+2]):
                        trinca = 1
                if (trinca == 0):
                    return 0
                else:
                    for i in range(5):
                        pontos += res[i]
            elif (criterio == 'Quadra'):
                quadra = 0
                res.sort()
                for i in range(3):
                    if (res[i] == res[i+1] == res[i+2]):
                        quadra = 1
                if (quadra == 0):
                    return 0
                else:
                    for i in range(5):
                        pontos += res[i]
            elif (criterio == 'Full House'):
                tmp = res
                if tmp.count(tmp[0]) == 3:
                    tmp[:] = (value for value in tmp if value != tmp[0])
                    if tmp.count(tmp[0]) == 2:
                        pontos += 25
                    else:
                        return 0
                elif tmp.count(tmp[0]) == 2:
                    tmp[:] = (value for value in tmp if value != tmp[0])
                    if tmp.count(tmp[0]) == 3:
                        pontos += 25
                    else:
                        return 0
                else:
                    return 0
            elif (criterio == 'Sequência Mínima'):
                res.sort()
                count = 0
                for i in range(0,4):
                    if res[i+1] == res[i] + 1:
                        count += 1
                    if count == 3:
                        pontos += 30
                if count < 3:
                    return 0
            elif (criterio == 'Sequência Máxima'):
                res.sort()
                count = 0
                for i in range(0,4):
                    if res[i+1] == res[i] + 1:
                        count += 1
                    if count == 4:
                        pontos += 40
                if count < 4:
                    return 0
            elif (criterio == 'YAHTZEE'):
                soma = 0
                for i in range(len(res)):
                    soma += res[i]
                if (soma != res[i]*5):
                    print("Critério YAHTZEE não aceito")
                    return 0
                else:
                    pontos = soma
            elif (criterio == 'Chance'):
                for i in range(5):
                    pontos += res[i]  
            return pontos