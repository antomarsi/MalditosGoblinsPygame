import pygame
from gui.SpriteLoader import SpriteLoader
from gui.Text import drawText
from gui.Utils import fastsaturation

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
                    "disabled": False,
                    "aa": True
                    }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def check_event(self, event):
        if self.disabled:
            return
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
        if self.clicked and self.call_on_release and self.function is not None and not self.disabled:
            self.function()
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered and not self.disabled:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False

    def update(self, surface):
        button = self.button
        text = self.text
        self.check_hover()
        if (self.clicked or self.active) and self.button_clicked and not self.disabled:
            button = self.button_clicked
        elif self.hovered and self.button_hover and not self.disabled:
            button = self.button_hover
        if self.disabled:
            fastsaturation(button, 0)
        surface.blit(button, self.rect)
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)

class IconButton(TextButton):
    def __init__(self, rect, function, **kwargs):
        self.rect = pygame.Rect(rect)
        self.function = function
        self.clicked = False
        self.hovered = False
        self.active = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        self.render_icon()
        self.render_button()

    def process_kwargs(self,kwargs):
        settings = {"sprite_icon" : None,
                    "sprite_icon_clicked" : None,
                    "sprite_icon_hover" : None,
                    "sprite": None,
                    "sprite_hover": None,
                    "sprite_clicked": None,
                    "call_on_release" : True,
                    "click_sound" : None,
                    "hover_sound" : None,
                    "disabled": False,
                    "scale": 1
                    }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def render_icon(self):
        if self.sprite_icon:
            self.icon = SpriteLoader.instance().get_image(self.sprite_icon)
            if self.scale != 1:
                self.icon = pygame.transform.scale(self.icon, (self.icon.get_width()*2, self.icon.get_height()*2))
        if self.sprite_icon_clicked:
            self.icon_clicked = SpriteLoader.instance().get_image(self.sprite_icon_clicked)
            if self.scale != 1:
                self.icon_clicked = pygame.transform.scale(self.icon_clicked, (self.icon_clicked.get_width()*2, self.icon_clicked.get_height()*2))
        if self.sprite_icon_hover:
            self.icon_hover = SpriteLoader.instance().get_image(self.sprite_icon_hover)
            if self.scale != 1:
                self.icon_hover = pygame.transform.scale(self.icon_hover, (self.icon_hover.get_width()*2, self.icon_hover.get_height()*2))


    def render_button(self):
        self.button = self.get_image_button(self.sprite, True)
        if self.sprite_hover:
            self.button_hover = self.get_image_button(self.sprite_hover)
        if self.sprite_clicked:
            self.button_clicked = self.get_image_button(self.sprite_clicked)

    def get_image_button(self, sprite, set_new_width = False):
        spritesheet = SpriteLoader.instance()
        if type(sprite) is str:
            button = spritesheet.get_image(sprite)
            if set_new_width:
                self.rect.width = button.get_width()
                self.rect.height = button.get_height()
        else:
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
        if self.scale != 1:
            button = pygame.transform.scale(button, (button.get_width()*self.scale, button.get_height()*self.scale))
            self.rect.width *= self.scale
            self.rect.height *= self.scale
        return button

    def update(self, surface):
        button = self.button
        self.check_hover()
        if (self.clicked or self.active) and self.sprite_clicked:
            button = self.button_clicked
        elif self.hovered and self.sprite_hover:
            button = self.button_hover
        surface.blit(button, self.rect)
        if self.icon:
            icon = self.icon
            if (self.clicked or self.active) and self.sprite_icon_clicked:
                icon = self.icon_clicked
            if (self.hovered or self.active) and self.sprite_icon_hover:
                icon = self.icon_hover
            icon_rect = icon.get_rect(center=self.rect.center)
            surface.blit(icon, icon_rect)
        pygame.draw.rect(surface, pygame.Color('red'), self.rect, 1)
