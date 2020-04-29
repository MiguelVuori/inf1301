import partida

__all__ = ['input_handler']

def init():
    pass

def input_handler(input, destination_type):
    if input == "quit":
        partida.termina_jogo()
    else:
        if destination_type == int:
            return int(input)
        else:
            return input

init()