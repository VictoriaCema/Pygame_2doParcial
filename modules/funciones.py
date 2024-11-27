import pygame
import random
from variables import *

def reproducir_musica(musica, volumen=0.2): # Cargar y reproduce la música de fondo
    pygame.mixer.music.load(musica)
    pygame.mixer.music.set_volume(volumen)  # Ajusta el volumen (0.0 a 1.0)
    pygame.mixer.music.play(-1)  # Esto repite la música indefinidamente

def detectar_colision_pildora(rect_personaje, rect_pildora, estado_jugador, medidas_ventana, sonido_pildora):
    """Maneja la colisión entre Somvicks y la píldora."""
    if rect_personaje.colliderect(rect_pildora):
        sonido_pildora.play()
        estado_jugador["pildoras"] += 1
        print(f"¡Pildoras recogidas: {estado_jugador['pildoras']}!")

        if estado_jugador["pildoras"] >9:
            global velocidad_virus
            velocidad_virus +=2
        # Reiniciar la posición de la píldora
        x_pildora = random.randint(0, medidas_ventana[0] - rect_pildora.width)
        y_pildora = -rect_pildora.height
        return x_pildora, y_pildora, True
        
    return rect_pildora.x, rect_pildora.y, False

def detectar_colision_virus(rect_personaje, rect_virus, estado_jugador, medidas_ventana, sonido_virus):
    """Maneja la colisión entre Somvicks y el virus."""
    if rect_personaje.colliderect(rect_virus):
        sonido_virus.play()
        estado_jugador["virus"] += 1
        print(f"¡Virus tocados: {estado_jugador['virus']}!")
        # Reiniciar la posición del virus
        x_virus = random.randint(0, medidas_ventana[0] - rect_virus.width)
        y_virus = -rect_virus.height
        return x_virus, y_virus, True
    return rect_virus.x, rect_virus.y, False

def detectar_colision_virus_mortal(rect_personaje, rect_virual_mortal, estado_jugador, medidas_ventana, sonido_virus):
    """Maneja la colisión entre Somvicks y el virus."""
    if rect_personaje.colliderect(rect_virual_mortal):
        sonido_virus.play()
        estado_jugador["vidas"] -= 1
        #print(f"¡Pildora salvadora tocada, ganaste una vida, vidas acumuladas: {estado_jugador['vidas']}!")

        # Reiniciar la posición del virus
        x_virus_mortal = random.randint(0, medidas_ventana[0] - rect_virual_mortal.width)
        y_virus_mortal = - rect_virual_mortal.height
        return x_virus_mortal, y_virus_mortal, True
    return rect_virual_mortal.x, rect_virual_mortal.y, False

def detectar_colision_pildora_salvadora(rect_personaje, rect_pildora_salvadora, estado_jugador, medidas_ventana, sonido_pildora):
    '''Muestra la colisión entre Somvicks y la pildora salvadora.'''
    if rect_personaje.colliderect(rect_pildora_salvadora):
        sonido_pildora.play()
        estado_jugador["vidas"] += 1
        #print(f"¡Pildora salvadora tocada, ganaste una vida, vidas acumuladas: {estado_jugador["vidas"]}!")
        x_pildora_salvadora = random.randint(0, medidas_ventana[0] - rect_pildora_salvadora.width)
        y_pildora_salvadora = - rect_pildora_salvadora.height
        return x_pildora_salvadora, y_pildora_salvadora, True
    return rect_pildora_salvadora.x, rect_pildora_salvadora.y, False

