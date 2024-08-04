import pygame
from player import Player
class Game:
    def __init__(self):
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode((600, 600))
        self.rect = self.pygame.Rect(275, 275, 50, 50)
        self.clock = self.pygame.time.Clock()

        self.BG = (54, 107, 27)

        self.loop()


    def loop(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            for self.event in self.pygame.event.get():
                if self.event.type == self.pygame.QUIT:
                    self.running = False
            self.draw()

    def draw(self):
        self.screen.fill(self.BG)
        Player(self.rect).update(self.screen)
        self.pygame.display.update()

game = Game()
