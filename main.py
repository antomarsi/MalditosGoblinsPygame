import pygame, os, time, random, math, datetime
from pygame.locals import *
import goblin

def getTimeStr():
    curTime = time.localtime(time.time())
    curTimeStr = "%s.%s.%s, %s:%s" %(curTime.tm_mday, curTime.tm_mon, curTime.tm_year, curTime.tm_hour, '%02d' % curTime.tm_min, )
    return curTimeStr

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
        pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF)

        self.clock = pygame.time.Clock()
        self.goblin = goblin.Goblin('data.json')

    def run(self):
        # Main Loop
        running = True
        while running:
            self.clock.tick(15)
        pygame.quit()

if __name__ == '__main__': 
    engine = Engine()
    engine.run()

