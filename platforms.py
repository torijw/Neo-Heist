#Tori Wu
#June 10, 2019
#NEO-HEIST/platform.py
#contains a class that allows platforms to be built using the spritesheet function

import pygame
from sprites import spriteSheet

#create types of platform blocks using spriteSheet function
#name = (x, y, width, height) - of image
BLOCK_RIGHT = (152,0,75,75)
BLOCK_MIDDLE = (152,76,75,75)
BLOCK_LEFT = (152,152,75,75)
BUILDING_RIGHTCORNER = (0,0,75,75)
BUILDING_TOP = (0,76,75,75)
BUILDING_LEFTCORNER = (76,0,75,75)
BUILDING_RIGHTSIDE = (76,76,75,75)
BUILDING_MIDDLE = (0,152,75,75)
BUILDING_LEFTSIDE = (76,152,75,75)

#takes in blocks from above and enters them into the function
class Platform (pygame.sprite.Sprite):
    
    #creates a sprite from the block
    def __init__(self, sheetData):
        
        pygame.sprite.Sprite.__init__(self)
        sheet = spriteSheet("sprites/platform_spritesheet.png")

        self.image = sheet.getImage (sheetData[0], #X
                                     sheetData[1], #Y
                                     sheetData[2], #width
                                     sheetData[3]) #height

        #get dimensions of sprite
        self.rect = self.image.get_rect()
        
