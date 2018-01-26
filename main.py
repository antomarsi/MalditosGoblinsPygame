import pygame, os, time, random, math, datetime, numpy
from pygame.locals import *
import goblin
from PIL import Image



def getTimeStr():
    curTime = time.localtime(time.time())
    curTimeStr = "%s.%s.%s, %s:%s" %(curTime.tm_mday, curTime.tm_mon, curTime.tm_year, curTime.tm_hour, '%02d' % curTime.tm_min, )
    return curTimeStr

def blit_tinted(image, tint, src_rect=None):
    if src_rect:
        image = image.subsurface(src_rect)
    buf = pygame.Surface(image.get_size(), SRCALPHA, 32)
    buf.blit(image, (0, 0))
    src_rgb = pygame.surfarray.array3d(image)
    buf_rgb = pygame.surfarray.pixels3d(buf)
    buf_rgb[...] = numpy.minimum(255, numpy.add(tint, src_rgb)).astype('b')
    buf_rgb = None
    return buf
BG_COLOR = [210, 206, 170]

SPRITE = {
    "HEART": [
        pygame.image.load("GenUI/UI_HEART_EMPTY.png"),
        pygame.image.load("GenUI/UI_HEART_FULL.png")
        ],
    "STAR": [
        pygame.image.load("GenUI/UI_STAR_EMTPY.png"),
        pygame.image.load("GenUI/UI_STAR_NORMAL.png")
    ],
    "GOBLIN":pygame.image.load("img/goblin.png"),
    "GOBLIN_GREY":pygame.image.load("img/goblin_grey.png"),
    "SYMB":{
        "LEFT": pygame.image.load("Symbols/SYMB_LEFTARROW.png"),
        "RIGHT": pygame.image.load("Symbols/SYMB_RIGHTARROW.png")
        },
    "BUTTON":{
        "ARROW": [
            pygame.image.load("Buttons/BTN_VERT_ (4).png"),
            pygame.image.load("Buttons/BTN_VERT_ (14).png"),
            pygame.image.load("Buttons/BTN_VERT_ (24).png"),
            ]
        }
    }

