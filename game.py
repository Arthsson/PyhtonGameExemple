import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circuit Puzzle")

# Cores
white = (255, 255, 255)
yellow = (255, 255, 0)

# Componentes
switch_width, switch_height = 50, 20
led_width, led_height = 50, 50
switch_x, switch_y = 375, 300
led_x, led_y = 375, 150

# Estados iniciais
is_switch_on = False
is_led_on = False

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Verificar se o botão foi pressionado
            if switch_x < mouse_x < switch_x + switch_width and switch_y < mouse_y < switch_y + switch_height:
                is_switch_on = not is_switch_on
                is_led_on = is_switch_on

    # Lógica do jogo
    screen.fill(white)
    pygame.draw.rect(screen, white, (switch_x, switch_y, switch_width, switch_height))
    pygame.draw.rect(screen, yellow if is_led_on else white, (led_x, led_y, led_width, led_height))

    # Atualização da tela
    pygame.display.flip()

    # Controle de frames por segundo (FPS)
    pygame.time.Clock().tick(30)
