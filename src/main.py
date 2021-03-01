import random
import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy import signal
from scipy.fftpack import fft, fftshift

import config
from pulsos_conformadores import dicionario_pulso_conformador
from sinais import sinal_analogico, sinal_sequencia_de_bits

matplotlib.use("TkAgg")


janela_principal = tk.Tk()


janela_principal.title("Gerador de Sinais")
janela_principal.resizable(True, True)
janela_principal.config(bg="white")
janela_principal.geometry("1000x700")

figura = Figure(figsize=(7.8, 7), dpi=100)
graficos = figura.subplots(4)

canvas = FigureCanvasTkAgg(figura, janela_principal)
canvas.get_tk_widget().place(x=1, y=1, relx=0.01, rely=0.01)


def funcao_iniciar():
    if config.INICIAR_ANIMACAO:
        config.INICIAR_ANIMACAO = False
        iniciar_butao["text"] = "Iniciar"
    else:
        config.INICIAR_ANIMACAO = True
        iniciar_butao["text"] = "Pausar"


def mapeamento(pulso_conformador, sinal, numero_simbolos):
    sinal_digital = []
    for s in range(0, int(numero_simbolos)):
        intervalo_auxiliar = sinal[s] * pulso_conformador
        for k in range(0, len(intervalo_auxiliar)):
            if intervalo_auxiliar[k] == 0:
                intervalo_auxiliar[k] = -1
            sinal_digital.append(intervalo_auxiliar[k])

    return sinal_digital


def limpar_graficos():

    # Sinal Analógico
    graficos[0].cla()
    graficos[0].set_ylabel("Sinal Analógico", fontweight="bold")
    graficos[0].set_ylim(config.MINIMO_EIXO_Y, config.MAXIMO_EIXO_Y)

    # Sinal Sequência de Bits
    graficos[1].clear()
    graficos[1].set_ylabel("Sequência de Bits", fontweight="bold")
    graficos[1].set_ylim(config.MINIMO_EIXO_Y, config.MAXIMO_EIXO_Y)

    # Sinal Digital referente a Sequência de Bits
    graficos[2].clear()
    graficos[2].set_ylabel("Sinal Digital", fontweight="bold")
    graficos[2].set_ylim(config.MINIMO_EIXO_Y, config.MAXIMO_EIXO_Y)

    # Sinal Pulso Conformador
    graficos[3].clear()
    graficos[3].set_xlabel("Tempo", fontweight="bold")
    graficos[3].set_ylabel("Pulso Conformador", fontweight="bold")
    graficos[3].set_ylim(config.MINIMO_EIXO_Y, config.MAXIMO_EIXO_Y)


def gerar_grafico(i):

    if config.INICIAR_ANIMACAO:

        limpar_graficos()

        intervalo = np.linspace(0, 10, 256) * random.uniform(0.9, 1)

        """""" """
        Antes da Geração da sequência de bits e do sinal digital correspondente
        devemos passar a taxa de Símbolos recebida pela interface
        como parâmetros para as funções

        Obs: O valor fornecido pela interface está armazenado na variável `taxa_simbolo`
        """ """"""

        """""" """
        Substitua as devidas funções correspondentes em `signal.square(intervalo)`
        """ """ """

        # Busca chave referênte ao pulso selecionado no combobox
        sinal_pulso_conformador = dicionario_pulso_conformador.get(
            combo_box_pulso_conformador.get()
        )

        # Chama função correspondente a operação acima
        sinal_pulso_conformador = sinal_pulso_conformador(
            config.TAXA_DE_SIMBOLO)

        sinal_digital = mapeamento(
            sinal_pulso_conformador, sinal_sequencia_de_bits(
                config.NUMERO_AMOSTRAS, config.TAXA_DE_SIMBOLO), config.NUMERO_DE_SIMBOLO
        )

        # Sinal Analógico
        graficos[0].plot(sinal_analogico(config.NUMERO_AMOSTRAS), "c")

        # Função do Sinal de sequência de Bits
        graficos[1].stem(
            sinal_sequencia_de_bits(config.NUMERO_AMOSTRAS,
                                    config.TAXA_DE_SIMBOLO),
            use_line_collection=True,
        )

        # Função do Sinal Digital referente a Sequência de Bits
        graficos[2].plot(
            sinal_digital,
            "r",
        )
        # Sinal Pulso Conformador
        graficos[3].plot(range(0, config.TAXA_DE_SIMBOLO),
                         sinal_pulso_conformador)


def set_taxa_simbolo(event):
    taxa_de_simbolo_digitada = int(input_taxa_simbolo.get().replace(",", "."))
    if (
        taxa_de_simbolo_digitada >= 0
        and taxa_de_simbolo_digitada <= config.NUMERO_AMOSTRAS
    ):
        config.TAXA_DE_SIMBOLO = taxa_de_simbolo_digitada
        taxa_simbolo_InfoLabel["text"] = taxa_de_simbolo_digitada
    else:
        tk.messagebox.showerror("Erro", "Taxa de símbolos inválida")

    input_taxa_simbolo.delete(0, tk.END)


def set_pulso_conformador(event):
    print(combo_box_pulso_conformador.get())


ani = animation.FuncAnimation(
    figura,
    gerar_grafico,
    interval=1500,
)

# Atribuindo os padrões do botão iniciar
iniciar_butao = tk.Button(
    janela_principal,
    width=20,
    height=3,
    bg="#d3d3d3",
    text="Iniciar",
    command=funcao_iniciar,
)
# Definindo a posição do botão iniciar
iniciar_butao.place(relx=0.87, rely=0.66, anchor=tk.N)

# Atribuindo padrões para a labelframe da taxa de símbolos
taxa_simbolo_Frame = tk.LabelFrame(
    janela_principal,
    text="Taxa de Símbolos",
    width=180,
    height=75,
    borderwidth=0,
)

# Definindo a posição da labelframe
taxa_simbolo_Frame.place(in_=janela_principal, relx=0.87,
                         rely=0.28, anchor=tk.CENTER)


taxa_simbolo_InfoLabel = tk.Label(
    taxa_simbolo_Frame,
    text=str(config.TAXA_DE_SIMBOLO),
)
taxa_simbolo_InfoLabel.place(relx=0.5, rely=0.15, anchor=tk.N)
input_taxa_simbolo = tk.Entry(taxa_simbolo_Frame, width=12)
input_taxa_simbolo.place(relx=0.5, rely=0.55, anchor=tk.N)
input_taxa_simbolo.bind("<Return>", set_taxa_simbolo)


# Atribuindo padrões para o combobox do pulso conformador
pulso_conformador_frame = tk.LabelFrame(
    janela_principal,
    text="Pulso Conformador",
    width=180,
    height=75,
    borderwidth=0,
)

# Definindo a posição para o pulso conformador
pulso_conformador_frame.place(
    in_=janela_principal, relx=0.87, rely=0.5, anchor=tk.CENTER
)

combo_box_pulso_conformador = ttk.Combobox(
    pulso_conformador_frame,
    values=[
        "Retangular: Meio Período",
        "Retangular: Período Completo",
        "Triangular",
    ],
)
combo_box_pulso_conformador.place(relx=0.5, rely=0.5, anchor=tk.N)
combo_box_pulso_conformador.bind("<<ComboboxSelected>>", set_pulso_conformador)
combo_box_pulso_conformador.current(0)

tk.mainloop()
