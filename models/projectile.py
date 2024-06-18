import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, COLOR, TYPE):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 8
        self.TYPE = TYPE

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    
    def who_type(self):
        if(self.TYPE == 1):
            return 1
        else:
            return 0