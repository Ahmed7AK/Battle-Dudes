import pygame
import math
class Player:
    def __init__(self, rect):
        self.color = (245, 207, 17)
        self.rect = rect
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load("line.png"), (128, 72))
        self.image_pos = (236, 264)

    def update(self, screen):
        self.movement()
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - self.image_pos[0]
        dy = mouse_pos[1] - self.image_pos[1]
        angle = math.degrees(math.atan2(-dy, dx))
        rotated_image = pygame.transform.rotate(self.image, angle)
        rotated_rect = rotated_image.get_rect(center=(self.rect.x+25, self.rect.y+25))
        screen.blit(rotated_image, rotated_rect.topleft)
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