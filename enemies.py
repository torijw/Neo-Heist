#Tori Wu
#June 10, 2019
#NEO-HEIST/enemies.py
#contains a class with every enemy related function

import pygame
from sprites import spriteSheet

#similar and referenced from platforms.py
#name = (x, y, width, height)
MOB_SPRITE = (0,0,55,95)

class Mob (pygame.sprite.Sprite):

    def __init__(self, sheetData):
        
        pygame.sprite.Sprite.__init__(self)

        sheet = spriteSheet("sprites/guard.png")

        self.image = sheet.getImage (sheetData[0], #X
                                     sheetData[1], #Y
                                     sheetData[2], #width
                                     sheetData[3]) #height

        #sprite dimensions
        self.rect = self.image.get_rect()


class movingMob (Mob):

    #ATTRIBUTES---------

    #speed
    VelX = 0

    #boundaries - mob will move from left to right
    boundaryLeft = 0
    boundaryRight = 0

    def update(self):

        #move left/right
        self.rect.x += self.VelX

        #check to see if mob needs to turn around
        curPosition = self.rect.x - self.level.worldShift
        if curPosition <self.boundaryLeft or curPosition > self.boundaryRight:
            self.VelX *= -1
        
