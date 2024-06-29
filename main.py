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
rectSpaceship.center = (400, 300)

# Velocidade da nave e parâmetros de aceleração
spaceshipSpeed = 0
spaceshipAcceleration = 0.1
spaceshipMaxSpeed = 5

# Loop principal
while True:
    # Checar se o usuário fechou o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Capturar as teclas pressionadas
    teclas = pygame.key.get_pressed()
    
    # Movimentar a nave com aceleração
    if teclas[pygame.K_LEFT]:
        spaceshipSpeed = max(spaceshipSpeed - spaceshipAcceleration, -spaceshipMaxSpeed)
        rectSpaceship.x += spaceshipSpeed
    elif teclas[pygame.K_RIGHT]:
        spaceshipSpeed = min(spaceshipSpeed + spaceshipAcceleration, spaceshipMaxSpeed)
        rectSpaceship.x += spaceshipSpeed
    elif teclas[pygame.K_UP]:
        spaceshipSpeed = max(spaceshipSpeed - spaceshipAcceleration, -spaceshipMaxSpeed)
        rectSpaceship.y += spaceshipSpeed
    elif teclas[pygame.K_DOWN]:
        spaceshipSpeed = min(spaceshipSpeed + spaceshipAcceleration, spaceshipMaxSpeed)
        rectSpaceship.y += spaceshipSpeed
    else:
        spaceshipSpeed = 0  # Zerar a velocidade se nenhuma tecla for pressionada

    # Garantir que a nave permaneça dentro dos limites da tela
    if rectSpaceship.left < 0:
        rectSpaceship.left = 0
    if rectSpaceship.right > 800:
        rectSpaceship.right = 800
    if rectSpaceship.top < 0:
        rectSpaceship.top = 0
    if rectSpaceship.bottom > 600:
        rectSpaceship.bottom = 600

    # Pintar a tela de fundo
    screen.fill(background_color)
    
    # Desenhar a nave na posição atual
    screen.blit(spaceshipImage, rectSpaceship)

    pygame.display.flip()