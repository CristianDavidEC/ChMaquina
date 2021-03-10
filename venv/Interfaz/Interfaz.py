import pygame
import random
import pygame_gui
from pygame.locals import *


import pygame
import pygame_gui

from Archivo.CH import ArcivoCh
from CompiladorCh.Compilador import Compilador


def __init__ ():
    ch = ArcivoCh()
    compila = Compilador()

    #Pygame inicia
    pygame.init()
    
    #Dimensiones
    ancho = 1200
    alto = 700
    
    #titulo ventana
    pygame.display.set_caption('StarsOS')
    #Crea la pantalla
    window_surface = pygame.display.set_mode((ancho, alto))

    #Define el fondo
    #background = pygame.Surface((ancho, alto))
    #background.fill(pygame.Color('#062761'))
    fondo = pygame.image.load('../Recursos/Archivos/fondo5.jpeg')

    #icono de ventana
    icon = pygame.image.load('../Recursos/Archivos/ico.png')
    pygame.display.set_icon(icon)

    #Entorno de Pygame-Guy administra los eventos y elementos de Pygame-Guy
    manager = pygame_gui.UIManager((ancho, alto))

##_________________________________________Elementos de Pygame_______________________________________________________
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                text='Say Hello',
                                                manager=manager)
##___________________________________________________________________________________________________________________

    clock = pygame.time.Clock()
    is_running = True

#-----------Ciclo principal de la ventana y ejecucion de la interfaz del programa-----------------
    while is_running:
        time_delta = clock.tick(60)/1000.0

#-------------Manejador de eventos de la interfaz---------------------
        for event in pygame.event.get():
            #Cierra el programa
            if event.type == pygame.QUIT:
                is_running = False

#---------------Manejador de eventos de Pygame-Gui------------------------
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        compila.sintaxis(ch.leer())


            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(fondo, (0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()



iniciar =__init__()