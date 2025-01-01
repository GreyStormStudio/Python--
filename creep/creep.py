import pygame
from constant import directionConstant


class Creep(pygame.sprite.Sprite):
    def __init__(self, x, y, image, screen):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        screen.blit(self.image, self.rect)
        self.x = x
        self.y = y
        self.speed = 32
        self.store = 0
        self.storeCapacity = 128

    def move(self, direction):
        if direction not in directionConstant:
            return -1
        if direction == "TOP_LEFT":
            self.rect.center+=-self.speed, -self.speed
        elif direction == "TOP":
            self.rect.move_ip(0, -self.speed)
        elif direction == "TOP_RIGHT":
            self.rect.move_ip(self.speed, -self.speed)
        elif direction == "LEFT":
            self.rect.move_ip(-self.speed, 0)
        elif direction == "RIGHT":
            self.rect.move_ip(self.speed, 0)
        elif direction == "BOTTOM_LEFT":
            self.rect.move_ip(-self.speed, self.speed)
        elif direction == "BOTTOM":
            self.rect.move_ip(0, self.speed)
        elif direction == "BOTTOM_RIGHT":
            self.rect.move_ip(self.speed, self.speed)
        return 0

    def harvest(self, source):
        if abs(self.rect.x - source.rect.x) <= 32 and abs(self.rect.y - source.rect.y) <= 32:
            if self.store < self.storeCapacity and source.store > 0:
                self.store += 1
                source.store -= 1
        pass
