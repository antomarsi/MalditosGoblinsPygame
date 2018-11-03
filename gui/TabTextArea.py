import pygame
from gui.Button import TextButton
from gui.Colors import Colors
from gui.Panel import Panel

class TabTextArea(object):
    """A fairly straight forward button class."""
    def __init__(self, rect, skills = []):
        self.rect = pygame.Rect(rect)
        self.current_tab = None
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
            button = TextButton((self.rect.x+(110*idx),self.rect.y,110,50), None, text="Level "+str(idx+1), **{'font': pygame.font.Font('font/GoblinOne.otf', 14)})
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
        for tab in self.tabs:
            tab["button"].update(surface)

    def event_loop(self, event):
        for idx, tab in enumerate(self.tabs):
            tab['button'].check_event(event)
            if tab['button'].clicked:
                self.change_text(idx)
