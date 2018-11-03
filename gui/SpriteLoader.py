import pygame, json

class SpriteLoader(object):
    __instance = None

    @staticmethod
    def instance():
        if not SpriteLoader.__instance:
            SpriteLoader.__instance = SpriteLoader()
        return SpriteLoader.__instance

    def load(self, filename, json_file):
        self.__images = {}
        json_decoded = json.load(open(json_file))
        sheet = pygame.image.load(filename).convert_alpha()
        for sprite in json_decoded['sprites']:
            rect = pygame.Rect(((sprite['x'], sprite['y']), (sprite['width'], sprite['height'])))
            image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
            image.blit(sheet, (0, 0), rect)
            self.__images[sprite['name']] = image

    def get_image(self, name):
        return self.__images[name]