def mostrar_pantalla_final(ventana, resultado, medidas_ventana, img_ganaste, img_gameover, sonido_ganar, sonido_perder):
    """Muestra la pantalla final según el resultado del juego."""
    ventana.fill((0, 0, 0)) 
    if resultado == "ganaste":
        sonido_ganar.play()
        ventana.blit(img_ganaste, ((medidas_ventana[0] - 400) // 2, (medidas_ventana[1] - 300) // 2))
    elif resultado == "perdiste":
        sonido_perder.play()
        ventana.blit(img_gameover, ((medidas_ventana[0] - 400) // 2, (medidas_ventana[1] - 300) // 2))
    pygame.display.flip()

def mostrar_menu(ventana, medidas_ventana, beige_clarito):
    """Muestra el menú principal y gestiona las opciones del usuario."""
    menu_activo = True
    fuente = pygame.font.Font(None, 40) 
    ventana.fill(beige_clarito) 

    while menu_activo:
        ventana.fill(beige_clarito) 
        titulo = fuente.render("MENU PRINCIPAL", True, (128, 0, 32))
        opcion1 = fuente.render("1 - Iniciar Juego", True, (128, 0, 32))
        opcion2 = fuente.render("2 - Reglas del Juego", True, (128, 0, 32))
        opcion3 = fuente.render("3 - Salir", True, (128, 0, 32))

        ventana.blit(titulo, ((medidas_ventana[0] - titulo.get_width()) // 2, 100))
        ventana.blit(opcion1, ((medidas_ventana[0] - opcion1.get_width()) // 2, 200))
        ventana.blit(opcion2, ((medidas_ventana[0] - opcion2.get_width()) // 2, 250))
        ventana.blit(opcion3, ((medidas_ventana[0] - opcion3.get_width()) // 2, 300))

        pygame.display.flip() 

        for event in pygame.event.get(): # Esta parte captura los eventos del menu
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Opción 1: Iniciar juego
                    menu_activo = False  # Salir del menú
                    return "iniciar"
                elif event.key == pygame.K_2:  # Opción 2: Reglas
                    mostrar_reglas(ventana, medidas_ventana, beige_clarito, fuente)
                elif event.key == pygame.K_3:  # Opción 3: Salir
                    pygame.quit()
                    exit()  # Salir del programa

def mostrar_reglas(ventana, medidas_ventana, beige_clarito, fuente):
    """Muestra las reglas del juego en pantalla."""
    reglas_activo = True
    ventana.fill(beige_clarito)

    # Texto de las reglas
    reglas = [
        "REGLAS DEL JUEGO:",
        "",
        "1. Mueve a Somvicks con las flechas <- y ->.",
        "2. Atrapa las píldoras rosas para sumar puntos.",
        "3. Consigue 20 píldoras rosas para ganar.", 
        "4. Comienzas con 3 vidas",
        "5. Pierdes 1 vida cada 3 virus verdes que tocas.",
        "6. Pierdes 1 vida por cada virus rojo que tocas.",
        "7. La pildora amarilla te devuelve 1 vida. ",
        "",
        "Presiona ESC para volver al menú principal."
    ]

    while reglas_activo:
        ventana.fill(beige_clarito)  # Fondo beige

        # Renderizar y mostrar cada línea de texto
        for i, linea in enumerate(reglas):
            texto = fuente.render(linea, True, (128, 0, 32))
            ventana.blit(texto, (50, 100 + i * 40))  # Posición de las reglas

        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                reglas_activo = False  # Volver al menú principal

def inicializar_estado_juego():
    """Inicializa las variables del estado del juego y las posiciones."""
    global velocidad_virus #Declara que vamos a modificar la variable global
    velocidad_virus = 1 #Reinicia la velocidad al valor inicial
    estado_jugador = {"pildoras": 0, "virus": 0, "vidas": 3}
    x_pildora, y_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora), -alto_pildora
    x_virus, y_virus = random.randint(0, medidas_ventana[0] - ancho_virus), -alto_virus
    x_somvicks, y_somvicks = (medidas_ventana[0] - ancho_somvicks) // 2, medidas_ventana[1] - alto_somvicks
    #x_virus_mortal, y_virus_mortal = random.randint(0, medidas_ventana[0] - ancho_virus), - alto_virus
    x_virus_mortal, y_virus_mortal = random.randint(0, medidas_ventana[0] - ancho_virus), - alto_virus
    x_pildora_salvadora, y_pildora_salvadora = random.randint(0, medidas_ventana[0] - 35), - 35
    return estado_jugador, x_pildora, y_pildora, x_virus, y_virus, x_somvicks, y_somvicks, x_virus_mortal, y_virus_mortal, x_pildora_salvadora, y_pildora_salvadora


def mover_personaje(teclas, x_somvicks, direccion):
    """Controla el movimiento del personaje según las teclas presionadas."""
    if teclas[pygame.K_LEFT] and x_somvicks > 0:
        x_somvicks -= velocidad_personaje
        direccion = "izquierda"
    if teclas[pygame.K_RIGHT] and x_somvicks < medidas_ventana[0] - ancho_somvicks:
        x_somvicks += velocidad_personaje
        direccion = "derecha"
    return x_somvicks, direccion


def actualizar_pildora(x_pildora, y_pildora):
    """Actualiza la posición de la píldora."""
    y_pildora += velocidad_pildora
    if y_pildora > medidas_ventana[1]:
        x_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora)
        y_pildora = -alto_pildora
    return x_pildora, y_pildora


def actualizar_virus(x_virus, y_virus):
    """Actualiza la posición del virus."""
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

contador_pildora_salvadora = 0
probabilidad_pildora_salvadora = 0.1  # Ajusta este valor para cambiar la frecuencia
def actualizar_pildora_salvadora(x_pildora_salvadora, y_pildora_salvadora, probabilidad_pildora_salvadora, contador_pildora_salvadora):
    y_pildora_salvadora += velocidad_pildora_salvadora
    if y_pildora_salvadora > medidas_ventana[1]:
        if random.random() < probabilidad_pildora_salvadora:
            x_pildora_salvadora = random.randint(0, medidas_ventana[0] - ancho_pildora_salvadora)
            y_pildora_salvadora = - alto_pildora_salvadora
            contador_pildora_salvadora = 0 #Reinicia el contador
        else:
            contador_pildora_salvadora +=1
            x_pildora_salvadora, y_pildora_salvadora = -100, -100 #La mantiene fuera de la pantalla 
    return x_pildora_salvadora, y_pildora_salvadora


def dibujar_elementos(ventana, x_somvicks, y_somvicks, x_pildora, y_pildora, x_virus, y_virus, x_virus_mortal, y_virus_mortal, x_pildora_salvadora, y_pildora_salvadora, reloj, direccion):
    """Dibuja los elementos en la pantalla."""
    reloj.tick(60)
    ventana.blit(imagen_fondo, (0, 0))
    
    if direccion == "derecha":
        ventana.blit(somvicks_D, (x_somvicks, y_somvicks))
    else:
        ventana.blit(somvicks_I, (x_somvicks, y_somvicks))
    ventana.blit(pildora, (x_pildora, y_pildora))
    ventana.blit(virus, (x_virus, y_virus))
    ventana.blit(virus_mortal, (x_virus_mortal, y_virus_mortal))
    ventana.blit(pildora_salvadora, (x_pildora_salvadora, y_pildora_salvadora))
    pygame.display.flip()


def mostrar_pantalla_final(ventana, resultado):
    """Muestra la pantalla final según el resultado del juego."""
    if resultado == "ganaste":
        sonido_ganar.play()
        ventana.fill((0, 0, 0))
        ventana.blit(ganaste_img, ((medidas_ventana[0] - 700) // 2, (medidas_ventana[1] - 500) // 2))
    elif resultado == "perdiste":
        sonido_perder.play()
        ventana.fill((0, 0, 0))
        ventana.blit(game_over_img, ((medidas_ventana[0] - 700) // 2, (medidas_ventana[1] - 500) // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

def ranking(ventana, estado_jugador):
    texto = f"Vidas: {estado_jugador['vidas']}  Pildoras: {estado_jugador['pildoras']}  Virus: {estado_jugador['virus']}"
    fuente = pygame.font.SysFont("Arial Black", 36)
    mensaje = fuente.render(texto, True, (120, 40, 140)) 
    ventana.blit(mensaje, (0, 0))
    pygame.display.flip()
