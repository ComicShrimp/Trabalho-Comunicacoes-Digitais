import numpy as np


def sinal_analogico(numero_amostras: int):
    """
    Cria o sinal analógico aleatório, com base no numero de amostras
    """
    return np.random.randn(numero_amostras)


def sinal_sequencia_de_bits(numero_amostras: int, taxa_de_simbolo: int):
    """
    Cria sequência de bits
    """
    numero_de_simbolo = numero_amostras / taxa_de_simbolo

    sinal_senquencia_bits = 2 * (
        np.random.randint(1, 3, size=int(numero_de_simbolo)) - 1.5
    )  # Função do Sinal de sequência de Bits
    return (sinal_senquencia_bits + 1) / 2


def sinal_digital(pulso_conformador, sequencia_de_bits, numero_simbolos):
    sinal_digital = []
    for s in range(0, int(numero_simbolos)):
        sinal_auxiliar = sequencia_de_bits[s] * pulso_conformador
        for k in range(0, len(sinal_auxiliar)):
            sinal_digital.append(sinal_auxiliar[k])

    return sinal_digital
