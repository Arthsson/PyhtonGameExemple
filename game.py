import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Nave")

# Cores
branco = (255, 255, 255)

# Nave
nave_img = pygame.image.load("nave.png")
nave = pygame.Rect(largura // 2, altura - 64, 64, 64)

# Asteróides
asteroides = []
SPAWN_ASTEROID_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ASTEROID_EVENT, 1000)

# Loop principal do jogo
rodando = True
clock = pygame.time.Clock()
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == SPAWN_ASTEROID_EVENT:
            tamanho = random.randint(20, 50)
            asteroides.append(pygame.Rect(random.randint(0, largura - tamanho), 0, tamanho, tamanho))

    # Lógica do jogo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and nave.left > 0:
        nave.x -= 5
    if teclas[pygame.K_RIGHT] and nave.right < largura:
        nave.x += 5

    # Movimento dos asteróides
    for asteroide in asteroides:
        asteroide.y += 3
        if asteroide.colliderect(nave):
            asteroides.remove(asteroide)

    # Renderização
    tela.fill(branco)
    tela.blit(nave_img, nave)
    for asteroide in asteroides:
        pygame.draw.rect(tela, (255, 0, 0), asteroide)
    pygame.display.update()

    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
