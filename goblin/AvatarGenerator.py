import pygame
from gui.Utils import get_random_color, color_variant

class AvatarGenerator(object):
    #color indexes:
    # 0 Black line
    # 1 dark shoe
    # 2 dark armor
    # 3 ALPHA MAGENTA
    # 4 light armor
    # 5 light shoe
    # 6 dark skin
    # 7 light skin

    def __init__(self, rect, goblin):
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
        sprite = pygame.image.load('sprites/goblin.bmp')
        sprite = pygame.transform.scale(sprite, (168, 168))
        sprite.set_colorkey((255, 0, 255))

        # randomize armor color
        self.randomize_color(sprite, 4, 2)
        # randomize shoe color
        self.randomize_color(sprite, 1, 6)

        rect_center = sprite.get_rect(center=self.image.get_rect().center)
        self.image.blit(sprite, rect_center)

    def randomize_color(self, sprite, index, shadow_index = None):
        color = get_random_color()
        sprite.set_palette_at(index, color)
        if shadow_index:
            sprite.set_palette_at(shadow_index, color_variant(color, -40))


    def update(self, surface):
        surface.blit(self.image, self.rect)

