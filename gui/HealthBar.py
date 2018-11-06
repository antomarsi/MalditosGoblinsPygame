import pygame
from gui.SpriteLoader import SpriteLoader
from gui.Text import drawText

SPRITES_BAR = {
    'bg_l': 'barBack_horizontalLeft',
    'bg_m': 'barBack_horizontalMid',
    'bg_r': 'barBack_horizontalRight',
    'bar_l': 'barRed_horizontalLeft',
    'bar_m': 'barRed_horizontalMid',
    'bar_r': 'barRed_horizontalRight',
}

class HealthBar(object):
    def __init__(self, rect, max_value, **kwargs):
        self.rect = pygame.Rect(rect)
        self.max_value = max_value
        self.value = max_value
        self.bar_back = None
        self.process_kwargs(kwargs)
        self.render_bar(self.sprite_front, self.sprite_back)
        if self.show_text:
            self.render_text()

    def render_text(self):
        self.text = drawText(surface=None, text=self.text_format % (self.value, self.max_value), color=self.font_color, rect=self.rect, font=self.font, aa=self.aa, drop_shadow=(-1,1))

    def render_bar(self, sprite, sprite_back = None):
        spritesheet = SpriteLoader.instance()
        middle_bar_back = None
        if sprite_back:
            left_bar_back = spritesheet.get_image(sprite_back[0])
            right_bar_back = spritesheet.get_image(sprite_back[2])

            if self.rect.width < left_bar_back.get_width() + right_bar_back.get_width():
                self.rect.width = left_bar_back.get_width() + right_bar_back.get_width()
            elif self.rect.width > left_bar_back.get_width() + right_bar_back.get_width():
                middle_bar_back = spritesheet.get_image(sprite_back[1])

            if self.rect.height < left_bar_back.get_height():
                self.rect.height = left_bar_back.get_height()
            back_bar = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
            back_bar.blit(left_bar_back, (0, 0))
            back_bar.blit(right_bar_back, (self.rect.width - right_bar_back.get_width(), 0))

            if middle_bar_back:
                middle_bar_back = pygame.transform.scale(middle_bar_back, (self.rect.width - (left_bar_back.get_width() + right_bar_back.get_width()), middle_bar_back.get_height()))
                back_bar.blit(middle_bar_back, (left_bar_back.get_width(), 0))
            self.bar_back = back_bar

        left_bar = spritesheet.get_image(sprite[0])
        right_bar = spritesheet.get_image(sprite[2])

        if self.rect.width < left_bar.get_width() + right_bar.get_width():
            self.rect.width = left_bar.get_width() + right_bar.get_width()
        elif middle_bar_back is not None or self.rect.width > left_bar.get_width() + right_bar.get_width():
            middle_bar = spritesheet.get_image(sprite[1])
        if self.rect.height < left_bar.get_height():
            self.rect.height = left_bar.get_height()
        bar = pygame.Surface((self.rect.width, left_bar.get_height()), pygame.SRCALPHA, 32)
        if middle_bar_back is not None:
            middle_bar = pygame.transform.scale(middle_bar, (middle_bar_back.get_width(), middle_bar.get_height()))
            bar.blit(middle_bar, (left_bar_back.get_width(), 0))
        elif middle_bar:
            middle_bar = pygame.transform.scale(middle_bar, (self.rect.width - (left_bar.get_width() + right_bar.get_width()), middle_bar.get_height()))
            bar.blit(middle_bar, (left_bar.get_width(), 0))
        if self.bar_back is not None:
            bar.blit(left_bar, (left_bar_back.get_width()-left_bar.get_width(), 0))
            bar.blit(right_bar, (self.rect.width - right_bar_back.get_width() - right_bar.get_width(), 0))
        else:
            bar.blit(left_bar, (0, 0))
            bar.blit(right_bar, (self.rect.width - right_bar.get_width(), 0))
        self.bar = bar


    def set_value(self, value):
        self.value = max(0, min(value, self.max_value))
        if self.show_text:
            self.render_text()

    def update(self, surface):
        bar_rect = self.bar.get_rect(center=self.rect.center)
        if self.bar_back:
            back_bar_rect = self.bar_back.get_rect(center=self.rect.center)
            bar_rect = self.bar.get_rect(center=back_bar_rect.center)
            surface.blit(self.bar_back, back_bar_rect)
        if self.value == self.max_value:
            surface.blit(self.bar, bar_rect)
        else:
            rect_size = ((int)(self.rect.width * (self.value / self.max_value)) , self.bar.get_height())
            surface.blit(self.bar.subsurface((self.bar.get_offset(), rect_size)), bar_rect)
        if self.show_text and self.text:
            text_rect = self.text.get_rect(center=bar_rect.center)
            surface.blit(self.text, text_rect)

    def process_kwargs(self,kwargs):
        settings = {"text_format" : '%d/%d',
                    "show_text": True,
                    "font" : pygame.font.Font(None,16),
                    "font_color" : pygame.Color('white'),
                    "sprite_front": ("bar_left", "bar_middle", "bar_right"),
                    "sprite_back": None,
                    "sprite_back": ("bar_blue_left", "bar_blue_middle", "bar_blue_right"),
                    "sprite_back": ("back_bar_left","back_bar_middle","back_bar_right"),
                    "call_on_release" : True,
                    "click_sound" : None,
                    "hover_sound" : None,
                    "disabled": False,
                    "aa": True
                    }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)