from numpy import random


def sinal_analogico(numero_amostras: int):
    """
    Cria o sinal analógico aleatório, com base no numero de amostras
    """
    return random.randn(numero_amostras)
