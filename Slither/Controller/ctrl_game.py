from Model.Game import Game
from Controller.ctrl_snake import ControlSnake
from Controller.ctrl_food import ControlFood

class ControlGame:
    def __init__(self):
        self.game       = Game()
        self.snake_ctrl = ControlSnake()
        self.food_ctrl  = ControlFood()
        self.score      = self.game.score
        self.speed      = self.game.speed
        self.level      = self.game.level

    def start(self):
        self.game.start()

    def quit(self):
        self.game.quit()

    def up_fps(self):
        self.game.set_fps(self.speed)

    def move(self, way):
        self.snake_ctrl.moviment(way)

    def chk_move(self, view):
        if self.snake_ctrl.chk_moviment(self.food_ctrl.check_food()):
            self.food_ctrl.set_devoured(view)
            self.score += 1

        if self.snake_ctrl.chk_level(self.speed, self.level):
            self.level += 1
            self.speed += 1
            self.up_fps()
            return True


    def chk_clash(self):
        return self.snake_ctrl.clash()

    def draw(self, view):
        self.snake_ctrl.draw(view)
        self.food_ctrl.draw(view)

    def lose(self):
        self.game.lose()
