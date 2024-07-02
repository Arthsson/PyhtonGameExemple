import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir o tamanho da janela
screen = pygame.display.set_mode((800, 600))

# Definir o título da janela
pygame.display.set_caption("Asteroids")

# Definir a cor de fundo
background_color = (0, 0, 0)

# Carregar a imagem da nave espacial
image = pygame.image.load('spaceship.png')
spaceshipImage = pygame.transform.scale(image, (int(image.get_width() * 0.1), int(image.get_height() * 0.1)))

# Obter o retângulo da nave espacial
rectSpaceship = spaceshipImage.get_rect()
rectSpaceship.center = (400, 600)

# Parâmetros de velocidade
speed_y = -0.6  # Definir uma velocidade inicial negativa para movimento para cima
acceleration = 0.1
max_speed = 10
min_speed = 0.6  # Velocidade mínima constante

# Configurar o controle de frame rate
clock = pygame.time.Clock()
fps = 60  # Definir o número de frames por segundo (FPS)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_UP]:
        speed_y = max(speed_y - acceleration, -max_speed)
    elif teclas[pygame.K_DOWN]:
        if speed_y <-1:
            speed_y = min(speed_y + acceleration, max_speed)
    else:
        # Diminuindo a velocidade aos poucos se não houver tecla pressionada
        if speed_y < -0.6:
            speed_y += 0.01
  
    rectSpaceship.y += speed_y

    if rectSpaceship.top < 0:
        rectSpaceship.top = 600
    if rectSpaceship.bottom > 600:
        rectSpaceship.bottom = 600

    screen.fill(background_color)
    screen.blit(spaceshipImage, rectSpaceship)
    pygame.display.flip()

    clock.tick(fps)
