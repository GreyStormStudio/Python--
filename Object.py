from pygame import sprite, image, draw

# from random import randint

import config


class Unit(sprite.Sprite):
    def __init__(self, image_name):
        super().__init__()
        self.image = image.load(image_name)
        self.rect = self.image.get_rect(
            center=(config.screen_width // 2, config.screen_height // 2)
        )

    pass


class PipelineNode:
    def __init__(self, pos):
        self.pos = pos
        self.radius = 5
        # self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = (0, 255, 0)

    def draw(self, surface):
        draw.circle(surface, self.color, self.pos, self.radius)


class Pipeline:
    def __init__(self):
        self.nodes = []
        self.preview_node = None

    def add_node(self, node):
        self.nodes.append(node)
        self.preview_node = None

    def set_preview_node(self, pos):
        self.preview_node = PipelineNode(pos)

    def draw(self, surface):
        if len(self.nodes) > 1:
            for i in range(len(self.nodes) - 1):
                draw.line(
                    surface,
                    self.nodes[i].color,
                    self.nodes[i].pos,
                    self.nodes[i + 1].pos,
                    self.nodes[i].radius * 2,
                )
        if self.preview_node:
            self.preview_node.draw(surface)
            if len(self.nodes) > 0:
                draw.aaline(
                    surface,
                    (255, 255, 255),
                    self.nodes[-1].pos,
                    self.preview_node.pos,
                    1,
                )  # 虚影线
