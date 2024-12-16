import pygame
import sys

import config
from Object import Pipeline, PipelineNode

pygame.init()
screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption(config.caption)

pipeline = Pipeline()


def round_to_grid(pos):
    grid_size = 20
    return (
        grid_size * round(pos[0] / grid_size),
        grid_size * round(pos[1] / grid_size),
    )


def game_loop():
    clock = pygame.time.Clock()
    clock.tick(config.FPS)
    while True:
        mouse_pos = pygame.mouse.get_pos()
        rounded_pos = round_to_grid(mouse_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键点击
                    if pipeline.preview_node:
                        pipeline.add_node(pipeline.preview_node)
                        pipeline.preview_node = None

            if event.type == pygame.MOUSEMOTION:
                pipeline.set_preview_node(rounded_pos)

        screen.fill((0, 0, 0))
        pipeline.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    game_loop()
