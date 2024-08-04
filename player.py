import pygame
class Player:
    def __init__(self, rect):
        self.color = (245, 207, 17)
        self.rect = rect
        self.speed = 5

    def update(self, screen):
        self.movement()
        pygame.draw.circle(screen, self.color, (self.rect.x+25, self.rect.y+25), self.rect.h/2)

    def movement(self):
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_w]:
            self.rect.y -= self.speed
        if key_press[pygame.K_a]:
            self.rect.x -= self.speed
        if key_press[pygame.K_s]:
            self.rect.y += self.speed
        if key_press[pygame.K_d]:
            self.rect.x += self.speed