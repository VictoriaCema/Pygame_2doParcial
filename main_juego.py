import pygame
import random

# Inicializar Pygame
pygame.init()

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

# Bucle principal (para que la ventana no se cierre de inmediato)
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
    y_pildora += velocidad_pildora
    # Mover el virus hacia abajo
    y_virus += velocidad_virus
    
    rect_somvicks = pygame.Rect(x_somvicks, y_somvicks, ancho_somvicks, alto_somvicks)
    rect_pildora = pygame.Rect(x_pildora, y_pildora, ancho_pildora, alto_pildora)
    rect_virus = pygame.Rect(x_virus, y_virus, ancho_virus, alto_virus)
    
    # Detectar colisión de la pildora con Somvicks
    if rect_somvicks.colliderect(rect_pildora):
        estado_jugador["antidotos"] += 1
        print(f"¡Antídotos recogidos: {estado_jugador['antidotos']}!")
        # Reiniciar la posición de la píldora
        x_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora)
        y_pildora = -alto_pildora
        
        # Condición para ganar el juego
        if estado_jugador["antidotos"] >= 20:
            print("¡Felicitaciones! Has ganado el juego.")
            resultado = "ganaste"
            jugando = False
            
    # Detectar colisión del virus con Somvicks
    if rect_somvicks.colliderect(rect_virus):
        estado_jugador["virus"] += 1
        print(f"¡Virus tocados: {estado_jugador['virus']}!")
        # Reiniciar la posición del virus
        x_virus = random.randint(0, medidas_ventana[0] - ancho_virus)
        y_virus = -alto_virus
    
    # Verificar si se acumulan 3 virus
    if estado_jugador["virus"] >= 3:
        estado_jugador["vidas"] -= 1
        estado_jugador["virus"] = 0  # Reiniciar el contador de virus
        print(f"¡Perdiste una vida! Vidas restantes: {estado_jugador['vidas']}")
    
        # Verificar si el jugador se queda sin vidas
        if estado_jugador["vidas"] <= 0:
            print("¡Game Over!")
            resultado = "perdiste"
            jugando = False
    
    # Reiniciar la píldora si cruza el borde inferior
    if y_pildora > medidas_ventana[1]:
        x_pildora = random.randint(0, medidas_ventana[0] - ancho_pildora)
        y_pildora = -alto_pildora
        
    # Reiniciar el virus si cruza el borde inferior
    if y_virus > medidas_ventana[1]:
        x_virus = random.randint(0, medidas_ventana[0] - ancho_virus)
        y_virus = -alto_virus
    
    ventana.fill(beige_clarito) # Fondo de la ventana
    ventana.blit(somvicks, (x_somvicks, y_somvicks))
    ventana.blit(pildora, (x_pildora, y_pildora))
    ventana.blit(virus, (x_virus, y_virus))
    
    pygame.display.flip() # Actualiza la ventana

# Mostrar pantalla final según el resultado del juego
if resultado == "ganaste":
    ventana.fill((0, 0, 0))  # Fondo negro
    ventana.blit(ganaste_img, ((medidas_ventana[0] - 400) // 2, (medidas_ventana[1] - 300) // 2))
elif resultado == "perdiste":
    ventana.fill((0, 0, 0))  # Fondo negro
    ventana.blit(game_over_img, ((medidas_ventana[0] - 400) // 2, (medidas_ventana[1] - 300) // 2))

pygame.display.flip()

# Esperar a que el usuario cierre la ventana
esperando = True
while esperando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esperando = False

# Salir de Pygame
pygame.quit()
