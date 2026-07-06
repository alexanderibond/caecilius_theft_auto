import pygame
import os

print("hello world")

pixel_vista = pygame.image.load(os.path.join('imgs', 'pixel_vista.png'))


import pygame
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Basic Pygame program')


    background = pygame.Surface((400,400))


    # Fill background

    background = background.convert() # makes it into single-pixel format
    background.blit(pixel_vista, (0, 0))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()
