import pygame
import sys
import random

import config

from Object import Tower, Enemy

pygame.init()
screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption(config.caption)


def game_loop():
    clock = pygame.time.Clock()
    tower_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    # 游戏主循环
    while True:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键点击放置塔
                    pos = pygame.mouse.get_pos()
                    tower = Tower(pos)
                    tower_group.add(tower)

        # 更新敌人
        if random.randint(1, 50) == 1:  # 随机生成敌人
            enemy = Enemy()
            enemy_group.add(enemy)

        # 更新塔和敌人
        tower_group.update()
        enemy_group.update()

        # 绘制
        screen.fill((0, 0, 0))
        tower_group.draw(screen)
        enemy_group.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    game_loop()
