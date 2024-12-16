import pygame
import sys

import config
from Object import Pipeline

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


def snap_to_direction(start_pos, end_pos):
    x_diff = end_pos[0] - start_pos[0]
    y_diff = end_pos[1] - start_pos[1]
    abs_x_diff = abs(x_diff)
    abs_y_diff = abs(y_diff)

    if abs_x_diff > abs_y_diff:
        # Horizontal movement
        new_pos = (end_pos[0], start_pos[1])
    else:
        # Vertical movement
        new_pos = (start_pos[0], end_pos[1])

    return new_pos


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
                        if pipeline.nodes:  # Check if there are already nodes
                            last_node_pos = pipeline.nodes[-1].pos
                            rounded_pos = snap_to_direction(last_node_pos, rounded_pos)
                        pipeline.add_node(pipeline.preview_node)
                        pipeline.preview_node = None

            if event.type == pygame.MOUSEMOTION:
                pipeline.set_preview_node(rounded_pos)

        screen.fill((0, 0, 0))
        pipeline.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    game_loop()
