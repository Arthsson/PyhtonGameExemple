import pygame


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type, SCREEN_HEIGHT):
        super().__init__()
        self.screen_height = SCREEN_HEIGHT
        self.item_type = item_type
        if item_type == 'follow':
            self.image = pygame.Surface((10, 10))
            self.image.fill((255, 0, 255))
        elif item_type == 'pulse':
            self.image = pygame.Surface((10, 10))
            self.image.fill((255, 255, 0))
        elif item_type == 'not':
            self.image = pygame.Surface((10, 10))
            self.image.fill((50, 50, 50))
        elif item_type == 'normal':
            self.image = pygame.Surface((10, 10))
            self.image.fill((0, 255, 0))
        elif item_type == 'and':
            self.image = pygame.Surface((10, 10))
            self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += 2
        if self.rect.y > self.screen_height:
            self.kill()
