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
        "GenUI/UI_HEART_EMPTY.png",
        "GenUI/UI_HEART_FULL.png"
        ],
    "GOBLIN":pygame.image.load("img/goblin.png"),
    "GOBLIN_GREY":pygame.image.load("img/goblin_grey.png")
    }

SCREEN_SIZE = (720, 576)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = image_file
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Engine:
    bg = None

    def __init__(self, *args, **kwargs):
        print ("Init pygame:")
        pygame.init()
        pygame.display.init()

        FONT_LRG = pygame.font.Font('font/GoblinOne.otf', int (SCREEN_SIZE[1] * (24.0 / 360.0)))
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

    def draw_panel(self, goblin):
        panel = pygame.Surface([int(self.interiorSize[0]/2), int(self.interiorSize[1]/2)])
        panel.fill((200,180,140))

        sprites = pygame.sprite.Group()
        
        goblinsprite  = blit_tinted(SPRITE["GOBLIN_GREY"], goblin.cor['rgb']);
        #goblin.fill((10, 10, 10, 10), None, pygame.BLEND_RGBA_ADD)
        #goblin.fill((255, 0, 0) + (0,), None, pygame.BLEND_RGBA_ADD)
        sprites.add(Sprite(pygame.transform.smoothscale(goblinsprite, [180, 180]),[0,0]))
        sprites.draw(panel)

        #pygame.draw.rect(panel, (80,80,80),
        #    [self.interiorSize[0]/2,0, self.interiorSize[0]/2, self.interiorSize[1]/2])

        #pygame.draw.rect(panel, (160,160,160),
        #    [0,self.interiorSize[1]/2, self.interiorSize[0]/2, self.interiorSize[1]/2])

        #pygame.draw.rect(panel, (200,200,200),
        #    [self.interiorSize[0]/2,self.interiorSize[1]/2, self.interiorSize[0]/2, self.interiorSize[1]/2])

        return panel

    def run(self):
        # Main Loop
        running = True
        while running:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    running = False # Flag that we are done so we exit this loop

            if not self.bg:
                self.bg = self.draw_bg()
            self.bg.draw(self.screen)
            pygame.draw.rect(
                self.screen, BG_COLOR, [7.5, 64, self.screenSize[0]-15, self.screenSize[1]-64*2])
            if self.goblin.get_changed():
                self.panel = self.draw_panel(self.goblin)

            self.screen.blit(self.panel, self.marginSize)

            pygame.display.flip()

            self.clock.tick(15)
            self.goblin.changed = False
        pygame.quit()

if __name__ == '__main__': 
    engine = Engine()
    engine.run()
