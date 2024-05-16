import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_position = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
player_size = 20

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_position, player_size)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_position.y -= 5
    if keys[pygame.K_s]:
        player_position.y += 5
    if keys[pygame.K_a]:
        player_position.x -= 5
    if keys[pygame.K_d]:
        player_position.x += 5

    if player_position.x < 0 + player_size:
        player_position.x = 0 + player_size
    elif player_position.x > screen.get_width() - player_size:
        player_position.x = screen.get_width() - player_size
    if player_position.y < 0 + player_size:
        player_position.y = 0 + player_size
    elif player_position.y > screen.get_height() - player_size:
        player_position.y = screen.get_height() - player_size

    pygame.display.flip()
    clock.tick(60) / 1000

pygame.quit()