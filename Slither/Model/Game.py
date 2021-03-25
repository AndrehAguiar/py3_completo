import pygame
import sys

class Game:
    def __init__(self):
        self.fps = pygame.time.Clock()
        self.score = 0
        self.level = 1
        self.speed = 5

    def start(self):
        pygame.init()

    def set_fps(self, speed):
        self.speed = speed
        # Atualiza a tela a cada frame
        pygame.display.update()
        self.fps.tick(self.speed)

    def lose(self):
        self.quit()

    def quit(self):
        pygame.quit()
        sys.exit()
