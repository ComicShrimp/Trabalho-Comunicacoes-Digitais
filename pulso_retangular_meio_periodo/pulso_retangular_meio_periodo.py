from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def gerar_pulso_retangular_meio_periodo(taxa_de_simbolo: int):
    '''
      Gerar o pulso conformador do tipo retangular de meio período
    '''
    amostras = np.zeros(taxa_de_simbolo)
    amostras[int(taxa_de_simbolo/2):] = 1
    return amostras
        
    
plt.plot(gerar_pulso_retangular_meio_periodo(500))
plt.xlim(0,500)
plt.show()    


