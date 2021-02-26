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

root = Tk()
iniciar = False
frequencia_digital = 2
frequencia_analogica = 1
minimo_tamanho_intervalo = 0
maximo_tamanho_intervalo = 15
analogico = True
digital = True

root.title("Gerador de Sinais")
root.resizable(True, True)
root.config(bg="white")
root.geometry("860x600")

f = Figure(figsize=(10, 6), dpi=85)
a = f.add_subplot(111)
x = [0]
y = [0]
a.plot(x, y)
a.set_xlabel("Tempo")
a.set_ylabel("Amplitude")
a.set_ylim(-2, 5)
canvas = FigureCanvasTkAgg(f, root)
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


def gerarGrafico(i, x, y):
    global intervalo, iniciar
    global maximo_tamanho_intervalo, minimo_tamanho_intervalo
    global frequencia_analogica, frequencia_digital

    if iniciar:
        intervalo = np.linspace(
            minimo_tamanho_intervalo, maximo_tamanho_intervalo, 256
        ) * random.uniform(0.9, 1)

        a.clear()
        a.set_ylim(-2, 2)
        a.set_xlabel("Tempo")
        a.set_ylabel("Amplitude")

        # analógico
        if analogico:
            freqAngularAnalogica = 2 * np.pi * frequencia_analogica
            sinalseno = np.sin(intervalo * freqAngularAnalogica) * random.uniform(
                0.9, 1
            )
            a.plot(intervalo, sinalseno, "c")

        # digital
        if digital:
            freqAngularDigital = 2 * np.pi * frequencia_digital
            sinalQuadrado = signal.square(intervalo * freqAngularDigital)
            a.plot(
                intervalo,
                sinalQuadrado,
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
    fargs=(x, y),
    interval=500,
)

iniciarBTN = Button(root, width=9, text="Iniciar", command=funcIniciar)
iniciarBTN.place(relx=0.9, rely=0.9, anchor=N)

analogicoBTN = Button(
    root, width=12, text="Ocutar analógico", bg="#00CED1", command=analogico
)
analogicoBTN.place(relx=0.75, rely=0.9, anchor=N)

digitalBTN = Button(
    root, width=12, text="Ocutar digital", bg="#C4302B", command=digital
)
digitalBTN.place(relx=0.6, rely=0.9, anchor=N)

######################################
############  Analógico   ############
######################################
frequenciaAnalogicoFrame = LabelFrame(
    root,
    text="Frequência Analógico",
    width=145,
    height=75,
    borderwidth=0,
)
frequenciaAnalogicoFrame.place(in_=root, relx=0.15, rely=0.9, anchor=CENTER)
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
    root,
    text="Frequência Digital",
    width=120,
    height=75,
    borderwidth=0,
)
frequenciaDigitalFrame.place(in_=root, relx=0.4, rely=0.9, anchor=CENTER)
frequenciaDigitalInfoLabel = Label(
    frequenciaDigitalFrame,
    text=str(frequencia_digital),
)
frequenciaDigitalInfoLabel.place(relx=0.5, rely=0.15, anchor=N)
inputFrequenciaDigital = Entry(frequenciaDigitalFrame, width=12)
inputFrequenciaDigital.place(relx=0.5, rely=0.55, anchor=N)
inputFrequenciaDigital.bind("<Return>", setFrequenciaDigital)


mainloop()