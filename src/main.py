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
frequencia_analogica = 1
minimo_tamanho_intervalo = 0
maximo_tamanho_intervalo = 15
analogico = True
digital = True

janela_principal.title("Gerador de Sinais")
janela_principal.resizable(True, True)
janela_principal.config(bg="white")
janela_principal.geometry("980x700")

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

graficos[0].set_ylabel("Sinal Analógico", fontweight='bold')
graficos[0].set_ylim(-2, 2)

# X/Y Sequencia de bits aleatorias
graficos[1].set_ylabel("Sequência de Bits", fontweight='bold')
graficos[1].set_ylim(-2, 2)

# X/Y Sinal digital referente a sequencia de bits
graficos[2].set_ylabel("Sinal Digital", fontweight='bold')
graficos[2].set_ylim(-2, 2)

# X/Y Pulso conformador
graficos[3].set_xlabel("Tempo")
graficos[3].set_ylabel("Pulso Conformador", fontweight='bold')
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


def analogico():
    global analogico
    if analogico:
        analogico = False
        analogicoBTN["text"] = "Mostar analógico"
    else:
        analogico = True
        analogicoBTN["text"] = "Ocutar analógico"


def digital():
    global digital
    if digital:
        digital = False
        digitalBTN["text"] = "Mostar digital"
    else:
        digital = True
        digitalBTN["text"] = "Ocutar digital"


def seno(intervalo):
    global freqAngular

    return np.sin(intervalo * freqAngular)


def gerarGrafico(i, eixo_x, eixo_y):
    global intervalo, iniciar
    global maximo_tamanho_intervalo, minimo_tamanho_intervalo
    global frequencia_analogica, frequencia_digital

    if iniciar:
        intervalo = np.linspace(
            minimo_tamanho_intervalo, maximo_tamanho_intervalo, 256
        ) * random.uniform(0.9, 1)

        # Sinal Analógico
        graficos[0].clear()
        graficos[0].set_ylim(-2, 2)
        graficos[0].set_ylabel("Sinal Analógico", fontweight='bold')

        # Sinal Sequência de Bits
        graficos[1].clear()
        graficos[1].set_ylim(-2, 2)
        graficos[1].set_ylabel("Sequência de Bits", fontweight='bold')

        # Sinal Digital referente a Sequência de Bits
        graficos[2].clear()
        graficos[2].set_ylim(-2, 2)
        graficos[2].set_ylabel("Sinal Digital", fontweight='bold')

        # Sinal Pulso Conformador
        graficos[3].clear()
        graficos[3].set_ylim(-2, 2)
        graficos[3].set_xlabel("Tempo", fontweight='bold')
        graficos[3].set_ylabel("Pulso Conformador", fontweight='bold')

        # Sinal Analógico
        sinal_analogico = np.sin(intervalo)
        graficos[0].plot(intervalo, sinal_analogico, "c")

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


def setFrequenciaAnalogica(event):
    global frequencia_analogica
    if float(inputFrequenciaAnalogica.get().replace(",", ".")) >= 0:
        frequencia_analogica = float(inputFrequenciaAnalogica.get().replace(",", "."))
        frequenciaAnalogicoInfoLabel["text"] = inputFrequenciaAnalogica.get()
    else:
        messagebox.showerror("Erro", "Frequência inválida")

    inputFrequenciaAnalogica.delete(0, END)


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


iniciarBTN = Button(janela_principal, width=24, height=3, bg="#d3d3d3", text="Iniciar", command=funcIniciar)
iniciarBTN.place(relx=0.87, rely=0.45, anchor=N)

analogicoBTN = Button(
    janela_principal, width=12, text="Ocutar analógico", bg="#00CED1", command=analogico
)
analogicoBTN.place(relx=0.92, rely=0.4, anchor=N)

digitalBTN = Button(
    janela_principal, width=12, text="Ocutar digital", bg="#C4302B", command=digital
)
digitalBTN.place(relx=0.82, rely=0.4, anchor=N)

######################################
############  Analógico   ############
######################################
frequenciaAnalogicoFrame = LabelFrame(
    janela_principal,
    text="Frequência Analógico",
    width=145,
    height=75,
    borderwidth=0,
)
frequenciaAnalogicoFrame.place(in_=janela_principal, relx=0.87, rely=0.2, anchor=CENTER)
frequenciaAnalogicoInfoLabel = Label(
    frequenciaAnalogicoFrame,
    text=str(frequencia_analogica),
)
frequenciaAnalogicoInfoLabel.place(relx=0.5, rely=0.15, anchor=N)
inputFrequenciaAnalogica = Entry(frequenciaAnalogicoFrame, width=12)
inputFrequenciaAnalogica.place(relx=0.5, rely=0.55, anchor=N)
inputFrequenciaAnalogica.bind("<Return>", setFrequenciaAnalogica)

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