import pygame
import random
pygame.mixer.init()

# Crear una ventana
medidas_ventana = (800, 600)
ventana = pygame.display.set_mode(medidas_ventana)
beige_clarito = (245, 245, 220) # Color de fondo

# Diccionario con la información del jugador
estado_jugador = {
    "nombre": "jugador",
    "vidas": 3,
    "pildoras": 0,
    "virus": 0
}

# Mostrar el estado inicial del jugador
print(estado_jugador)

# Carga del Somvicks!! <3
somvicks = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/pequeñoSomvicks.png")  # Reemplaza con la ruta de tu imagen
# Achicar a Somvicks
ancho_somvicks, alto_somvicks = 50, 50
somvicks = pygame.transform.scale(somvicks, (ancho_somvicks, alto_somvicks))  # Redimensiona a 50x50 píxeles

# Cargar y redimensionar la píldora
pildora = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/pildora.png")
ancho_pildora, alto_pildora = 25, 25
pildora = pygame.transform.scale(pildora, (ancho_pildora, alto_pildora))

# Cargar y redimensionar el virus
virus = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/virus.png")
ancho_virus, alto_virus = 40, 40
virus = pygame.transform.scale(virus, (ancho_virus, alto_virus))

# Cargar imagen de "Game Over"
game_over_img = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/gameover.png")
game_over_img = pygame.transform.scale(game_over_img, (400, 300))  # Ajustar tamaño

# Cargar imagen de "Ganaste"
ganaste_img = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/ganaste.png")
ganaste_img = pygame.transform.scale(ganaste_img, (400, 300))  # Ajustar tamaño


# Posición inicial del personaje
x_somvicks = (medidas_ventana[0] - ancho_somvicks) // 2  # Centrado horizontalmente
y_somvicks = medidas_ventana[1] - alto_somvicks  # En el borde inferior

# Velocidad de movimiento del personaje
velocidad_personaje = 0.5

# Variables de la píldora
x_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora)
y_pildora = -alto_pildora  # Comienza fuera de la pantalla (borde superior)
velocidad_pildora = 1
contador_pildora = 0  # Contador para controlar la caída de la píldora
caida_cada_n_frames = 2  # Mover la píldora cada 5 cuadros

# Variables del virus
x_virus = random.randint(0, medidas_ventana[0] - ancho_virus)
y_virus = -alto_virus
velocidad_virus = 1 # El virus cae más rápido que la píldora

resultado = None

# Cargar sonido
sonido_pildora = pygame.mixer.Sound("C:/Users/Victoria/Desktop/SomvicksPygame/pildora.wav")
sonido_virus = pygame.mixer.Sound("C:/Users/Victoria/Desktop/SomvicksPygame/virus1.wav")
sonido_ganar = pygame.mixer.Sound("C:/Users/Victoria/Desktop/SomvicksPygame/ganar.wav")
sonido_perder = pygame.mixer.Sound("C:/Users/Victoria/Desktop/SomvicksPygame/perder.wav")

def reproducir_musica(musica, volumen=0.4): # Cargar y reproducir música de fondo
    pygame.mixer.music.load(musica)
    pygame.mixer.music.set_volume(volumen)  # Ajusta el volumen (0.0 a 1.0)
    pygame.mixer.music.play(-1)  # Repetir la música indefinidamente

import random

def detectar_colision_pildora(rect_personaje, rect_pildora, estado_jugador, medidas_ventana, sonido_pildora):
    """Maneja la colisión entre Somvicks y la píldora."""
    if rect_personaje.colliderect(rect_pildora):
        sonido_pildora.play()
        estado_jugador["pildoras"] += 1
        print(f"¡Antídotos recogidos: {estado_jugador['pildoras']}!")
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

