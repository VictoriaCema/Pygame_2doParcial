import pygame
import random
from variables import *

# Inicializar Pygame
pygame.init()
# Inicializar el mezclador de audio
pygame.mixer.init()

reproducir_musica("C:/Users/Victoria/Desktop/SomvicksPygame/musica.mp3")

# Bucle principal (para que la ventana no se cierre de inmediato)

while True:
    opcion = mostrar_menu(ventana, medidas_ventana, beige_clarito)

    if opcion == "iniciar":
        # Inicia el juego (coloca aquí el bucle del juego)
        # Reiniciar estado del jugador y posiciones
        estado_jugador, x_pildora, y_pildora, x_virus, y_virus, x_somvicks, y_somvicks = inicializar_estado_juego()
        contador_pildora = 0
        resultado = None
        
    jugando = True
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Cerrar al hacer clic en la X de la ventana
                jugando = False
                
        # Mover el Somvicks de izquierda a derecha con las teclas de flechitas del teclado
        teclas = pygame.key.get_pressed()
        x_somvicks = mover_personaje(teclas, x_somvicks)
        
        # Hacer que la pildora caiga
        # Incrementar el contador de la píldora
        contador_pildora, x_pildora, y_pildora = actualizar_pildora(contador_pildora, x_pildora, y_pildora)
        x_virus, y_virus = actualizar_virus(x_virus, y_virus)
        
        rect_somvicks = pygame.Rect(x_somvicks, y_somvicks, ancho_somvicks, alto_somvicks)
        rect_pildora = pygame.Rect(x_pildora, y_pildora, ancho_pildora, alto_pildora)
        rect_virus = pygame.Rect(x_virus, y_virus, ancho_virus, alto_virus)
        
        # Colisión con píldora
        x_pildora, y_pildora, ganado = detectar_colision_pildora(rect_somvicks, rect_pildora, estado_jugador, medidas_ventana, sonido_pildora)

        if ganado and estado_jugador["pildoras"] >= 20:
                resultado = "ganaste"
                jugando = False

        # Colisión con virus
        x_virus, y_virus, colision = detectar_colision_virus(rect_somvicks, rect_virus, estado_jugador, medidas_ventana, sonido_virus)
        
        if estado_jugador["virus"] >= 3:
            estado_jugador["vidas"] -= 1
            estado_jugador["virus"] = 0
            print(f"¡Perdiste una vida! Vidas restantes: {estado_jugador['vidas']}")
            if estado_jugador["vidas"] <= 0:
                print("¡Game Over!")
                resultado = "perdiste"
                jugando = False
        
        # Dibujar pantalla
        dibujar_elementos(ventana, x_somvicks, y_somvicks,x_pildora, y_pildora, x_virus, y_virus)

    # Pantalla final
    pygame.mixer.music.stop()

    # Pantalla final
    mostrar_pantalla_final(ventana, resultado)
