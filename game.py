import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)


pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Colisão')

ball = pygame.Rect(300,230,20,20)

position_player_one = 210
position_player_two = 210

player_one = pygame.Rect(20,position_player_one,20,60)
player_two = pygame.Rect(600,position_player_one,20,60)

pads = [player_one, player_two]

velocity_x = 0.1

clock = pygame.time.Clock()


while True:
    dt = clock.tick(30)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break
    

    ball.move_ip(velocity_x * dt, 0)

    if ball.collidelist(pads) >= 0:
        velocity_x = -velocity_x
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        position_player_one -= 10
    if keys[pygame.K_s]:
        position_player_one += 10
    if keys[pygame.K_i]:
        position_player_two -= 10
    if keys[pygame.K_k]:
        position_player_two += 10

    position_player_one = max(0, min(position_player_one, 420))
    position_player_two = max(0, min(position_player_two, 420))
    
    player_one.y = position_player_one
    player_two.y = position_player_two

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, ball)
    
    for pad in pads:
        pygame.draw.rect(screen, WHITE, pad)
    pygame.display.flip()


pygame.quit()