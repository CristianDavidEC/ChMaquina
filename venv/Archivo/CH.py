from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

class ArcivoCh:
    #Lee los archivos .ch y los dibido por \n , cada linea es un valor de un arreglo
    def leer(self):
        Tk().withdraw()
        aplicacion_ch= filedialog.askopenfilename(initialdir='D: Documents/')
        archivo = open(aplicacion_ch, 'r')

        contenido = archivo.read()
        code = contenido.split('\n')

        return (code) 
        







