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
from sinais import sinal_analogico, sinal_sequencia_de_bits, sinal_digital

matplotlib.use("TkAgg")


janela_principal = tk.Tk()


janela_principal.title("Gerador de Sinais")
janela_principal.resizable(True, True)
janela_principal.config(bg="white")
# janela_principal.geometry("1000x700")
janela_principal.attributes("-zoomed", True)
tamanho_largura = janela_principal.winfo_screenwidth() * 0.0085
tamanho_altura = janela_principal.winfo_screenheight() * 0.0085
figura = Figure(figsize=(tamanho_largura, tamanho_altura), dpi=100)
graficos = figura.subplots(4)

canvas = FigureCanvasTkAgg(figura, janela_principal)
canvas.get_tk_widget().place(x=1, y=1, relx=0.01, rely=0.01)


def funcao_iniciar():
    if config.INICIAR_ANIMACAO:
        config.INICIAR_ANIMACAO = False
        iniciar_butao["text"] = "Iniciar"
        iniciar_butao["bg"] = "#008000"

    else:
        config.INICIAR_ANIMACAO = True
        iniciar_butao["text"] = "Pausar"
        iniciar_butao["bg"] = "#FF0000"


def mapeamento_de_bits(
    senquencia_bits, valor_bit_para_um: int, valor_bit_para_zero: int, numero_simbolos
):
    for s in range(0, int(numero_simbolos)):
        if senquencia_bits[s] == 1:
            senquencia_bits[s] = valor_bit_para_um
        elif senquencia_bits[s] == 0:
            senquencia_bits[s] = valor_bit_para_zero

    return senquencia_bits


def limpar_graficos():

    # Sinal Analógico
    graficos[0].cla()
    graficos[0].set_ylabel("Sinal Analógico", fontweight="bold")
    graficos[0].set_ylim(config.MINIMO_EIXO_Y, config.MAXIMO_EIXO_Y)
    graficos[0].grid(True)

    # Sinal Sequência de Bits
    graficos[1].clear()
    graficos[1].set_ylabel("Sequência de Bits", fontweight="bold")
    graficos[1].set_ylim(config.MINIMO_EIXO_Y, config.MAXIMO_EIXO_Y)
    graficos[1].grid(True)

    # Sinal Digital referente a Sequência de Bits
    graficos[2].clear()
    graficos[2].set_ylabel("Sinal Digital", fontweight="bold")
    graficos[2].set_ylim(config.MINIMO_EIXO_Y, config.MAXIMO_EIXO_Y)
    graficos[2].grid(True)

    # Sinal Pulso Conformador
    graficos[3].clear()
    graficos[3].set_xlabel("Tempo", fontweight="bold")
    graficos[3].set_ylabel("Pulso Conformador", fontweight="bold")
    graficos[3].set_ylim(config.MINIMO_EIXO_Y, config.MAXIMO_EIXO_Y)
    graficos[3].grid(True)


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

        # Busca chave referênte ao pulso selecionado no combobox
        sinal_pulso_conformador = dicionario_pulso_conformador.get(
            combo_box_pulso_conformador.get()
        )

        # Chama função correspondente a operação acima
        sinal_pulso_conformador = sinal_pulso_conformador(config.TAXA_DE_SIMBOLO)

        # Sinal Analógico
        graficos[0].plot(sinal_analogico(config.NUMERO_AMOSTRAS), "c")

        sequencia_de_bits = sinal_sequencia_de_bits(
            config.NUMERO_AMOSTRAS, config.TAXA_DE_SIMBOLO
        )

        # Função do Sinal de sequência de Bits
        graficos[1].stem(
            sequencia_de_bits,
            use_line_collection=True,
        )

        # Função do Sinal Digital referente a Sequência de Bits
        graficos[2].plot(
            sinal_digital(
                sinal_pulso_conformador,
                mapeamento_de_bits(
                    sequencia_de_bits,
                    config.VALOR_DE_BITS_PARA_UM,
                    config.VALOR_DE_BITS_PARA_ZERO,
                    config.NUMERO_DE_SIMBOLO,
                ),
                config.NUMERO_DE_SIMBOLO,
            ),
            "r",
        )
        # Sinal Pulso Conformador
        graficos[3].plot(range(0, config.TAXA_DE_SIMBOLO), sinal_pulso_conformador)


def set_taxa_simbolo(event):
    taxa_de_simbolo_digitada = int(input_taxa_simbolo.get().replace(",", "."))
    if (
        taxa_de_simbolo_digitada >= 0
        and taxa_de_simbolo_digitada <= config.NUMERO_AMOSTRAS
    ):
        config.TAXA_DE_SIMBOLO = taxa_de_simbolo_digitada
        config.NUMERO_DE_SIMBOLO = config.NUMERO_AMOSTRAS / config.TAXA_DE_SIMBOLO
        taxa_simbolo_InfoLabel["text"] = taxa_de_simbolo_digitada
        numero_simbolo_InfoLabel["text"] = str(config.NUMERO_DE_SIMBOLO)
    else:
        tk.messagebox.showerror("Erro", "Taxa de símbolos inválida")

    input_taxa_simbolo.delete(0, tk.END)


def set_numero_amostras(event):
    numero_amostras_digitada = int(numero_amostras_entrada.get().replace(",", "."))
    if (
        numero_amostras_digitada >= 0
        and numero_amostras_digitada >= config.TAXA_DE_SIMBOLO
    ):
        config.NUMERO_AMOSTRAS = numero_amostras_digitada
        config.NUMERO_DE_SIMBOLO = config.NUMERO_AMOSTRAS / config.TAXA_DE_SIMBOLO
        numero_amostras_infoframe["text"] = numero_amostras_digitada
        numero_simbolo_InfoLabel["text"] = str(config.NUMERO_DE_SIMBOLO)
    else:
        tk.messagebox.showerror("Erro", "Número de amostras inválida")

    numero_amostras_entrada.delete(0, tk.END)


