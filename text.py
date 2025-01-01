import pygame
import sys
from creep.creep import Creep
from explainer.Interpreter import Interpreter
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Code Interpreter Game")

creep = Creep(WIDTH // 2, HEIGHT // 2,"creep.png",screen)
all_sprites = pygame.sprite.Group(creep)


# 示例代码
code = """move TOP_RIGHT
move RIGHT
move BOTTOM
move TOP
move LEFT
move BOTTOM_LEFT
goto 4
"""

interpreter = Interpreter(code)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    interpreter.execute_next_command(creep)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()
    pygame.time.Clock().tick(5)

pygame.quit()
sys.exit()
