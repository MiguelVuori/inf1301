import random
from utils import *

__all__ = ['joga_dado']

def init():
    random.seed()


def joga_dado(n_dados):
    res = []
    for i in range(n_dados):
        res.append(random.randint(1,6))
    return res 

init()