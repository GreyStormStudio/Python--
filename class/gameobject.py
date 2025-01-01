import pygame


class GameObject:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)

    def show(self, screen):
        rect = self.image.get_rect()
        rect.center = self.x, self.y
        screen.blit(self.image, rect)