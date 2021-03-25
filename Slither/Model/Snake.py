class Snake:
    def __init__(self, window=(300,400),
                        position=[100,50],
                        body=[[80,50],[70,50],[60,50]],
                        direction='RIGHT'):
        self.window = window
        self.position = position
        self.body = body
        self.direction = direction

    def change_direction(self, new_direction):
        # Controla a direção do movimento
        # Muda pra direita
        if new_direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        # Muda pra esquerda
        if new_direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        # Muda pra cima
        if new_direction == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        # Muda pra baixo
        if new_direction == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def move(self, food_position):
        # Controla o movimento
        # Move pra direita
        if self.direction == 'RIGHT':
            self.position[0] += 10
        # Move pra esquerda
        if self.direction == 'LEFT':
            self.position[0] -= 10
        # Move pra cima
        if self.direction == 'UP':
            self.position[1] -= 10
        # Move pra baixo
        if self.direction == 'DOWN':
            self.position[1] += 10

        return self.make_body(food_position)

    def make_body(self, food_position):
        # Adiciona cabeça
        self.body.insert(0, list(self.position))
        # Verifica se comeu a comida
        if self.position == food_position:
            return True
        # Remove calda
        self.body.pop()
        return False

    def up_level(self, level):
        self.body = self.body[:level]

    def check_collision(self):
        # Verifica colisão horizontal com as paredes
        if self.position[0] > (self.window[0] - 10) or self.position[0] < 0:
            return True
        # Verifica colisão vertical com as paredes
        if self.position[1] > (self.window[1] - 10) or self.position[1] < 0:
            return True
        # Verifica colisão com o próprio corpo
        for node in self.body[1:]:
            if self.position == node:
                return True
