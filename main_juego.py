import pygame
from modules.variables import *
from modules.funciones import *
# Inicializar Pygame
pygame.init()

# Inicializar el mezclador de audio
pygame.mixer.init()

reloj = pygame.time.Clock() # Limita los fps del juego
reproducir_musica("C:/Users/Victoria/Desktop/SomvicksPygame/assets/audios/musica.mp3")

nombre = "Somvicks"
pygame.display.set_caption(nombre)
icono = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/assets/imagenes/pequeñoSomvicksD.png")
pygame.display.set_icon(icono)

# Bucle inicial, muestra el menu principal con las reglas del juego

while ejecutando == 1:
    opcion = mostrar_menu(ventana, medidas_ventana, beige_clarito)

    if opcion == "iniciar":
        
        # Reiniciar estado del jugador y posiciones por si se elije jugar otra partida 
        estado_jugador, x_pildora, y_pildora, x_virus, y_virus, x_somvicks, y_somvicks, x_virus_mortal, y_virus_mortal, x_pildora_salvadora, y_pildora_salvadora = inicializar_estado_juego() 
        
        # Bucle del juego propiamente dicho
        while jugando == 1:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando = 2
                    quit()
                    
            # Mover el Somvicks de izquierda a derecha con las teclas de flechitas del teclado
            teclas = pygame.key.get_pressed()
            x_somvicks, direccion = mover_personaje(teclas, x_somvicks, direccion)
            
            # Hacer que los objetos caigan
            x_pildora, y_pildora = actualizar_objeto(x_pildora, y_pildora, velocidad_pildora, ancho_pildora, alto_pildora)
            
            velocidad_virus = aumentar_velocidad_virus(velocidad_virus, estado_jugador)
            
            x_virus, y_virus = actualizar_objeto(x_virus, y_virus, velocidad_virus, ancho_virus, alto_virus)
            
            x_virus_mortal, y_virus_mortal = actualizar_objeto(x_virus_mortal, y_virus_mortal, velocidad_virus_mortal, ancho_virus, alto_virus)      
            
            x_pildora_salvadora, y_pildora_salvadora = actualizar_pildora_salvadora(x_pildora_salvadora, y_pildora_salvadora, probabilidad_pildora_salvadora)
            
            # Rectangulos de cada objeto colisionable 
            rect_somvicks = pygame.Rect(x_somvicks, y_somvicks, ancho_somvicks, alto_somvicks)
            rect_pildora = pygame.Rect(x_pildora, y_pildora, ancho_pildora, alto_pildora)
            rect_virus = pygame.Rect(x_virus, y_virus, ancho_virus, alto_virus)
            rect_virus_mortal = pygame.Rect(x_virus_mortal, y_virus_mortal, ancho_virus, alto_virus)
            rect_pildora_salvadora = pygame.Rect(x_pildora_salvadora, y_pildora_salvadora, ancho_pildora_salvadora, alto_pildora_salvadora)
            
            # Colisión con píldora
            x_pildora, y_pildora, ganado = detectar_colision("pildora",rect_somvicks, rect_pildora, estado_jugador, medidas_ventana)
            
            # Colisión con virus
            x_virus, y_virus, colision = detectar_colision("virus", rect_somvicks, rect_virus, estado_jugador, medidas_ventana)
            
            # Colisión con virus mortal
            x_virus_mortal, y_virus_mortal, colision = detectar_colision("virus_mortal", rect_somvicks, rect_virus_mortal, estado_jugador, medidas_ventana )
            
            # Colision con pildora salvadora
            x_pildora_salvadora, y_pildora_salvadora, ganado1 = detectar_colision("pildora_salvadora", rect_somvicks, rect_pildora_salvadora, estado_jugador, medidas_ventana)
            
            #actualizar_estado_jugador(estado_jugador)
            resultado, jugando = chequear_ganar_perder(estado_jugador)
            
            actualizar_estado_virus(estado_jugador)

            # Dibujar pantalla                                 
            dibujar_elementos(ventana, x_somvicks, y_somvicks,x_pildora, y_pildora, x_virus, y_virus, x_virus_mortal, y_virus_mortal, x_pildora_salvadora, y_pildora_salvadora, reloj, direccion)
            
            ranking(ventana, estado_jugador)
            
        # Pantalla final
        pygame.mixer.music.stop()
        mostrar_pantalla_final(ventana, resultado)
    
    elif opcion == "salir":
        ejecutando = 2
pygame.quit()
