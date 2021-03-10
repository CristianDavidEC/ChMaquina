from tkinter import ttk
from tkinter import *

from Archivo.CH import ArcivoCh
from CompiladorCh.Compilador import Compilador

class Ventana:
    def __init__(self, vent):
        self.wind = vent
        self.wind.title('StarsOS')
        self.wind.geometry('1300x700')

        # contenedor
        """frame =LabelFrame(self.wind, text = 'Hola')
        frame.grid(row = 1, column = 1, columnspan = 5, pady = 20)

        #entradas
        Label(frame, text = 'Nombre').grid(row = 2, column = 2)"""

        boton = ttk.Button(self.wind, text = "archivo", command = self.leer)
        boton.pack()

    def leer(self):
        ch = ArcivoCh()
        compila = Compilador()
        compila.sintaxis(ch.leer())

if __name__ == '__main__':
    window = Tk()
    aplicacion = Ventana(window)
    window.mainloop()
