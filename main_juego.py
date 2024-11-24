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
        estado_jugador = {"pildoras": 0, "virus": 0, "vidas": 3}
        x_pildora, y_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora), -alto_pildora
        x_virus, y_virus = random.randint(0, medidas_ventana[0] - ancho_virus), -alto_virus
        x_somvicks, y_somvicks = (medidas_ventana[0] - ancho_somvicks) // 2, medidas_ventana[1] - alto_somvicks - 20
        contador_pildora = 0
        resultado = None
        
    jugando = True
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Cerrar al hacer clic en la X de la ventana
                jugando = False
                
        # Mover el Somvicks de izquierda a derecha con las teclas de flechitas del teclado
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and x_somvicks > 0:
            x_somvicks -= velocidad_personaje
        if teclas[pygame.K_RIGHT] and x_somvicks < medidas_ventana[0] - ancho_somvicks:
            x_somvicks += velocidad_personaje
        
        # Hacer que la pildora caiga
        # Incrementar el contador de la píldora
        contador_pildora += 1
        if contador_pildora >= caida_cada_n_frames:
            y_pildora += 1  # Incrementa en 1 (entero)
            contador_pildora = 0  # Reinicia el contador

        # Reiniciar la píldora si cruza el borde inferior
        if y_pildora > medidas_ventana[1]:
            x_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora)
            y_pildora = -alto_pildora
            
        # Mover el virus hacia abajo
        y_virus += velocidad_virus
        
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
        
        # Reiniciar el virus si cruza el borde inferior
        if y_virus > medidas_ventana[1]:
            x_virus = random.randint(0, medidas_ventana[0] - ancho_virus)
            y_virus = -alto_virus
        
        # Dibujar elementos
        ventana.fill(beige_clarito)
        ventana.blit(somvicks, (x_somvicks, y_somvicks))
        ventana.blit(pildora, (x_pildora, y_pildora))
        ventana.blit(virus, (x_virus, y_virus))
        pygame.display.flip()

    # Pantalla final
    pygame.mixer.music.stop()

    # Mostrar pantalla final según el resultado del juego
    if resultado == "ganaste":
        sonido_ganar.play()
        ventana.fill((0, 0, 0))  # Fondo negro
        ventana.blit(ganaste_img, ((medidas_ventana[0] - 400) // 2, (medidas_ventana[1] - 300) // 2))
    elif resultado == "perdiste":
        sonido_perder.play()
        ventana.fill((0, 0, 0))  # Fondo negro
        ventana.blit(game_over_img, ((medidas_ventana[0] - 400) // 2, (medidas_ventana[1] - 300) // 2))

    pygame.display.flip()
    pygame.time.wait(3000)  # Esperar 3 segundos antes de volver al menú