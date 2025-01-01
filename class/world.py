import pygame

class World:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.objects = []

    def display(self):
        self.screen.fill((0, 0, 0))
        for obj in self.objects:
            obj.draw(self.screen)
        pygame.display.flip()

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def update(self):
        for obj in self.objects:
            obj.show()
