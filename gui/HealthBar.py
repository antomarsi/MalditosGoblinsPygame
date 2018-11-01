import pygame
from gui.Spritesheet import Spritesheet

SPRITES_BAR = {
    'bg_l': 'barBack_horizontalLeft',
    'bg_m': 'barBack_horizontalMid',
    'bg_r': 'barBack_horizontalRight',
    'bar_l': 'barRed_horizontalLeft',
    'bar_m': 'barRed_horizontalMid',
    'bar_r': 'barRed_horizontalRight',
}

class HealthBar(object):
    def __init__(self, rect, max_value):
        self.rect = pygame.Rect(rect)
        self.max_value = max_value
        self.value = max_value
        self.spritesheet = Spritesheet.instance()

    def set_value(self, value):
        self.value = max(0, min(value, self.max_value))

    def update(self, surface):
