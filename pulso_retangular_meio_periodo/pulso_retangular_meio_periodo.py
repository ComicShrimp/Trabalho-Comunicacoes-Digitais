from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def gerar_pulso_retangular_meio_periodo(taxa_de_amostragem: int, periodo_de_simbolo: int):
    '''
      Gerar o pulso conformador do tipo retangular de meio período
    '''
    taxa_de_simbolo = int(taxa_de_amostragem / periodo_de_simbolo) 
    amostras = []
   
    for r in range(0, int(taxa_de_simbolo/2)):
        amostras.append(0)
        
    for r in range(0, int(taxa_de_simbolo/2)):
        amostras.append(1)      
    
    return amostras
        
    
    


