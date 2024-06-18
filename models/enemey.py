import pygame
import random

class Enemy(pygame.sprite.Sprite, ):
    def __init__(self, color, SCREEN_WIDTH, SCREEN_HEIGHT, player, type_zero, follow=False):
        super().__init__()
        self.height = SCREEN_HEIGHT
        self.width = SCREEN_WIDTH
        self.player = player
        self.type_zero = type_zero
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)  # Cor dos inimigos
        self.rect = self.image.get_rect(center=(random.randint(0, self.width), 0))
        self.speed = random.randint(1, 4)
        self.following_player = follow

    def update(self):
        if self.following_player:
            if self.rect.x < self.player.rect.x:
                self.rect.x += self.speed
            elif self.rect.x > self.player.rect.x:
                self.rect.x -= self.speed
            if self.rect.y < self.player.rect.y:
                self.rect.y += self.speed
            elif self.rect.y > self.player.rect.y:
                self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
            if self.rect.y > self.height:
                self.rect.y = 0
                self.rect.x = random.randint(0, self.width)
