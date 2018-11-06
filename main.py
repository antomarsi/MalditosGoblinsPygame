import pygame, os, time, random, math, datetime, numpy
from pygame.locals import *
from goblin.goblin import Goblin
from PIL import Image
from gui.SpriteLoader import SpriteLoader
from gui.Colors import Colors
from gui.Button import TextButton
from gui.Panel import Panel
from gui.TabTextArea import TabTextArea
from gui.HealthBar import HealthBar

pygame.font.init()

FONT_LRG = pygame.font.Font('font/Kenney Pixel.ttf', 24)
FONT_MED = pygame.font.Font('font/Kenney Pixel Square.ttf', 17)
FONT_SML = pygame.font.Font('font/Kenney Pixel Square.ttf', 14)
FONT_VR_SML = pygame.font.Font('font/Kenney Pixel Square.ttf', 12)

class Game:
    bg = None
    click = 0

    def __init__(self, *args, **kwargs):
        print ("Init pygame:")
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.init()
        print ("(done)")

        self.rootParent = self
        self.screenSize = (720, 576)

        self.screen = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF)
        pygame.display.set_caption("Malditos Goblins - Gerador de Goblin v2 Remake")
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

        self.clock = pygame.time.Clock()
        self.sprite_loader = SpriteLoader.instance()
        self.sprite_loader.load('sprites/ui_big_pieces.png', 'sprites/ui_big_pieces.json')
        self.reset_goblin()
        self.background = Panel(((0, 0), self.screenSize))
        self.cursor = self.sprite_loader.get_image('cursor')
        self.cursor = pygame.transform.scale(self.cursor, (24, 34))
        self.cursor_click = self.sprite_loader.get_image('cursor_click')
        self.cursor_click = pygame.transform.scale(self.cursor_click, (24, 34))
        self.click_holding = False

        self.buttons = {}
        self.init_buttons()

    def reset_goblin(self):
        self.goblin = Goblin()
        self.skills_textarea = TabTextArea((100, 100, 300, 200), FONT_MED, FONT_SML, self.goblin.skills)
        self.health_bar = HealthBar((20, 20, 100, 20), self.goblin.max_health, **{'font': FONT_VR_SML})

    def init_buttons(self):
        self.buttons['reset_goblin'] = TextButton((500,50,200,50), self.reset_goblin, text='Criar Goblin', **{'font': FONT_MED})
    
    def minus_goblin_health(self):
        self.goblin.set_health(self.goblin.current_health-1)
        self.health_bar.set_value(self.goblin.current_health)

    def plus_goblin_health(self):
        self.goblin.set_health(self.goblin.current_health+1)
        self.health_bar.set_value(self.goblin.current_health)

    def update(self):
        self.screen.fill((0, 0, 0))
        self.background.update(self.screen)
        for button in self.buttons:
            self.buttons[button].update(self.screen)
        self.skills_textarea.update(self.screen)
        self.health_bar.update(self.screen)
        self.update_cursor()

    def update_cursor(self):
        if not self.click_holding:
            self.screen.blit(self.cursor, pygame.mouse.get_pos())
        else:
            self.screen.blit(self.cursor_click, pygame.mouse.get_pos())

    def event_loop(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.click_holding = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.click_holding = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            self.minus_goblin_health()
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            self.plus_goblin_health()
        for button in self.buttons:
            self.buttons[button].check_event(event)
        self.skills_textarea.event_loop(event)

    def run(self):
        self.running = True
        while (self.running):
            for event in pygame.event.get():
                self.event_loop(event)
            self.update()
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

if __name__ == '__main__': 
    game = Game()
    game.run()
