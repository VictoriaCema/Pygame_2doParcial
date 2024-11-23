import pygame
import random

# Crear una ventana
medidas_ventana = (800, 600)
ventana = pygame.display.set_mode(medidas_ventana)
beige_clarito = (245, 245, 220) # Color de fondo

# Diccionario con la información del jugador
estado_jugador = {
    "nombre": "jugador",
    "vidas": 3,
    "antidotos": 0,
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
velocidad_pildora = 0.4

# Variables del virus
x_virus = random.randint(0, medidas_ventana[0] - ancho_virus)
y_virus = -alto_virus
velocidad_virus = 1.5  # El virus cae más rápido que la píldora

resultado = None

