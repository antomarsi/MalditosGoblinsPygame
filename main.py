import pygame, os, time, random, math, datetime
from pygame.locals import *
import goblin

BG_COLOR = [210, 206, 170]

def getTimeStr():
    curTime = time.localtime(time.time())
    curTimeStr = "%s.%s.%s, %s:%s" %(curTime.tm_mday, curTime.tm_mon, curTime.tm_year, curTime.tm_hour, '%02d' % curTime.tm_min, )
    return curTimeStr

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = image_file
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Engine:
    
    def __init__(self, *args, **kwargs):
        print ("Init pygame:")
        pygame.init()
        pygame.display.init()
        print ("(done)")
        
        self.rootParent = self
        self.screenSize = (720, 576)
        self.canvasSize = (720, 576)
        
        print ('Resolution: {0}x{1}'.format(self.screenSize[0], self.screenSize[1]))
        print ('Canvas Size: {0}x{1}'.format(self.canvasSize[0], self.canvasSize[1]))
        
        # Don't show mouse-pointer:
        self.screen = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF)
        pygame.display.set_caption("Goblins Malditos v2")

        self.clock = pygame.time.Clock()
        self.goblin = goblin.Goblin('data.json')

    def draw_bg(self):
        self.screen.fill([0, 0, 0])
        background = pygame.sprite.Group()
        #background.add(Sprite("GenUI/window1.png", [0, 0]))
        middle = [self.screenSize[0]-(122*2), self.screenSize[1]-(64+92)]

        pygame.draw.rect(self.screen, BG_COLOR, [122,92, middle[0], middle[1]])

        background.add(Sprite(pygame.transform.scale(
            pygame.image.load("GenUI/window6.png"), [122, middle[1]+14]), [0, 85]))
        #background.add(Sprite(pygame.transform.scale(
        #    pygame.image.load("GenUI/window5.png"), [middle[0], 120]), [122, 0]))
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
        background.draw(self.screen)

    def draw

    def run(self):
        # Main Loop
        running = True
        while running:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    running = False # Flag that we are done so we exit this loop
            self.draw_bg()
            sefl.draw_panel()
            pygame.display.flip()
            self.clock.tick(15)
        pygame.quit()

if __name__ == '__main__': 
    engine = Engine()
    engine.run()

