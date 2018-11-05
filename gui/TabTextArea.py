import pygame
from gui.Button import TextButton
from gui.Colors import Colors
from gui.Panel import Panel

class TabTextArea(object):
    """A fairly straight forward button class."""
    def __init__(self, rect, font_button, font_text, skills = []):
        self.rect = pygame.Rect(rect)
        self.current_tab = None
        self.font_button = font_button
        self.font_text = font_text
        self.process_skills(skills)
        min_width = 0
        for tab in self.tabs:
            min_width += tab["button"].rect.width
        if self.rect.width < min_width:
            self.rect.width = min_width
        self.panel = Panel((self.rect.x, self.rect.y+self.tabs[0]['button'].rect.height, self.rect.width, self.rect.height))

    def process_skills(self, skills):
        self.tabs = []
        for idx, value in enumerate(skills):
            button = TextButton((self.rect.x+(110*idx),self.rect.y,110,50), None, text="Level "+str(idx+1), **{'font': self.font_button})
            tab = {'button': button, 'skill': value}
            self.tabs.append(tab)
        self.change_text(0)

    def change_text(self, index):
        if self.current_tab is not None:
            self.current_tab["button"].active = False
        self.current_tab = self.tabs[index]
        self.current_tab["button"].active = True

    def drawText(self, surface, text, color, rect, font, aa=False, bkg=None):
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2
        # get the height of the font
        fontHeight = font.size("Tg")[1]
        while text:
            i = 1
            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break
            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1
            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1
            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)
            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
            # remove the text we just blitted
            text = text[i:]
        return text
    def update(self, surface):
        self.panel.update(surface)
        if self.current_tab:
            title = self.font_button.render(self.current_tab['skill']['name'], 1, pygame.Color('white'), None)
            surface.blit(title, (self.rect.left+10, self.rect.y+self.tabs[0]['button'].rect.height+10))
            self.drawText(surface, self.current_tab['skill']['description'], pygame.Color('white'), (self.rect.left + 10, self.rect.y+self.tabs[0]['button'].rect.height + 10 + title.get_rect().height, self.rect.width, self.rect.height), self.font_text, 1)
        for tab in self.tabs:
            tab["button"].update(surface)

    def event_loop(self, event):
        for idx, tab in enumerate(self.tabs):
            tab['button'].check_event(event)
            if tab['button'].clicked:
                self.change_text(idx)
