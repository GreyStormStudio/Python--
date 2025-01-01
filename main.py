import pygame
import sys

import config

pygame.init()
screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption(config.caption)


def mainloop():
    clock = pygame.time.Clock()

    # 游戏主循环
    while True:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    mainloop()
