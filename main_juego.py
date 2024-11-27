import pygame
from modules.variables import *
from modules.funciones import *

# Inicializar Pygame
pygame.init()

# Inicializar el mezclador de audio
pygame.mixer.init()

reloj = pygame.time.Clock()
#reproducir_musica("C:/Users/Victoria/Desktop/SomvicksPygame/musica.mp3")

nombre = "Somvicks"
pygame.display.set_caption(nombre)
icono = pygame.image.load("C:/Users/byawe/OneDrive/Escritorio/pygame parcial/Pygame_2doParcial/assets/imagenes/pequeñoSomvicksD.png")
pygame.display.set_icon(icono)

# Bucle inicial, muestra el menu principal con las reglas del juego
ejecutando = 1
while ejecutando == 1:
    opcion = mostrar_menu(ventana, medidas_ventana, beige_clarito)

    if opcion == "iniciar":
        
        # Reiniciar estado del jugador y posiciones por si se elije jugar otra partida 
        estado_jugador, x_pildora, y_pildora, x_virus, y_virus, x_somvicks, y_somvicks, x_virus_mortal, y_virus_mortal, x_pildora_salvadora, y_pildora_salvadora = inicializar_estado_juego() 
        resultado = None
        direccion = "derecha"
        
        jugando = 1 # Bucle del juego propiamente dicho
        while jugando == 1:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando = False
                    
            # Mover el Somvicks de izquierda a derecha con las teclas de flechitas del teclado
            teclas = pygame.key.get_pressed()
            x_somvicks, direccion = mover_personaje(teclas, x_somvicks, direccion)
            
            # Hacer que la pildora, el virus comun, el virus mortal y la pildora salvadora caigan
            x_pildora, y_pildora = actualizar_pildora(x_pildora, y_pildora)
            x_virus, y_virus = actualizar_virus(x_virus, y_virus)
            x_virus_mortal, y_virus_mortal = actualizar_virus_mortal(x_virus_mortal, y_virus_mortal)
            x_pildora_salvadora, y_pildora_salvadora = actualizar_pildora_salvadora(x_pildora_salvadora, y_pildora_salvadora, probabilidad_pildora_salvadora)
            
            
            rect_somvicks = pygame.Rect(x_somvicks, y_somvicks, ancho_somvicks, alto_somvicks)
            rect_pildora = pygame.Rect(x_pildora, y_pildora, ancho_pildora, alto_pildora)
            rect_virus = pygame.Rect(x_virus, y_virus, ancho_virus, alto_virus)
            rect_virus_mortal = pygame.Rect(x_virus_mortal, y_virus_mortal, ancho_virus, alto_virus)
            rect_pildora_salvadora = pygame.Rect(x_pildora_salvadora, y_pildora_salvadora, ancho_pildora_salvadora, alto_pildora_salvadora)
            
            # Colisión con píldora
            x_pildora, y_pildora, ganado = detectar_colision_pildora(rect_somvicks, rect_pildora, estado_jugador, medidas_ventana, sonido_pildora)

            if ganado and estado_jugador["pildoras"] >= 20:
                    resultado = "ganaste"
                    jugando = 2

            # Colisión con virus
            x_virus, y_virus, colision = detectar_colision_virus(rect_somvicks, rect_virus, estado_jugador, medidas_ventana, sonido_virus)
            
            # Colisión con virus mortal 
            x_virus_mortal, y_virus_mortal, colision = detectar_colision_virus_mortal(rect_somvicks, rect_virus_mortal, estado_jugador, medidas_ventana, sonido_virus)
            

            def actualizar_estado_jugador(estado_jugador):
                if estado_jugador["virus"] >= 3:
                    estado_jugador["vidas"] -= 1
                    estado_jugador["virus"] = 0
                    print(f"¡Perdiste una vida! Vidas restantes: {estado_jugador['vidas']}")
                
                if estado_jugador["vidas"] <= 0:
                    print("¡Game Over!")
                    resultado = "perdiste"
                    jugando = 2
                    return resultado, jugando
                return None, 1 # Devuelve None y un valor por defecto para "jugando" si no se cumple la condición de "Game Over"

            resultado, jugando = actualizar_estado_jugador(estado_jugador)

            # Colision con pildora salvadora 
            x_pildora_salvadora, y_pildora_salvadora, ganado1 = detectar_colision_pildora_salvadora(rect_somvicks, rect_pildora_salvadora, estado_jugador, medidas_ventana, sonido_pildora)
            
            # Dibujar pantalla                                 
            dibujar_elementos(ventana, x_somvicks, y_somvicks,x_pildora, y_pildora, x_virus, y_virus, x_virus_mortal, y_virus_mortal, x_pildora_salvadora, y_pildora_salvadora, reloj, direccion)
            
            ranking(ventana, estado_jugador)
            
        
        # Pantalla final
        pygame.mixer.music.stop()
        mostrar_pantalla_final(ventana, resultado)
    
    elif opcion == "salir":
        ejecutando = 2
pygame.quit()
