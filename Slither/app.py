import pygame
import sys
from Snake import Snake
from Food import Food

pygame.init()

VIEW_SIZE = (300,400)
view = pygame.display.set_mode(VIEW_SIZE)

snake = Snake()
food = Food()
position_food = food.position

while True:
    view.fill((0,155,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Interrompe o pygame
            pygame.quit()
            # Fecha a janela
            sys.exit()

    for pos in snake.body:
        pygame.draw.rect(view, pygame.Color(220,220,50),
                                # Left, Top, width, height
                                pygame.Rect(pos[0],pos[1], 10, 10))

    pygame.draw.rect(view, pygame.Color(204, 51, 0),
                            pygame.Rect(position_food[0], position_food[1], 10,10))

    # Atualiza a tela a cada frame
    pygame.display.update()
