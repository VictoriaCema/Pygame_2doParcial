import pygame
from variables import *
from funciones import *

# Inicializar Pygame
pygame.init()
# Inicializar el mezclador de audio
pygame.mixer.init()

reproducir_musica("C:/Users/Victoria/Desktop/SomvicksPygame/musica.mp3")

# Bucle inicial, muestra el menu principal con las reglas del juego
ejecutando = 1
while ejecutando == 1:
    opcion = mostrar_menu(ventana, medidas_ventana, beige_clarito)

    if opcion == "iniciar":
        
        # Reiniciar estado del jugador y posiciones por si se elije jugar otra partida 
        estado_jugador, x_pildora, y_pildora, x_virus, y_virus, x_somvicks, y_somvicks = inicializar_estado_juego()
        contador_pildora = 0
        resultado = None
        
        jugando = 1 # Bucle del juego propiamente dicho
        while jugando == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
                    jugando = 2

            # Colisión con virus
            x_virus, y_virus, colision = detectar_colision_virus(rect_somvicks, rect_virus, estado_jugador, medidas_ventana, sonido_virus)
            
            if estado_jugador["virus"] >= 3:
                estado_jugador["vidas"] -= 1
                estado_jugador["virus"] = 0
                print(f"¡Perdiste una vida! Vidas restantes: {estado_jugador['vidas']}")
                if estado_jugador["vidas"] <= 0:
                    print("¡Game Over!")
                    resultado = "perdiste"
                    jugando = 2
                    
            
            # Dibujar pantalla
            dibujar_elementos(ventana, x_somvicks, y_somvicks,x_pildora, y_pildora, x_virus, y_virus)
            
        # Pantalla final
        pygame.mixer.music.stop()
        mostrar_pantalla_final(ventana, resultado)
    
    elif opcion == "salir":
        ejecutando = 2
pygame.quit()
