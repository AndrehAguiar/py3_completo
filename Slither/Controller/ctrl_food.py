import pygame
from Model.Food import Food

class ControlFood:
    def __init__(self):
        self.food = Food()

    def check_food(self):
        return self.food.generate_food()

    def set_devoured(self, view):
        self.food.devour()

    def draw(self, view):
        pygame.draw.rect(view, pygame.Color(204, 51, 0),
                                pygame.Rect(self.food.position[0], self.food.position[1], 10,10))
