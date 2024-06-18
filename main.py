import pygame
import sys
import random

from configs.consts import Const
from models.player import Player
from models.projectile import Projectile
from models.enemey import Enemy
from models.item import Item    

pygame.init()

screen = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
pygame.display.set_caption("Atirar Projetéis")

def draw_text(surface, text, pos, color, font_size=30):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()

player = Player(Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT, Const.RED)
all_sprites.add(player)

clock = pygame.time.Clock()
running = True
inverted_controls = False

def verify_type():
    if(type=='and'):
        return 1

while running:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not inverted_controls:
                if event.key == pygame.K_KP_0:
                    projectile = Projectile(player.rect.centerx, player.rect.centery, Const.WHITE, 0)
                    all_sprites.add(projectile)
                    projectiles.add(projectile)
                elif event.key == pygame.K_KP_1:
                    projectile = Projectile(player.rect.centerx, player.rect.centery, Const.RED, 1)
                    all_sprites.add(projectile)
                    projectiles.add(projectile)
            else:
                if event.key == pygame.K_KP_0:
                    projectile = Projectile(player.rect.centerx, player.rect.centery, Const.RED, 1)
                    all_sprites.add(projectile)
                    projectiles.add(projectile)
                elif event.key == pygame.K_KP_1:
                    projectile = Projectile(player.rect.centerx, player.rect.centery, Const.WHITE, 0)
                    all_sprites.add(projectile)
                    projectiles.add(projectile)

    if random.randint(0, 100) < 1:
        type = random.choice([True, False])
        if type:
            color = Const.WHITE
        else:
            color = Const.RED
        enemy = Enemy(color, Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT, player, type, False)
        all_sprites.add(enemy)
        enemies.add(enemy)
    


    hits = pygame.sprite.groupcollide(enemies, projectiles, False, True)
    for enemy in hits:
        for projectile in hits[enemy]:
            if projectile.who_type() == 0 and enemy.type_zero:
                enemy.kill()
                if random.random() < 0.5:  # 50% de chance de soltar um item
                    item = Item(enemy.rect.x, enemy.rect.y, random.choice(['follow', 'not', 'normal', 'pulse', 'and']), Const.SCREEN_HEIGHT)
                    all_sprites.add(item)
                    items.add(item)
            elif projectile.who_type() == 1 and not enemy.type_zero:
                enemy.kill()
                if random.random() < 0.5:  # 50% de chance de soltar um item
                    item = Item(enemy.rect.x, enemy.rect.y, random.choice(['follow', 'not', 'normal', 'pulse', 'and']), Const.SCREEN_HEIGHT)
                    all_sprites.add(item)
                    items.add(item)
                    
    item_hits = pygame.sprite.spritecollide(player, items, True)
    for item in item_hits:
        if item.item_type == 'follow':
            for enemy in enemies:
                enemy.following_player = True
        elif item.item_type == 'pulse':
            for enemy in enemies:
                enemy.kill()
        elif item.item_type == 'not':
            inverted_controls = True
        elif item.item_type == 'normal':
            inverted_controls = False

    all_sprites.update()

    screen.fill(Const.PURPLE)
    all_sprites.draw(screen)

    draw_text(screen, f"Inimigos restantes: {len(enemies)}", (10, 10), Const.WHITE)
    draw_text(screen, f"Controles invertidos: {'Sim' if inverted_controls else 'Não'}", (10, 50), Const.WHITE)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()