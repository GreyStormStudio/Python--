import config
from pygame import sprite, Surface, image


class Unit(sprite.Sprite):
    def __init__(self, image_name):
        super().__init__()
        self.image = image.load(image_name)
        self.rect = self.image.get_rect(
            center=(config.screen_width // 2, config.screen_height // 2)
        )

    pass


class Player(Unit):
    def __init__(self, image_name):
        super().__init__(image_name)
        self.health = 100
        self.degree = 0
        self.pos = [0, 0]

    def move(self):
        pass

    pass


class Enemy(Unit):
    def __init__(self, image_name):
        super().__init__(image_name)
        self.health = 100
        self.degree = 0
        self.pos = [0, 0]

    def move(self):
        pass

    pass
