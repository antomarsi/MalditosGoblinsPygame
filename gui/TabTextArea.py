import pygame as pg
from gui.Button import Button
from gui.Colors import Colors

BUTTON_STYLE = {"hover_color" : Colors.BLUE,
                "clicked_color" : Colors.GREEN,
                "clicked_font_color" : Colors.BLACK,
                "hover_font_color" : Colors.ORANGE}

class TabTextArea(object):
    """A fairly straight forward button class."""
    def __init__(self, rect, **kwargs):
        self.rect = pg.Rect(rect)
        self.tabs = {}
        self.process_kwargs(kwargs)
        self.current_text = None

    def process_kwargs(self,kwargs):
        for key in kwargs:
            button = Button((0,0,200,50), Colors.RED, self.change_text(key), key, **BUTTON_STYLE)
            self.tabs[key] = {
                'button': button,
                'text': kwargs[key]}
            if self.current_text is None:
                self.change_text(key)

    def change_text(self, index):
        self.current_text = self.tabs[index]["text"]

    def update(self, surface):
        pass

    def event_loop(self, event):
        for tab in self.tabs:
            tab['button'].check_event(event)