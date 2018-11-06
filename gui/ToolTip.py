import pygame
from gui.Button import TextButton
from gui.Colors import Colors
from gui.Panel import Panel
from gui.Text import drawText

class ToolTip(object):
    def __init__(self, text, rect, font, max_width=100, font_color=pygame.Color('white'), aa=1):
        self.rect = pygame.Rect(rect)
        self.disabled = False
        self.hovered = False
        self.text = drawText(surface=None, text=text, color=font_color, rect=((0,0), (max_width, self.rect.height)), font=font, aa=aa, wrap=True, overflow=True)
        panel_size = (self.text.get_width()+10, self.text.get_height()+10)
        self.panel = Panel(((0, 0), panel_size))

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered and not self.disabled:
                self.hovered = True
        else:
            self.hovered = False

    def update(self, surface):
        if self.hovered and not self.disabled:
            panel_rect = self.panel.image.get_rect(bottomleft=pygame.mouse.get_pos())
            surface.blit(self.panel.image, panel_rect)
            text_rect = self.text.get_rect(center=panel_rect.center)
            surface.blit(self.text, text_rect)
        pygame.draw.rect(surface, pygame.Color('red'), self.rect, 2)
