import random

class Food:
    def __init__(self, window=(300,400)):
        self.window = window
        self.devoured = True
        self.position = self.generate_food()

    def generate_food(self):
        if self.devoured:
            self.position = [random.randrange(10,self.window[0], 10),
                            random.randrange(10,self.window[1], 10)]
            self.devoured = False
        return self.position

    def devour(self):
        self.devoured = True
        return self.devoured
