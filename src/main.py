from tkinter import *
from tkinter import messagebox
import matplotlib
import matplotlib.animation as animation
from scipy import signal
import numpy as np
import random

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

janela_principal = Tk()
iniciar = False
frequencia_digital = 2
taxa_simbolo = 3
minimo_tamanho_intervalo = 0
maximo_tamanho_intervalo = 15
taxaSimbolo = True
digital = True

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
graficos[0].set_xlabel("Tempo")
graficos[0].set_ylabel("Sinal Analogico")
graficos[0].set_ylim(-2, 2)

# X/Y Sequencia de bits aleatorias
graficos[1].set_xlabel("Tempo")
graficos[1].set_ylabel("Sequencia de Bits")
graficos[1].set_ylim(-2, 2)

# X/Y Sinal digital referente a sequencia de bits
graficos[2].set_xlabel("Tempo")
graficos[2].set_ylabel("Sinal Digital")
graficos[2].set_ylim(-2, 2)

# X/Y Pulso conformador
graficos[3].set_xlabel("Tempo")
graficos[3].set_ylabel("Pulso Conformador")
graficos[3].set_ylim(-2, 2)

canvas = FigureCanvasTkAgg(f, janela_principal)
grafico = canvas.get_tk_widget().place(x=1, y=1, relx=0.01, rely=0.01)


def funcIniciar():
    global iniciar
    if iniciar:
        iniciar = False
        iniciarBTN["text"] = "Iniciar"
    else:
        iniciar = True
        iniciarBTN["text"] = "Pausar"


def seno(intervalo):
    global freqAngular

    return np.sin(intervalo * freqAngular)


def gerarGrafico(i, eixo_x, eixo_y):
    global intervalo, iniciar
    global maximo_tamanho_intervalo, minimo_tamanho_intervalo
    global taxa_simbolo, frequencia_digital

    if iniciar:
        intervalo = np.linspace(
            minimo_tamanho_intervalo, maximo_tamanho_intervalo, 256
        ) * random.uniform(0.9, 1)

        # Sinal Analógico
        graficos[0].clear()
        graficos[0].set_ylim(-2, 2)
        graficos[0].set_xlabel("Tempo")
        graficos[0].set_ylabel("Amplitude")

        # Sinal Sequência de Bits
        graficos[1].clear()
        graficos[1].set_ylim(-2, 2)
        graficos[1].set_xlabel("Tempo")
        graficos[1].set_ylabel("Amplitude")

        # Sinal Digital referente a Sequência de Bits
        graficos[2].clear()
        graficos[2].set_ylim(-2, 2)
        graficos[2].set_xlabel("Tempo")
        graficos[2].set_ylabel("Amplitude")

        # Sinal Pulso Conformador
        graficos[3].clear()
        graficos[3].set_ylim(-2, 2)
        graficos[3].set_xlabel("Tempo")
        graficos[3].set_ylabel("Amplitude")

        # Sinal Analógico
        taxaSimbolo = np.sin(intervalo)
        graficos[0].plot(intervalo, taxaSimbolo, "c")

        # Sinal Sequência de Bits
        sinal_senquencia_bits = signal.square(intervalo)
        graficos[1].plot(
            intervalo,
            sinal_senquencia_bits,
            "r",
        )

        # Sinal Digital referente a Sequência de Bits
        sinal_digital = signal.square(intervalo)
        graficos[2].plot(
            intervalo,
            sinal_digital,
            "r",
        )
        # Sinal Pulso Conformador
        sinal_digital = signal.square(intervalo)
        graficos[3].plot(
            intervalo,
            sinal_digital,
            "r",
        )

        maximo_tamanho_intervalo += 1
        minimo_tamanho_intervalo += 1


def setTaxaSimbolo(event):
    global taxa_simbolo
    if float(inputTaxaSimbolo.get().replace(",", ".")) >= 0:
        taxa_simbolo = float(inputTaxaSimbolo.get().replace(",", "."))
        taxa_simbolo_InfoLabel["text"] = inputTaxaSimbolo.get()
    else:
        messagebox.showerror("Erro", "Taxa de símbolos inválida")

    inputTaxaSimbolo.delete(0, END)


def setFrequenciaDigital(event):
    global frequencia_digital
    if float(inputFrequenciaDigital.get().replace(",", ".")) >= 0:
        frequencia_digital = float(inputFrequenciaDigital.get().replace(",", "."))
        frequenciaDigitalInfoLabel["text"] = inputFrequenciaDigital.get()
    else:
        messagebox.showerror("Erro", "Frequência inválida")

    inputFrequenciaDigital.delete(0, END)


ani = animation.FuncAnimation(
    f,
    gerarGrafico,
    fargs=(eixo_x, eixo_y),
    interval=500,
)

# Botão iniciar
iniciarBTN = Button(janela_principal, width=24, height=3, bg="#d3d3d3", text="Iniciar", command=funcIniciar)
iniciarBTN.place(relx=0.87, rely=0.65, anchor=N)

######################################
########  Taxa de Símbolos   #########
######################################
taxa_simbolo_Frame = LabelFrame(
    janela_principal,
    text="Taxa de Símbolos",
    width=145,
    height=75,
    borderwidth=0,
)
taxa_simbolo_Frame.place(in_=janela_principal, relx=0.87, rely=0.2, anchor=CENTER)
taxa_simbolo_InfoLabel = Label(
    taxa_simbolo_Frame,
    text=str(taxa_simbolo),
)
taxa_simbolo_InfoLabel.place(relx=0.5, rely=0.15, anchor=N)
inputTaxaSimbolo = Entry(taxa_simbolo_Frame, width=12)
inputTaxaSimbolo.place(relx=0.5, rely=0.55, anchor=N)
inputTaxaSimbolo.bind("<Return>", setTaxaSimbolo)

######################################
############    Digital   ############
######################################
frequenciaDigitalFrame = LabelFrame(
    janela_principal,
    text="Frequência Digital",
    width=145,
    height=75,
    borderwidth=0,
)
frequenciaDigitalFrame.place(in_=janela_principal, relx=0.87, rely=0.32, anchor=CENTER)
frequenciaDigitalInfoLabel = Label(
    frequenciaDigitalFrame,
    text=str(frequencia_digital),
)
frequenciaDigitalInfoLabel.place(relx=0.5, rely=0.15, anchor=N)
inputFrequenciaDigital = Entry(frequenciaDigitalFrame, width=12)
inputFrequenciaDigital.place(relx=0.5, rely=0.55, anchor=N)
inputFrequenciaDigital.bind("<Return>", setFrequenciaDigital)


mainloop()