SCREEN_SIZE = (720, 576)
pygame.font.init()
FONT_LRG = pygame.font.Font('font/GoblinOne.otf', 24)
FONT_MED = pygame.font.Font('font/GoblinOne.otf', 16)
FONT_SML = pygame.font.Font('font/GoblinOne.otf', 8)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = image_file
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Engine:
    bg = None
    click = 0
    def __init__(self, *args, **kwargs):
        print ("Init pygame:")
        pygame.init()
        pygame.display.init()

        
        print ("(done)")
        
        self.rootParent = self
        self.screenSize = SCREEN_SIZE
        self.interiorSize = [
            SCREEN_SIZE[0]*0.95,
            SCREEN_SIZE[1]*0.95,
        ]
        self.marginSize = [
            SCREEN_SIZE[0]*0.025,
            SCREEN_SIZE[1]*0.025,
        ]
        
        print ('Resolution: {0}x{1}'.format(self.screenSize[0], self.screenSize[1]))
        
        # Don't show mouse-pointer:
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF)
        pygame.display.set_caption("Goblins Malditos v2")

        self.clock = pygame.time.Clock()
        self.goblin = goblin.Goblin('data.json')

    def draw_bg(self):
        self.screen.fill([0, 0, 0])
        background = pygame.sprite.Group()
        #background.add(Sprite("GenUI/window1.png", [0, 0]))
        middle = [self.screenSize[0]-(122*2), self.screenSize[1]-(64+92)]
        background.add(Sprite(pygame.transform.scale(
            pygame.image.load("GenUI/window6.png"), [122, middle[1]+14]), [0, 85]))
        background.add(Sprite(pygame.transform.scale(
            pygame.image.load("GenUI/window5.png"),
            [122, self.screenSize[1]-(64*2)]), [middle[0]+122, 64]
                             )
                      )
        #TOP
        background.add(Sprite(pygame.image.load("GenUI/window8.png"), [0, 0]))
        background.add(Sprite(pygame.transform.scale(
            pygame.image.load("GenUI/window9.png"), [middle[0], 92]), [122, 0]))
        background.add(Sprite(pygame.image.load("GenUI/window7.png"), [self.screenSize[0]-122, 0]))
        #BOTTOM
        background.add(Sprite(pygame.image.load("GenUI/window2.png"), [0, self.screenSize[1]-64]))
        background.add(Sprite(pygame.transform.scale(
            pygame.image.load("GenUI/window3.png"), [middle[0], 64]), [122, self.screenSize[1]-64]))
        background.add(Sprite(pygame.image.load("GenUI/window4.png"), [self.screenSize[0]-122, self.screenSize[1]-64]))


        return background
    def draw_buttons(self):
        panel = pygame.Surface(self.screenSize, pygame.SRCALPHA, 32)
        mouse = pygame.mouse.get_pos()

        sprites = pygame.sprite.Group()

        life_button = pygame.transform.smoothscale(SPRITE['BUTTON']["ARROW"][0], [40, 80])
        life_button = Sprite(pygame.transform.rotate(life_button, 90), [250, 180])
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
        panel = pygame.Surface([int(self.interiorSize[0]), int(self.interiorSize[1])])
        panel.fill((200,180,140))

        sprites = pygame.sprite.Group()
        
        goblinsprite  = blit_tinted(SPRITE["GOBLIN_GREY"], goblin.cor['rgb']);
        goblinsprite = Sprite(pygame.transform.smoothscale(goblinsprite, [180, 180]),[0,0])
        sprites.add(goblinsprite)
        
        #texts
        text = FONT_MED.render('Level: '+str(goblin.nivel), True, (0,0,0))
        panel.blit(text, [180, 10])

        #cor
        panel.blit(FONT_SML.render('Cor: '+str(goblin.cor['nome']), True, (0, 0, 0)), [180, 32])
        panel.blit(FONT_SML.render('Caracteristica: '+str(goblin.caracteristica['nome']), True, (0, 0, 0)), [180, 48])
        if goblin.anomalia:
            panel.blit(FONT_SML.render('Anomalias: ', True, (0, 0, 0)), [180, 64])
            for index, anomalia in enumerate(goblin.anomalia):
                panel.blit(FONT_SML.render(anomalia, True, (0,0,0)), [200, 80+(10*index)])
        #lives
        hearth_full = pygame.transform.smoothscale(SPRITE['HEART'][1], [50, 50])
        hearth_empty = pygame.transform.smoothscale(SPRITE['HEART'][0], [50, 50])

        for hp in range(1, 5):
            if hp <= goblin.vitalidade:
                vida = hearth_full
            else:
                vida = hearth_empty
            sprites.add(Sprite(vida,[(50*(hp-1))+(10*hp),180]))

        #STATUS
        status = [
            ["FOR", goblin.combate],
            ["CON", goblin.conhecimento],
            ["HAB", goblin.habilidade],
            ["SOR", goblin.sorte]
        ]
        for index, stat in enumerate(status):
            panel.blit(FONT_LRG.render(stat[0], True, (0, 0, 0)), [32, (self.interiorSize[0]/2)+(40*index)])
            for value in range(1, 5):
                #stat[1]
                if value <= stat[1]:
                    sprite = pygame.transform.smoothscale(SPRITE['STAR'][1], [30, 30])
                else:
                    sprite = pygame.transform.smoothscale(SPRITE['STAR'][0], [30, 30])
                sprites.add(Sprite(sprite,[60+(52*value), (self.interiorSize[0]/2)+(40*index)-5]))


        sprites.draw(panel)
        return panel

    def run(self):
        # Main Loop
        running = True
        while running:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    running = False # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = event.button
            buttons = self.draw_buttons()
            if not self.bg:
                self.bg = self.draw_bg()
            self.bg.draw(self.screen)
            pygame.draw.rect(
                self.screen, BG_COLOR, [7.5, 64, self.screenSize[0]-15, self.screenSize[1]-64*2])
            if self.goblin.get_changed():
                self.panel = self.draw_panel(self.goblin)

            self.screen.blit(self.panel, self.marginSize)
            self.screen.blit(buttons, self.marginSize)
            

            pygame.display.flip()

            self.clock.tick(10)
            self.goblin.changed = False
            self.click = 0
        pygame.quit()

if __name__ == '__main__': 
    engine = Engine()
    engine.run()
