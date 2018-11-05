import pygame
from gui.Button import TextButton
from gui.Colors import Colors
from gui.Panel import Panel
from gui.Text import drawText

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

    def update(self, surface):
        self.panel.update(surface)
        if self.current_tab:
            drawText(surface, text=self.current_tab['skill']['name'], color=pygame.Color('white'), rect=(self.rect.left + 10, self.rect.y+self.tabs[0]['button'].rect.height + 10, self.rect.width - 20, self.rect.height - self.tabs[0]['button'].rect.height), font=self.font_button, aa=1, drop_shadow=(-1,1))
            title = self.font_button.render(self.current_tab['skill']['name'], 0, pygame.Color('white'), None)
            drawText(surface, text=self.current_tab['skill']['description'], color=pygame.Color('white'),  rect=(self.rect.left + 10, self.rect.y+self.tabs[0]['button'].rect.height + 10 + title.get_rect().height, self.rect.width - 20, self.rect.height - self.tabs[0]['button'].rect.height), font=self.font_text, aa=1, drop_shadow=(-1,1), wrap=True)
        for tab in self.tabs:
            tab["button"].update(surface)

    def event_loop(self, event):
        for idx, tab in enumerate(self.tabs):
            tab['button'].check_event(event)
            if tab['button'].clicked:
                self.change_text(idx)
