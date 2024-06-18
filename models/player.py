import pygame

""" 
class Player(pygame.sprite.Sprite,):
    def __init__(self,  SCREEN_WIDTH, SCREEN_HEIGHT, COLOR) :
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(COLOR)
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5

        self.rect.x = max(0, min(self.rect.x, self.SCREEN_WIDTH - 20))
        self.rect.y = max(0, min(self.rect.y, self.SCREEN_HEIGHT - 20))
"""

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, color):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, color, [(10, 0), (0, 20), (20, 20)])  # Forma de nave triangular
        self.orig_image = self.image  # Para preservar a imagem original para rotação
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.position = pygame.math.Vector2(self.rect.center)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0  # Ângulo inicial da nave
        self.speed = 0.3  # Velocidade de aceleração da nave
        self.max_speed = 5  # Velocidade máxima da nave
        self.rotation_speed = 3  # Velocidade de rotação em graus por frame

    def update(self):
        keys = pygame.key.get_pressed()

        # Rotação da nave
        if keys[pygame.K_a]:
            self.angle += self.rotation_speed
        if keys[pygame.K_d]:
            self.angle -= self.rotation_speed

        # Aceleração da nave na direção em que está apontando
        if keys[pygame.K_w]:
            direction = pygame.math.Vector2(0, -self.speed).rotate(self.angle)
            self.velocity += direction

        # Limite de velocidade
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        # Atualização da posição com base na velocidade
        self.position += self.velocity
        self.rect.center = self.position

        # Desaceleração gradual (simulação de atrito)
        self.velocity *= 0.98  # Reduz a velocidade em 2% a cada frame

        # Limitação para permanecer na tela
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity.x = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
            self.velocity.x = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.velocity.y = 0

        # Atualiza a posição da imagem da nave conforme o ângulo
        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)