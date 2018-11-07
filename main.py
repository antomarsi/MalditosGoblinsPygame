import pygame, os, time, random, math, datetime, numpy
from pygame.locals import *
from goblin.goblin import Goblin
from PIL import Image
from gui.SpriteLoader import SpriteLoader
from gui.Colors import Colors
from gui.Button import TextButton, IconButton
from gui.Panel import Panel
from gui.TabTextArea import TabTextArea
from gui.HealthBar import HealthBar
from gui.ToolTip import ToolTip

pygame.font.init()

FONT_LRG = pygame.font.Font('font/Kenney Pixel.ttf', 24)
FONT_MED = pygame.font.Font('font/Kenney Pixel Square.ttf', 17)
FONT_SML = pygame.font.Font('font/Kenney Pixel Square.ttf', 14)
FONT_VR_SML = pygame.font.Font('font/Kenney Pixel Square.ttf', 10)

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
        self.screenSize = (720, 494)

        self.screen = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF)
        pygame.display.set_caption("Malditos Goblins - Gerador de Goblin v2 Remake")
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

        self.clock = pygame.time.Clock()
        self.sprite_loader = SpriteLoader.instance()
        print('Loading textures')
        self.sprite_loader.load('sprites/ui_big_pieces.png', 'sprites/ui_big_pieces.json')
        print('(done)')
        self.mana_bar = None
        self.use_magic = False
        self.reset_goblin()
        self.cursor = self.sprite_loader.get_image('cursor')
        self.cursor = pygame.transform.scale(self.cursor, (24, 34))
        self.cursor_click = self.sprite_loader.get_image('cursor_click')
        self.cursor_click = pygame.transform.scale(self.cursor_click, (24, 34))
        self.click_holding = False
        self.fixed_gui = []
        # background
        self.fixed_gui.append(Panel(((0, 0), self.screenSize)))
        # Temporary Goblin Avatar Frame
        self.fixed_gui.append(Panel(((10, 10), (200, 237))))
        # Temporary Stats Frame
        self.fixed_gui.append(Panel(((10, 257), (200, 227))))
        # Features
        self.fixed_gui.append(Panel(((220, 80), (483, 167))))


        self.tooltip = ToolTip(text="Fazendo teste de tooltip", rect=(100, 50, 200, 50), max_width=200, font=FONT_VR_SML)
        self.buttons = []
        self.init_buttons()

    def reset_goblin(self):
        self.goblin = Goblin()
        self.magic_buttons = []
        self.skills_textarea = TabTextArea((220, 257, 483, 200), FONT_MED, FONT_SML, self.goblin.skills)
        self.health_bar = HealthBar((217, 20, 130, 20), self.goblin.max_health, **{'font': FONT_VR_SML})
        self.mana_bar = HealthBar((217, 50, 130, 20), self.goblin.max_mana, **{'font': FONT_VR_SML})
        self.use_magic = self.goblin.can_use_mana
        self.magic_buttons.append(IconButton((353, 48, 0, 0), self.minus_goblin_health, **{'sprite_icon': 'icon_minus', 'sprite': 'round_button_green', 'scale': 1.5}))
        self.magic_buttons.append(IconButton((380, 48, 0, 0), self.plus_goblin_health, **{'sprite_icon': 'icon_plus', 'sprite': 'round_button_green', 'scale': 1.5}))
 

    def init_buttons(self):
        print('Loading Buttons')
        self.buttons.append(TextButton((540, 10, 170, 50), self.reset_goblin, text='Criar Goblin', **{'font': FONT_MED}))
        self.buttons.append(TextButton((565, 40, 120, 50), self.level_up_goblin, text='Level Up', **{'font': FONT_MED}))
        self.buttons.append(IconButton((353, 18, 0, 0), self.minus_goblin_health, **{'sprite_icon': 'icon_minus', 'sprite': 'round_button_green', 'scale': 1.5}))
        self.buttons.append(IconButton((380, 18, 0, 0), self.plus_goblin_health, **{'sprite_icon': 'icon_plus', 'sprite': 'round_button_green', 'scale': 1.5}))
        print('(done)')

    def level_up_goblin(self):
        self.goblin.set_level(self.goblin.level+1)

    def minus_goblin_health(self):
        self.goblin.set_health(self.goblin.current_health-1)
        self.health_bar.set_value(self.goblin.current_health)

    def plus_goblin_health(self):
        self.goblin.set_health(self.goblin.current_health+1)
        self.health_bar.set_value(self.goblin.current_health)

    def update(self):
        self.screen.fill((0, 0, 0))
        for fixed_gui in self.fixed_gui:
            fixed_gui.update(self.screen)
        for button in self.buttons:
            button.update(self.screen)
        self.skills_textarea.update(self.screen)
        self.health_bar.update(self.screen)
        if self.use_magic:
            self.mana_bar.update(self.screen)
            for magic_button in self.magic_buttons:
                magic_button.update(self.screen)
        self.tooltip.update(self.screen)
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
            button.check_event(event)
        self.tooltip.check_hover()
        self.skills_textarea.event_loop(event)
        if self.use_magic:
            for magic_button in self.magic_buttons:
                magic_button.check_event(event)

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