def mostrar_pantalla_final(ventana, resultado, medidas_ventana, img_ganaste, img_gameover, sonido_ganar, sonido_perder):
    """Muestra la pantalla final según el resultado del juego."""
    ventana.fill((0, 0, 0))  # Fondo negro
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
    fuente = pygame.font.Font(None, 40)  # Fuente para el texto
    ventana.fill(beige_clarito)  # Fondo del menú

    while menu_activo:
        ventana.fill(beige_clarito)  # Fondo beige
        # Renderizar texto
        titulo = fuente.render("MENU PRINCIPAL", True, (128, 0, 32))
        opcion1 = fuente.render("1 - Iniciar Juego", True, (128, 0, 32))
        opcion2 = fuente.render("2 - Reglas del Juego", True, (128, 0, 32))
        opcion3 = fuente.render("3 - Salir", True, (128, 0, 32))

        # Posicionar texto en la pantalla
        ventana.blit(titulo, ((medidas_ventana[0] - titulo.get_width()) // 2, 100))
        ventana.blit(opcion1, ((medidas_ventana[0] - opcion1.get_width()) // 2, 200))
        ventana.blit(opcion2, ((medidas_ventana[0] - opcion2.get_width()) // 2, 250))
        ventana.blit(opcion3, ((medidas_ventana[0] - opcion3.get_width()) // 2, 300))

        pygame.display.flip()  # Actualizar pantalla

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # Salir del programa

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
        "1. Mueve Somvicks con las flechas izquierda y derecha.",
        "2. Atrapa las píldoras para sumar puntos.",
        "3. Evita los virus o perderás vidas.",
        "4. Consigue 20 píldoras para ganar.",
        "5. Pierdes si te quedas sin vidas.",
        "Presiona ESC para volver al menú principal."
    ]

    while reglas_activo:
        ventana.fill(beige_clarito)  # Fondo beige

        # Renderizar y mostrar cada línea de texto
        for i, linea in enumerate(reglas):
            texto = fuente.render(linea, True, (0, 0, 0))
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
    estado_jugador = {"pildoras": 0, "virus": 0, "vidas": 3}
    x_pildora, y_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora), -alto_pildora
    x_virus, y_virus = random.randint(0, medidas_ventana[0] - ancho_virus), -alto_virus
    x_somvicks, y_somvicks = (medidas_ventana[0] - ancho_somvicks) // 2, medidas_ventana[1] - alto_somvicks - 20
    return estado_jugador, x_pildora, y_pildora, x_virus, y_virus, x_somvicks, y_somvicks


def mover_personaje(teclas, x_somvicks):
    """Controla el movimiento del personaje según las teclas presionadas."""
    if teclas[pygame.K_LEFT] and x_somvicks > 0:
        x_somvicks -= velocidad_personaje
    if teclas[pygame.K_RIGHT] and x_somvicks < medidas_ventana[0] - ancho_somvicks:
        x_somvicks += velocidad_personaje
    return x_somvicks


def actualizar_pildora(contador_pildora, x_pildora, y_pildora):
    """Actualiza la posición de la píldora."""
    contador_pildora += 1
    if contador_pildora >= caida_cada_n_frames:
        y_pildora += 1
        contador_pildora = 0

    if y_pildora > medidas_ventana[1]:
        x_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora)
        y_pildora = -alto_pildora
    return contador_pildora, x_pildora, y_pildora


def actualizar_virus(x_virus, y_virus):
    """Actualiza la posición del virus."""
    y_virus += velocidad_virus
    if y_virus > medidas_ventana[1]:
        x_virus = random.randint(0, medidas_ventana[0] - ancho_virus)
        y_virus = -alto_virus
    return x_virus, y_virus


def dibujar_elementos(ventana, x_somvicks, y_somvicks, x_pildora, y_pildora, x_virus, y_virus):
    """Dibuja los elementos en la pantalla."""
    ventana.fill(beige_clarito)
    ventana.blit(somvicks, (x_somvicks, y_somvicks))
    ventana.blit(pildora, (x_pildora, y_pildora))
    ventana.blit(virus, (x_virus, y_virus))
    pygame.display.flip()


def mostrar_pantalla_final(ventana, resultado):
    """Muestra la pantalla final según el resultado del juego."""
    if resultado == "ganaste":
        sonido_ganar.play()
        ventana.fill((0, 0, 0))
        ventana.blit(ganaste_img, ((medidas_ventana[0] - 400) // 2, (medidas_ventana[1] - 300) // 2))
    elif resultado == "perdiste":
        sonido_perder.play()
        ventana.fill((0, 0, 0))
        ventana.blit(game_over_img, ((medidas_ventana[0] - 400) // 2, (medidas_ventana[1] - 300) // 2))
    pygame.display.flip()
    pygame.time.wait(3000)