from pygame import sprite, image, draw, Surface, transform

# from random import randint

import config


class Tower(sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # self.image = image(config.tower_img)
        self.original_image = Surface((200, 200))
        self.original_image.fill((0, 255, 0))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.range = 100
        self.angle = 0  # 初始角度

    def update(self):
        self.angle = (self.angle + 1) % 360
        self.image = transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


class Enemy(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(0, config.screen_height // 2))
        self.speed = 1

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > config.screen_width:
            self.kill()  # 敌人离开屏幕后销毁
