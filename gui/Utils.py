import pygame

def fastsaturation(surf, sat):
    arr = pygame.surfarray.pixels3d(surf)
    parr = arr.astype("float", copy = True)
    parr **= 2
    parr[:,:,0] *= 0.299
    parr[:,:,1] *= 0.587
    parr[:,:,2] *= 0.114
    parr[:,:,0] += parr[:,:,1] + parr[:,:,2]
    parr[:,:,0] **= 0.5
    parr[:,:,1] = parr[:,:,0]
    parr[:,:,2] = parr[:,:,0]
    arrdash = arr.astype("float", copy = True)
    arrdash -= parr
    arrdash *= sat
    arrdash += parr
    arrdash.clip(0, 255, arrdash)
    arr[:,:,:] = arrdash