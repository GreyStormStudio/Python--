import pygame

import config

pygame.init()
screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption(config.caption)
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    pygame.display.flip()

    clock.tick(config.FPS)

pygame.quit()
