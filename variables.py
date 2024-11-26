import pygame
import random
pygame.mixer.init()

# Crear una ventana
medidas_ventana = (800, 600)
ventana = pygame.display.set_mode(medidas_ventana)
beige_clarito = (245, 245, 220) # Color de fondo

# Diccionario con la información del jugador
estado_jugador = {
    "vidas": 3,
    "pildoras": 0,
    "virus": 0,
}

# Mostrar el estado inicial del jugador
print(estado_jugador)

# Carga del Somvicks!! <3
#somvicks = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/pequeñoSomvicksD.png") 
# Achicar a Somvicks
ancho_somvicks, alto_somvicks = 100, 100
somvicks_D = pygame.transform.scale((pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/pequeñoSomvicksD.png")), (ancho_somvicks, alto_somvicks))
somvicks_I = pygame.transform.scale((pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/pequeñoSomvicksI.png")), (ancho_somvicks, alto_somvicks)) 

# Estas variables guardan los datos de la pildora
pildora = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/pildora.png")
ancho_pildora, alto_pildora = 35, 35
pildora = pygame.transform.scale(pildora, (ancho_pildora, alto_pildora))

# Estas variables guardan los datos del virus verde
virus = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/virus.png")
ancho_virus, alto_virus = 50, 50
virus = pygame.transform.scale(virus, (ancho_virus, alto_virus))

#Estas variables guardan el virus mortal
virus_mortal = pygame.transform.scale(pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/virus1.png"), (ancho_virus, alto_virus))

#Estas variables guardan la pildora salvadora
ancho_pildora_salvadora, alto_pildora_salvadora = 50, 50
pildora_salvadora = pygame.transform.scale(pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/pildora_salvadora.png"), (alto_pildora_salvadora, ancho_pildora_salvadora))

# Fondo 
imagen_fondo = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/fondo2.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, medidas_ventana) 

# estas variables guardan la imagen que aparece cuando perdes
game_over_img = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/gameover.png")
game_over_img = pygame.transform.scale(game_over_img, (400, 300)) 

# Estas variables pertenece a la imagen que aparece cuanod ganas
ganaste_img = pygame.image.load("C:/Users/Victoria/Desktop/SomvicksPygame/ganaste.png")
ganaste_img = pygame.transform.scale(ganaste_img, (400, 300))


# Posición inicial del personaje
x_somvicks = (medidas_ventana[0] - ancho_somvicks) // 2  # Centrado horizontalmente
y_somvicks = 850 #medidas_ventana[1] + alto_somvicks  # En el borde inferior

# Velocidad de movimiento del personaje
velocidad_personaje = 7

# Variables de la píldora
x_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora)
y_pildora = -alto_pildora  # Comienza fuera de la pantalla (borde superior)
velocidad_pildora = 7

# Variables del virus
x_virus = random.randint(0, medidas_ventana[0] - ancho_virus)
y_virus = -alto_virus
velocidad_virus = 10

# Variables del virus mortal 
x_virus_mortal = random.randint(0, medidas_ventana[0] - ancho_virus)
y_virus_mortal = -alto_virus
velocidad_virus_mortal = 20

# Variables de la pildora salvadora
x_pildora_salvadora = random.randint(0, medidas_ventana[0] - 35)
y_pildora_salvadora = - 35
velocidad_pildora_salvadora = 10

resultado = None

# Estas variables guardan el sonido de cada colision y cuando ganas o perdes
sonido_pildora = pygame.mixer.Sound("C:/Users/Victoria/Desktop/SomvicksPygame/pildora.wav")
sonido_virus = pygame.mixer.Sound("C:/Users/Victoria/Desktop/SomvicksPygame/virus1.wav")
sonido_ganar = pygame.mixer.Sound("C:/Users/Victoria/Desktop/SomvicksPygame/ganar.wav")
sonido_perder = pygame.mixer.Sound("C:/Users/Victoria/Desktop/SomvicksPygame/perder.wav")



