from tkinter import *
from tkinter import messagebox
import matplotlib
import matplotlib.animation as animation
from scipy import signal
import numpy as np
import random
from tkinter import ttk

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


janela_principal = Tk()
iniciar = False
minimo_tamanho_intervalo = 0
maximo_tamanho_intervalo = 10
digital = True

numero_amostras = 500
taxa_simbolo = 3
numero_simbolo = numero_amostras / taxa_simbolo


janela_principal.title("Gerador de Sinais")
janela_principal.resizable(True, True)
janela_principal.config(bg="white")
janela_principal.geometry("980x600")

f = Figure(figsize=(10, 7), dpi=80)
graficos = f.subplots(4)
eixo_x = [0]
eixo_y = [0]

# Graficos:
graficos[0].plot(eixo_x, eixo_y)  # Sinal analogico
graficos[1].plot(eixo_x, eixo_y)  # Sequencia de bits aleatoria
graficos[2].plot(eixo_x, eixo_y)  # Sinal digital
graficos[3].plot(eixo_x, eixo_y)  # Pulso conformador

# X/Y Sinal analogico

graficos[0].set_ylabel("Sinal Analógico", fontweight="bold")
graficos[0].set_ylim(-2, 2)

# X/Y Sequencia de bits aleatorias
graficos[1].set_ylabel("Sequência de Bits", fontweight="bold")
graficos[1].set_ylim(-2, 2)

# X/Y Sinal digital referente a sequencia de bits
graficos[2].set_ylabel("Sinal Digital", fontweight="bold")
graficos[2].set_ylim(-2, 2)

# X/Y Pulso conformador
graficos[3].set_xlabel("Tempo", fontweight="bold")
graficos[3].set_ylabel("Pulso Conformador", fontweight="bold")
graficos[3].set_ylim(-2, 2)

canvas = FigureCanvasTkAgg(f, janela_principal)
grafico = canvas.get_tk_widget().place(x=1, y=1, relx=0.01, rely=0.01)


def funcao_iniciar():
    global iniciar
    if iniciar:
        iniciar = False
        iniciar_butao["text"] = "Iniciar"
    else:
        iniciar = True
        iniciar_butao["text"] = "Pausar"


# Função de exemplo, ao final ela será exlcuída
# para dar lugar as pertinentes
def funcao_exemplo_pulso_conformador(intervalo):
    return np.sin(intervalo)


def gerar_grafico(i, eixo_x, eixo_y):
    global iniciar
    global maximo_tamanho_intervalo, minimo_tamanho_intervalo
    global taxa_simbolo, numero_amostras, numero_simbolo

    if iniciar:
        intervalo = np.linspace(
            minimo_tamanho_intervalo, maximo_tamanho_intervalo, 256
        ) * random.uniform(0.9, 1)

        # Sinal Analógico
        graficos[0].clear()
        graficos[0].set_ylim(-2, 2)
        graficos[0].set_ylabel("Sinal Analógico", fontweight="bold")

        # Sinal Sequência de Bits
        graficos[1].clear()
        graficos[1].set_ylim(-2, 2)
        graficos[1].set_ylabel("Sequência de Bits", fontweight="bold")

        # Sinal Digital referente a Sequência de Bits
        graficos[2].clear()
        graficos[2].set_ylim(-2, 2)
        graficos[2].set_ylabel("Sinal Digital", fontweight="bold")

        # Sinal Pulso Conformador
        graficos[3].clear()
        graficos[3].set_ylim(-2, 2)
        graficos[3].set_xlabel("Tempo", fontweight="bold")
        graficos[3].set_ylabel("Pulso Conformador", fontweight="bold")

        # Sinal Analógico
        sinal_analogico = np.sin(intervalo)
        graficos[0].plot(intervalo, sinal_analogico, "c")

        """""" """
        Antes da Geração da sequência de bits e do sinal digital correspondente
        devemos passar a taxa de Símbolos recebida pela interface
        como parâmetros para as funções

        Obs: O valor fornecido pela interface está armazenado na variável `taxa_simbolo`
        """ """"""

        """""" """
        Substitua as devidas funções correspondentes em `signal.square(intervalo)`
        """ """ """

        # Sinal Sequência de Bits
        numero_simbolo = numero_amostras / taxa_simbolo
        sinal_senquencia_bits = 2 * (
            np.random.randint(1, 3, size=int(numero_simbolo)) - 1.5
        )  # Função do Sinal de sequência de Bits
        sinal_senquencia_bits = (sinal_senquencia_bits + 1) / 2

        graficos[1].stem(
            range(0, int(numero_simbolo)),
            sinal_senquencia_bits,
            use_line_collection=True,
        )

        # Sinal Digital referente a Sequência de Bits
        sinal_digital = signal.square(
            intervalo
        )  # Função do Sinal Digital referente a Sequência de Bits
        graficos[2].plot(
            intervalo,
            sinal_digital,
            "r",
        )

        """""" """"""
        # Substitua as funções funcao_exemplo_pulso_conformador
        # pela sua função correspondente
        # OBS: Todas as funções devem manter os mesmos padrões
        # de parâmetros
        """""" """"""
        # Dicionário de pulso conformador
        dicionario_pulso_conformador = {
            "Triangular": funcao_exemplo_pulso_conformador,
            "Retangular: Meio Período": funcao_exemplo_pulso_conformador,
            "Retangular: Período Completo": funcao_exemplo_pulso_conformador,
        }

        # Busca chave referênte ao pulso selecionado no combobox
        sinal_pulso_conformador = dicionario_pulso_conformador.get(
            combo_box_pulso_conformador.get()
        )

        # Chama função correspondente a operação acima
        sinal_pulso_conformador = sinal_pulso_conformador(intervalo)

        # Sinal Pulso Conformador
        graficos[3].plot(intervalo, sinal_pulso_conformador)

        # Movimento de tempo do gráfico
        maximo_tamanho_intervalo += 1
        minimo_tamanho_intervalo += 1


