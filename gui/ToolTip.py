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
        self.text = drawText(surface=None, text=text, color=font_color, drop_shadow=None, rect=((0,0), (max_width, self.rect.height)), font=font, aa=aa, wrap=True, overflow=True)
        panel_size = (self.text.get_width()+20, self.text.get_height()+20)
        self.panel = Panel(((0, 0), panel_size))
        self.panel.image.blit(self.text, (10, 10))

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered and not self.disabled:
                self.hovered = True
        else:
            self.hovered = False

    def update(self, surface):
        pygame.draw.rect(surface, pygame.Color('red'), self.rect, 2)
        if self.hovered and not self.disabled:
            mouse_pos = pygame.mouse.get_pos()
            panel_rect = self.panel.image.get_rect(bottomleft=mouse_pos)
            if mouse_pos[1] - self.panel.image.get_height() < 0:
                panel_rect.y = 0
            elif mouse_pos[0] + self.panel.image.get_width() > surface.get_width():
                panel_rect.x = surface.get_width() - panel_rect.width
            surface.blit(self.panel.image, (panel_rect.x, panel_rect.y))