def set_mapeamento_um(event):
    mapeamento_um_digitado = int(mapeamento_um_entrada.get())
    config.VALOR_DE_BITS_PARA_UM = mapeamento_um_digitado
    mapeamento_um_infoframe["text"] = "Bit 1 é igual a " + str(
        config.VALOR_DE_BITS_PARA_UM
    )
    mapeamento_um_entrada.delete(0, tk.END)


def set_mapeamento_zero(event):
    mapeamento_zero_digitado = int(mapeamento_zero_entrada.get())
    config.VALOR_DE_BITS_PARA_ZERO = mapeamento_zero_digitado
    mapeamento_zero_infoframe["text"] = "Bit 0 é igual a " + str(
        config.VALOR_DE_BITS_PARA_ZERO
    )
    mapeamento_zero_entrada.delete(0, tk.END)


def set_pulso_conformador(event):
    print(combo_box_pulso_conformador.get())


ani = animation.FuncAnimation(
    figura,
    gerar_grafico,
    interval=1500,
)

# Atribuindo padrões para a labelframe de número de amostras
numero_amostras_frame = tk.LabelFrame(
    janela_principal,
    text="Número de Amostras",
    width=180,
    height=75,
    borderwidth=0,
)

# Definindo a posição da labelframe
numero_amostras_frame.place(
    in_=janela_principal, relx=0.87, rely=0.18, anchor=tk.CENTER
)


numero_amostras_infoframe = tk.Label(
    numero_amostras_frame,
    text=str(config.NUMERO_AMOSTRAS),
)
numero_amostras_infoframe.place(relx=0.5, rely=0.15, anchor=tk.N)
numero_amostras_entrada = tk.Entry(numero_amostras_frame, width=12)
numero_amostras_entrada.place(relx=0.5, rely=0.55, anchor=tk.N)
numero_amostras_entrada.bind("<Return>", set_numero_amostras)


# Atribuindo padrões para a labelframe da taxa de símbolos
taxa_simbolo_Frame = tk.LabelFrame(
    janela_principal,
    text="Taxa de Símbolos",
    width=180,
    height=75,
    borderwidth=0,
)

# Definindo a posição da labelframe
taxa_simbolo_Frame.place(in_=janela_principal, relx=0.87, rely=0.3, anchor=tk.CENTER)


taxa_simbolo_InfoLabel = tk.Label(
    taxa_simbolo_Frame,
    text=str(config.TAXA_DE_SIMBOLO),
)
taxa_simbolo_InfoLabel.place(relx=0.5, rely=0.15, anchor=tk.N)
input_taxa_simbolo = tk.Entry(taxa_simbolo_Frame, width=12)
input_taxa_simbolo.place(relx=0.5, rely=0.55, anchor=tk.N)
input_taxa_simbolo.bind("<Return>", set_taxa_simbolo)


# Atribuindo padrões para a labelframe do Número de Simbolos
numero_simbolo_Frame = tk.LabelFrame(
    janela_principal,
    text="Número de Símbolos",
    width=180,
    height=75,
    borderwidth=0,
)

# Definindo a posição da labelframe
numero_simbolo_Frame.place(in_=janela_principal, relx=0.87, rely=0.42, anchor=tk.CENTER)


numero_simbolo_InfoLabel = tk.Label(
    numero_simbolo_Frame,
    text=str(config.NUMERO_DE_SIMBOLO),
)
numero_simbolo_InfoLabel.place(relx=0.5, rely=0.15, anchor=tk.N)


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
    in_=janela_principal, relx=0.87, rely=0.54, anchor=tk.CENTER
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

# Atribuindo padrões para a labelframe de Mapeamento
mapeamento_frame = tk.LabelFrame(
    janela_principal,
    text="Mapeamento de bits",
    width=180,
    height=150,
    borderwidth=0,
)

# Definindo a posição da labelframe
mapeamento_frame.place(in_=janela_principal, relx=0.87, rely=0.715, anchor=tk.CENTER)


mapeamento_um_infoframe = tk.Label(
    mapeamento_frame,
    text="Bit 1 é igual a " + str(config.VALOR_DE_BITS_PARA_UM),
)
mapeamento_um_infoframe.place(relx=0.5, rely=0.1, anchor=tk.N)
mapeamento_um_entrada = tk.Entry(mapeamento_frame, width=12)
mapeamento_um_entrada.place(relx=0.5, rely=0.28, anchor=tk.N)
mapeamento_um_entrada.bind("<Return>", set_mapeamento_um)

mapeamento_zero_infoframe = tk.Label(
    mapeamento_frame,
    text="Bit 0 é igual a " + str(config.VALOR_DE_BITS_PARA_ZERO),
)
mapeamento_zero_infoframe.place(relx=0.5, rely=0.52, anchor=tk.N)
mapeamento_zero_entrada = tk.Entry(mapeamento_frame, width=12)
mapeamento_zero_entrada.place(relx=0.5, rely=0.7, anchor=tk.N)
mapeamento_zero_entrada.bind("<Return>", set_mapeamento_zero)

# Atribuindo os padrões do botão iniciar
iniciar_butao = tk.Button(
    janela_principal,
    width=6,
    height=1,
    font=14,
    bg="#008000",
    fg="#ffffff",
    text="Iniciar",
    command=funcao_iniciar,
)
# Definindo a posição do botão iniciar
iniciar_butao.place(relx=0.87, rely=0.835, anchor=tk.N)

tk.mainloop()
