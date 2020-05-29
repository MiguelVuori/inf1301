import dadoModel, dadoView

def inicia_view():
    dadoView.inicia_view()

def joga_dados():
    if dadoModel.retries == 0:
        dados = dadoModel.joga_dados([0,1,2,3,4])
        dadoView.atualiza_dados([0,1,2,3,4])
        dadoView.redefine_botoes_relancamento()
        dadoModel.retries += 1
    elif dadoModel.retries < 3:
        dados = pega_dados()
        selecionados = []
        i = 0
        for dado in dados.values():
            if dado['selected']:
                selecionados.append(i)
            i += 1
        dados = dadoModel.joga_dados(selecionados)
        dadoView.atualiza_dados(selecionados)
        dadoModel.retries += 1
    else:
        dadoView.redefine_botoes_termino()
        dadoView.atualiza_dados([0,1,2,3,4])

def pega_dados():
    return dadoModel.pega_dados()

def finaliza_dados():
    return(pega_dados(),exit(0))