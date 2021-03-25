import random

class Food:
    def __init__(self, window=(300,400)):
        self.window = window
        self.position = [random.randrange(10,self.window[0], 10),
                        random.randrange(10,self.window[1], 10)]

        self.devoured = False
