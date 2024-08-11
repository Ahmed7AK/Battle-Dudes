import pygame
import random
class Zombie:
    def __init__(self, rect, zombies):
        self.rect = rect
        self.zombies = zombies

    def update(self, screen, player_rect):
        if random.randint(1, 120) == 8:
            self.zombies.append(pygame.Rect(random.randrange(-200, 801, 1000), random.randrange(-200, 801, 1000), self.rect.w, self.rect.h))
        for z in self.zombies:
            if player_rect.x > z.x:
                z.x += 1
            if player_rect.x < z.x:
                z.x -= 1
            if player_rect.y > z.y:
                z.y += 1
            if player_rect.y < z.y:
                z.y -= 1
            pygame.draw.rect(screen, (89, 145, 87), z)
