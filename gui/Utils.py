import pygame
from random import randint

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
    return rgb.astype('uint8')

def hex_to_rgb(hex_color = 0x000000):
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2 ,4))

def get_random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def color_variant(rgb_color, brightness_offset=1):
    """ takes a color like #87c95f and produces a lighter or darker variant """
    return tuple(min(255, max(0, rgb_value + brightness_offset)) for rgb_value in rgb_color)