def set_taxa_simbolo(event):
    global taxa_simbolo
    if int(input_taxa_simbolo.get().replace(",", ".")) >= 0:
        taxa_simbolo = int(input_taxa_simbolo.get().replace(",", "."))
        taxa_simbolo_InfoLabel["text"] = input_taxa_simbolo.get()
    else:
        messagebox.showerror("Erro", "Taxa de símbolos inválida")

    input_taxa_simbolo.delete(0, END)


def set_pulso_conformador(event):
    print(combo_box_pulso_conformador.get())


ani = animation.FuncAnimation(
    f,
    gerar_grafico,
    fargs=(eixo_x, eixo_y),
    interval=500,
)

# Atribuindo os padrões do botão iniciar
iniciar_butao = Button(
    janela_principal,
    width=20,
    height=3,
    bg="#d3d3d3",
    text="Iniciar",
    command=funcao_iniciar,
)
# Definindo a posição do botão iniciar
iniciar_butao.place(relx=0.87, rely=0.66, anchor=N)

# Atribuindo padrões para a labelframe da taxa de símbolos
taxa_simbolo_Frame = LabelFrame(
    janela_principal,
    text="Taxa de Símbolos",
    width=180,
    height=75,
    borderwidth=0,
)

# Definindo a posição da labelframe
taxa_simbolo_Frame.place(in_=janela_principal, relx=0.87, rely=0.28, anchor=CENTER)


taxa_simbolo_InfoLabel = Label(
    taxa_simbolo_Frame,
    text=str(taxa_simbolo),
)
taxa_simbolo_InfoLabel.place(relx=0.5, rely=0.15, anchor=N)
input_taxa_simbolo = Entry(taxa_simbolo_Frame, width=12)
input_taxa_simbolo.place(relx=0.5, rely=0.55, anchor=N)
input_taxa_simbolo.bind("<Return>", set_taxa_simbolo)


# Atribuindo padrões para o combobox do pulso conformador
pulso_conformador_frame = LabelFrame(
    janela_principal,
    text="Pulso Conformador",
    width=180,
    height=75,
    borderwidth=0,
)

# Definindo a posição para o pulso conformador
pulso_conformador_frame.place(in_=janela_principal, relx=0.87, rely=0.5, anchor=CENTER)

combo_box_pulso_conformador = ttk.Combobox(
    pulso_conformador_frame,
    values=[
        "Retangular: Meio Período",
        "Retangular: Período Completo",
        "Triangular",
    ],
)
combo_box_pulso_conformador.place(relx=0.5, rely=0.5, anchor=N)
combo_box_pulso_conformador.bind("<<ComboboxSelected>>", set_pulso_conformador)
combo_box_pulso_conformador.current(0)

mainloop()