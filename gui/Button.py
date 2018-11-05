import pygame
from gui.SpriteLoader import SpriteLoader
from gui.Text import drawText

class TextButton(object):
    """A fairly straight forward button class."""
    def __init__(self, rect, function, **kwargs):
        self.rect = pygame.Rect(rect)
        self.function = function
        self.clicked = False
        self.hovered = False
        self.active = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        if self.text:
            self.text = drawText(surface=None, text=self.text, color=self.font_color, rect=self.rect, font=self.font, aa=self.aa, drop_shadow=(-1,1), center=True)
        self.render_button()

    def render_button(self):
        self.button = self.get_image_button(self.sprite, True)
        if self.sprite_hover:
            self.button_hover = self.get_image_button(self.sprite_hover)
        if self.sprite_clicked:
            self.button_clicked = self.get_image_button(self.sprite_clicked)

    def get_image_button(self, sprite, set_new_width = False):
        spritesheet = SpriteLoader.instance()
        button = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
        left = spritesheet.get_image(sprite[0])
        right = spritesheet.get_image(sprite[2])
        if set_new_width:
            if self.rect.width < (left.get_width() + right.get_width()):
                self.rect.width = (left.get_width() + right.get_width())
            self.rect.height = left.get_height()
        button.blit(left, (0, 0))
        button.blit(right, (self.rect.width-right.get_width(), 0))
        if (self.rect.width > (left.get_width() + right.get_width())):
            middle = spritesheet.get_image(sprite[1])
            button.blit(pygame.transform.scale(middle, (self.rect.width - (left.get_width() + right.get_width()), middle.get_height())), (left.get_width(), 0) )
        return button

    def process_kwargs(self,kwargs):
        settings = {"text" : None,
                    "font" : pygame.font.Font(None,16),
                    "font_color" : pygame.Color('white'),
                    "sprite": ("button_left","button_middle","button_right"),
                    "sprite_hover": ("button_left_hover","button_middle_hover","button_right_hover"),
                    "sprite_clicked": ("button_left_clicked","button_middle_clicked","button_right_clicked"),
                    "call_on_release" : True,
                    "click_sound" : None,
                    "hover_sound" : None,
                    "aa": True
                    }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def check_event(self, event):
        """The button needs to be passed events from your program event loop."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self,event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release and self.function is not None:
                self.function()

    def on_release(self,event):
        if self.clicked and self.call_on_release and self.function is not None:
            self.function()
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False

    def update(self, surface):
        button = self.button
        text = self.text
        self.check_hover()
        if (self.clicked or self.active) and self.button_clicked:
            button = self.button_clicked
        elif self.hovered and self.button_hover:
            button = self.button_hover
        surface.blit(button, self.rect)
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)

class SpriteButton(TextButton):
    def __init__(self, rect, function, **kwargs):
        self.rect = pygame.Rect(rect)
        self.function = function
        self.clicked = False
        self.hovered = False
        self.icon = None
        self.button = None
        self.active = False
        self.button_clicked = None
        self.button_hover
        self.process_kwargs(kwargs)
        self.render_button()

    def process_kwargs(self,kwargs):
        settings = {"left_sprite" : None,
                    "middle_sprite" : None,
                    "right_sprite" : None,
                    "left_sprite_hover" : None,
                    "middle_sprite_hover" : None,
                    "right_sprite_hover" : None,
                    "left_sprite_clicked" : None,
                    "middle_sprite_clicked" : None,
                    "right_sprite_clicked" : None,
                    "icon": None,
                    "button_sprite": ("button_left","button_middle","button_right"),
                    "call_on_release" : True,
                    "click_sound" : None,
                    "hover_sound" : None}
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def render_button(self):
        self.button = self.get_image_button()
        self.button_hover = self.get_image_button("_hover")
        self.button_clicked = self.get_image_button("_clicked")

    def get_image_button(self, postfix = ""):
        spritesheet = SpriteLoader.instance()
        button = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
        left = spritesheet.get_image(self.button_sprite[0]+postfix)
        right = spritesheet.get_image(self.button_sprite[2]+postfix)
        button.blit(left, (0, 0))
        button.blit(right, (self.rect.width-41, 0))
        if (self.rect.width > 82):
            middle = spritesheet.get_image(self.button_sprite[1]+postfix)
            button.blit(pygame.transform.scale(middle, (self.rect.width - 82, 28)), (41, 0) )
        return button

    def update(self, surface):
        button = self.button
        icon = self.icon
        self.check_hover()
        if (self.clicked and self.button_clicked) or self.active:
            button = self.button_clicked
        elif self.hovered and self.button_hover:
            button = self.button_hover
        surface.blit(button, self.rect)
        if self.icon:
            icon_rect = icon.get_rect(center=self.rect.center)
            surface.blit(text, icon_rect)
