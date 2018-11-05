import pygame

def drawText(surface, text, color, rect, font, aa=False, bkg=None, drop_shadow=None, shadow_color=(0, 0, 0), wrap=False, center=False):
    rect = pygame.Rect(rect)

    y = rect.top
    lineSpacing = -2
    # get the height of the font

    fontHeight = font.size("Tg")[1]
    if not wrap:
        if bkg:
            image = font.render(text, 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text, aa, color)
        if center:
            rect = image.get_rect(center=rect.center)
        if drop_shadow:
            shadow = font.render(text, aa, shadow_color)
            shadow.blit(image, (drop_shadow[0] * -1, drop_shadow[1] * -1))
            image = shadow
        if surface is None:
            return image
        surface.blit(image, (rect.left, rect.top))
    else:
        if surface is None:
            return_surface = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        while text:
            i = 1
            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
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
            if surface is not None:
                surface.blit(image, (rect.left, y))
            else:
                return_surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
            # remove the text we just blitted
            text = text[i:]
        if surface is None:
            return return_surface
        return text

