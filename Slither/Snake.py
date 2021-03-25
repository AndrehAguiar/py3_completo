
class Snake:
    def __init__(self, window=(300,400),
                        position=[100,50],
                        body=[[80,50],[70,50],[60,50]],
                        direction='RIGHT'):
        self.window = window
        self.position = position
        self.body = body
        self.direction = direction
