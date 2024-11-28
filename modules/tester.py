import pygame
from modules.variables import *
from modules.funciones import *

def actualizar_objeto(objeto, x_objeto, y_objeto, velocidad_objeto, ancho_objeto, alto_objeto):
    # Actualiza los objetos 
    y_objeto += velocidad_objeto
    if y_objeto > medidas_ventana[1]:
        x_objeto = random.randint(0, medidas_ventana[0] - ancho_objeto)
        y_objeto = - alto_objeto
    return x_objeto, y_objeto

def actualizar_pildora(x_pildora, y_pildora):
    """Actualiza la posición de la píldora."""
    y_pildora += velocidad_pildora
    if y_pildora > medidas_ventana[1]:
        x_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora)
        y_pildora = -alto_pildora

    return x_pildora, y_pildora

def actualizar_virus(x_virus, y_virus):
    """Actualiza la posición del virus."""
    global velocidad_virus
    y_virus += velocidad_virus
    if y_virus > medidas_ventana[1]:
        x_virus = random.randint(0, medidas_ventana[0] - ancho_virus)
        y_virus = -alto_virus
    return x_virus, y_virus

def actualizar_virus_mortal(x_virus_mortal, y_virus_mortal):
    y_virus_mortal += velocidad_virus_mortal
    if y_virus_mortal > medidas_ventana[1]:
        x_virus_mortal = random.randint(0, medidas_ventana[0] - ancho_virus)
        y_virus_mortal = - alto_virus
    return x_virus_mortal, y_virus_mortal

def actualizar_pildora_salvadora(x_pildora_salvadora, y_pildora_salvadora, probabilidad_pildora_salvadora):
    y_pildora_salvadora += velocidad_pildora_salvadora
    if y_pildora_salvadora > medidas_ventana[1]:
        if random.random() > probabilidad_pildora_salvadora:
            x_pildora_salvadora = random.randint(0, medidas_ventana[0] - ancho_pildora_salvadora)
            y_pildora_salvadora = - alto_pildora_salvadora
        else:
            x_pildora_salvadora, y_pildora_salvadora = -100, -100 #La mantiene fuera de la pantalla 
    return x_pildora_salvadora, y_pildora_salvadora

    # if objeto == "pildora_salvadora":
    #     if random.random() > probabilidad_pildora_salvadora:
    #         x_objeto = random.randint(0, medidas_ventana[0] - ancho_pildora_salvadora)
    #         y_objeto = - alto_pildora_salvadora
    #     else:
    #         x_objeto, y_objeto = -100, -100 #La mantiene fuera de la pantalla 
    # return x_objeto, y_objeto
