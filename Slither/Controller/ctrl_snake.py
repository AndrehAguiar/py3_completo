import pygame
from Model.Snake import Snake

class ControlSnake:
    def __init__(self):
        self.snake = Snake()

    def moviment(self, way):
        if way == pygame.K_RIGHT:
            self.snake.change_direction('RIGHT')
        if way == pygame.K_LEFT:
            self.snake.change_direction('LEFT')
        if way == pygame.K_UP:
            self.snake.change_direction('UP')
        if way == pygame.K_DOWN:
            self.snake.change_direction('DOWN')

    def chk_moviment(self, food_position):
        return self.snake.move(food_position)

    def chk_level(self, speed, level):
        flag = len(self.snake.body) == (20 + level)
        if flag:
            self.snake.up_level(speed)
        return flag

    def clash(self):
        return self.snake.check_collision()

    def draw(self, view):
        for pos in self.snake.body:
            pygame.draw.rect(view, pygame.Color(220,220,50),
                                    # Left, Top, width, height
                                    pygame.Rect(pos[0],pos[1], 10, 10))
