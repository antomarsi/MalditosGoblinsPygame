import pygame, os, time, random, math, datetime, numpy
from pygame.locals import *
import goblin
from PIL import Image
from gui.SpriteLoader import SpriteLoader
from gui.Sprite import Sprite
from gui.Colors import Colors
from gui.Button import Button

pygame.font.init()
FONT_LRG = pygame.font.Font('font/GoblinOne.otf', 24)
FONT_MED = pygame.font.Font('font/GoblinOne.otf', 16)
FONT_SML = pygame.font.Font('font/GoblinOne.otf', 8)
FONT_VR_SML = pygame.font.Font('font/GoblinOne.otf', 7)

BUTTON_STYLE = {"hover_color" : Colors.BLUE,
                "clicked_color" : Colors.GREEN,
                "clicked_font_color" : Colors.BLACK,
                "hover_font_color" : Colors.ORANGE}
class Game:
    bg = None
    click = 0
    def __init__(self, *args, **kwargs):
        print ("Init pygame:")
        pygame.init()
        pygame.display.init()
        print ("(done)")
        
        self.rootParent = self
        self.screenSize = (720, 576)

        self.screen = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF)
        pygame.display.set_caption("Goblins Malditos v2 Remade")
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

        self.clock = pygame.time.Clock()
        self.goblin = goblin.Goblin('data.json')
        self.sprite_loader = SpriteLoader.instance()
        self.sprite_loader.load('sprites/uipack_rpg_sheet.png', 'sprites/uipack_rpg_sheet.json')
        self.cursor = self.sprite_loader.get_image('cursorGauntlet_grey')
        self.background = self.sprite_loader.get_image('panelInset_beigeLight')
        self.background = pygame.transform.scale(self.background, (710, 566))
        self.buttons = {}
        self.init_buttons()

    def init_buttons(self):
        self.buttons['minus_health'] = Button((0,0,200,50), Colors.RED, self.change_color, text='TESTE', **BUTTON_STYLE)
        pass

    def change_color(self):
        pass

    def draw_buttons(self):
        panel = pygame.Surface(self.screenSize, pygame.SRCALPHA, 32)
        mouse = pygame.mouse.get_pos()

        sprites = pygame.sprite.Group()

        life_button = pygame.transform.smoothscale(SPRITE['BUTTON']["ARROW"][0], [40, 80])
        life_button = Sprite(pygame.transform.rotate(life_button, 90), [250, 0])
        button_rect = life_button.rect
        if button_rect.collidepoint(mouse[0]-20, mouse[1]-12) and self.click == 1:
            if (mouse[0] <= button_rect.centerx+10):
                life_button.image = pygame.transform.rotate(pygame.transform.smoothscale(SPRITE['BUTTON']["ARROW"][1], [40, 80]), 90)
                self.goblin.take_damage()
            else:
                life_button.image = pygame.transform.rotate(pygame.transform.smoothscale(SPRITE['BUTTON']["ARROW"][2], [40, 80]), 90)
                self.goblin.take_heal()

        sprites.add(life_button)
        sprites.draw(panel)

        return panel

    def draw_panel(self, goblin):
        panel = pygame.Surface(self.screenSize)
        panel.fill((200,180,140))
        linha = 50

        sprites = pygame.sprite.Group()
        
        goblinsprite  = blit_tinted(SPRITE["GOBLIN_GREY"], goblin.cor['rgb']);
        goblinsprite = Sprite(pygame.transform.smoothscale(goblinsprite, [180, 180]),[0,linha])
        sprites.add(goblinsprite)
        
        
        #texts
        text = FONT_MED.render('Nome: '+str(goblin.nome)+' - Level: '+str(goblin.nivel), True, (0,0,0))
        panel.blit(text, [180, linha])  
        linha += 16      
        #cor
        panel.blit(FONT_SML.render('Cor: '+str(goblin.cor['nome']), True, (0, 0, 0)), [180, linha])
        linha += 16
        panel.blit(FONT_SML.render('Caracteristica: '+str(goblin.caracteristica['nome']), True, (0, 0, 0)), [180, linha])
        linha += 16
        panel.blit(FONT_SML.render('Armas: ', True, (0, 0, 0)), [180, linha])
        linha += 16
        for index, arma in  enumerate(goblin.equipamento):
            panel.blit(FONT_SML.render(str(arma.nome)+' Dano: '+str(arma.dano), True, (0, 0, 0)), [180, linha])            
            linha += 16

        panel.blit(FONT_SML.render('Ocupação: '+str(goblin.ocupacao['nome']), True, (0, 0, 0)), [180, linha])
        linha += 16
        panel.blit(FONT_SML.render('Especiais: ', True, (0, 0, 0)), [180, linha])
        linha += 16

        for index, skill in enumerate(goblin.skill):
            level = 'Level '+str(index+1)
            panel.blit(FONT_SML.render(level, True, (0, 0, 0)), [180, linha])
            linha += 16
            panel.blit(FONT_SML.render(skill['title'], True, (0,0,0)), [200, linha])
            linha += 16
            if((len(skill['descricao'])) > 5):
                panel.blit(FONT_VR_SML.render(skill['descricao'][:int(len(skill['descricao'])/2)], True, (10,10,10)), [200, linha])
                linha += 16
                panel.blit(FONT_VR_SML.render(skill['descricao'][int(len(skill['descricao'])/2):], True, (10,10,10)), [200, linha])
                linha += 16

        if goblin.anomalia:
            panel.blit(FONT_SML.render('Anomalias: ', True, (0, 0, 0)), [180, linha])
            linha += 16
            for index, anomalia in enumerate(goblin.anomalia):
                panel.blit(FONT_SML.render(anomalia, True, (0,0,0)), [200, linha])
                linha += 16

        #lives
        hearth_full = pygame.transform.smoothscale(SPRITE['HEART'][1], [50, 50])
        hearth_empty = pygame.transform.smoothscale(SPRITE['HEART'][0], [50, 50])

        for hp in range(1, 5):
            if hp <= goblin.vitalidade:
                vida = hearth_full
            else:
                vida = hearth_empty
            sprites.add(Sprite(vida,[(50*(hp-1))+(10*hp),0]))

        #STATUS
        status = [
            ["FOR", goblin.combate],
            ["CON", goblin.conhecimento],
            ["HAB", goblin.habilidade],
            ["SOR", goblin.sorte]
        ]
        for index, stat in enumerate(status):
            panel.blit(FONT_LRG.render(stat[0], True, (0, 0, 0)), [32, linha+(40*index)])
            for value in range(1, 5):
                #stat[1]
                if value <= stat[1]:
                    sprite = pygame.transform.smoothscale(SPRITE['STAR'][1], [30, 30])
                else:
                    sprite = pygame.transform.smoothscale(SPRITE['STAR'][0], [30, 30])
                sprites.add(Sprite(sprite,[60+(52*value), linha+(40*index)-5]))
        sprites.draw(panel)
        return panel

    def update(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            self.buttons[button].update(self.screen)
        self.update_cursor()

    def update_cursor(self):
        self.screen.blit(self.cursor, pygame.mouse.get_pos())

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def run(self):
        # Main Loop
        self.running = True
        while (self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for button in self.buttons:
                    self.buttons[button].check_event(event)
            self.update()
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

if __name__ == '__main__': 
    game = Game()
    game.run()
