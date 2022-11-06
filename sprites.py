#Tori Wu
#June 10, 2019
#NEO-HEIST/sprites.py
#contains a class that allows sprites to be taken from spritesheets.

import pygame
import constant

class spriteSheet (object):

    #spritesheet png image
    sheet = None

    #constructor - loads spritesheet into sheet
    def __init__ (self, filename): 
        self.sheet = pygame.image.load(filename).convert()

    #cuts image sprite from sheet 
    def getImage (self, x, y, width, height): 
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sheet,(0,0), (x, y, width, height))

        #creates transparent image
        image.set_colorkey(constant.BLACK)
        return image


        
        
