import pygame
from itertools import chain

def drawText(surface, text, color, rect, font, aa=False, bkg=None, drop_shadow=None, shadow_color=(0, 0, 0), wrap=False, overflow=False, center=False):
    rect = pygame.Rect(rect)

    y = rect.top
    lineSpacing = -2
    # get the height of the font

    fontHeight = font.size("Tg")[1]
    fontWidth = font.size("Tg")[0]
    if not wrap:
        if bkg:
            image = font.render(text, 1, color, bkg)
#            image.set_colorkey(bkg)
        else:
            image = font.render(text, aa, color)
        if center:
            rect = image.get_rect(center=rect.center)
        if drop_shadow:
            shadow = font.render(text, aa, shadow_color)
            shadow.blit(image, (drop_shadow[0] * -1, drop_shadow[1] * -1))
            image = shadow
        if surface is None:
            return image.convert_alpha()
        surface.blit(image, (rect.left, rect.top))
    elif wrap and overflow:
        texts = wrapline(text, font, rect.width)
        greater_height = rect.height
        if rect.height < len(texts) * fontHeight:
            greater_height = len(texts) * fontHeight
        rect.height = greater_height
        greater_width = 0
        for text in texts:
            width = image = font.render(text, aa, color).get_width()
            if width > greater_width:
                greater_width = width
        rect.width = greater_width
        if surface is None:
            surface = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        for i in range(0, len(texts)):
            image = font.render(texts[i], aa, color)
            if drop_shadow:
                shadow = font.render(texts[i], aa, shadow_color)
                shadow.blit(image, (drop_shadow[0] * -1, drop_shadow[1] * -1))
                image = shadow
            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
        return surface
    else:
        if surface is None:
            surface = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        while text:
            i = 1
            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom and not overflow:
                break
            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1
            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1
            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)
            if drop_shadow:
                shadow = font.render(text[:i], aa, shadow_color)
                shadow.blit(image, (drop_shadow[0] * -1, drop_shadow[1] * -1))
                image = shadow
            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
            # remove the text we just blitted
            text = text[i:]
        return surface

def truncline(text, font, maxwidth):
        real=len(text)
        stext=text
        l=font.size(text)[0]
        cut=0
        a=0
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)
            done=0
        return real, done, stext

def wrapline(text, font, maxwidth):
    done=0
    wrapped=[]
    while not done:
        nl, done, stext=truncline(text, font, maxwidth)
        wrapped.append(stext.strip())
        text=text[nl:]
    return wrapped

def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)
