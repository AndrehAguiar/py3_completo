import time
import pygame
from Controller.ctrl_game import ControlGame

class Slither:
    def __init__(self):
        self.game_ctrl      = ControlGame()
        self.window         = (300,400)
        self.background     = (0,155,0)
        self.view           = pygame.display.set_mode(self.window)
        self.font           = self.get_font()

    def start(self):
        self.game_ctrl.start()
        while True:
            self.view.fill(self.background)
            self.display_score()
            self.listener()

            if self.game_ctrl.chk_move(self.view):
                level = self.font.render(f'Level UP!:  {self.game_ctrl.level}', True, (255,255,255))
                self.view.blit(level, (80,180))
                pygame.display.flip()
                time.sleep(2)

            self.game_ctrl.draw(self.view)
            self.game_ctrl.up_fps()
            if self.game_ctrl.chk_clash():
                time.sleep(2)
                self.lose()

    def listener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_ctrl.quit()
            if event.type == pygame.KEYDOWN:
                self.game_ctrl.move(event.key)

    def get_font(self):
        pygame.font.init()
        return pygame.font.SysFont('Comic Sans MS', 20)

    def display_score(self):
        scr = self.font.render(f'Score:  {self.game_ctrl.score}', True, (255,255,255))
        self.view.blit(scr,(10,10))

    def lose(self):
        lose = self.font.render(f'You Lose!:  {self.game_ctrl.score}', True, (255,255,255))
        self.view.blit(lose, (80,180))
        pygame.display.flip()
        self.game_ctrl.lose()
