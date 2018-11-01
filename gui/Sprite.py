import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = image_file
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location