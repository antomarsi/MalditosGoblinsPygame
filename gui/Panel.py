import pygame
from gui.SpriteLoader import SpriteLoader

class Panel(object):
    def __init__(self, rect, frame_name = "frame" ):
        self.rect = pygame.Rect(rect)
        self.position = (self.rect.x, self.rect.y)

        loader = SpriteLoader.instance()
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
        top_left = loader.get_image(frame_name+'_top_left')
        top_right = loader.get_image(frame_name+'_top_right')
        bottom_left = loader.get_image(frame_name+'_bottom_left')
        bottom_right = loader.get_image(frame_name+'_bottom_right')
        if self.rect.width < (top_left.get_width() + top_right.get_width()):
            self.rect.width = (top_left.get_width() + top_right.get_width())
        if self.rect.height < (top_left.get_height() + bottom_left.get_height()):
            self.rect.width = (top_left.get_height() + bottom_left.get_height())

        self.image.blit(top_left, (0, 0))
        self.image.blit(top_right, (self.rect.width - top_left.get_width(), 0))
        self.image.blit(bottom_left, (0, self.rect.height - bottom_left.get_height()))
        self.image.blit(bottom_right, (self.rect.width - top_left.get_width(), self.rect.height - bottom_right.get_height()))

        if self.rect.width > top_left.get_width() + bottom_left.get_width():
            top_middle = loader.get_image(frame_name+'_top_middle')
            bottom_middle = loader.get_image(frame_name+'_bottom_middle')
            self.image.blit(pygame.transform.scale(top_middle, (self.rect.width - (top_left.get_width() + top_right.get_width()), top_middle.get_height())), (top_left.get_width(), 0))
            self.image.blit(pygame.transform.scale(bottom_middle, (self.rect.width - (top_left.get_width() + top_right.get_width()), bottom_middle.get_height())), (top_left.get_width(), self.rect.height - bottom_middle.get_height()))
            del top_middle
            del bottom_middle
        if self.rect.height > (top_left.get_height() + bottom_left.get_height()):
            middle_left = loader.get_image(frame_name+'_middle_left')
            middle_right = loader.get_image(frame_name+'_middle_right')
            self.image.blit(pygame.transform.scale(middle_left, (middle_left.get_width(), self.rect.height - (top_left.get_height() + bottom_left.get_height()))), (0, 32) )
            self.image.blit(pygame.transform.scale(middle_right, (middle_right.get_width(), self.rect.height - (top_left.get_height() + bottom_left.get_height()))), (self.rect.width - top_left.get_width(), 32))
            del middle_left
            del middle_right
        if self.rect.height > (top_left.get_height() + bottom_left.get_height()) and self.rect.width > (top_left.get_width() + top_right.get_width()):
            middle = loader.get_image(frame_name+'_middle_middle')
            self.image.blit(pygame.transform.scale(middle, (self.rect.width - (top_left.get_width() + top_right.get_width()), self.rect.height - (top_left.get_height() + bottom_left.get_height()))), (top_left.get_width(), top_left.get_height()))
            del middle
        del top_right
        del top_left
        del bottom_left
        del bottom_right

    def update(self, surface):
        surface.blit(self.image, self.rect)
        pass