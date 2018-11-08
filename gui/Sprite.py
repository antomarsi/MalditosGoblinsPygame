import pygame
from gui.SpriteLoader import SpriteLoader

class Sprite(object):
    def __init__(self, position, sprite):
        spritesheet = SpriteLoader.instance()
        self.image = spritesheet.get_image(sprite)
        self.rect = pygame.Rect((position, self.image.get_size()))

    def update(self, surface):
        surface.blit(self.image, self.rect)