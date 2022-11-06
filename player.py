#Tori Wu
#June 10, 2019
#NEO-HEIST/player.py
#contains all player related functions; creates a player when Player class is called

import pygame

import constant
from sprites import spriteSheet

class Player (pygame.sprite.Sprite):

    #ATTRIBUTES------------------------
    
    #speed
    playerVelX = 0
    playerVelY = 0

    #lists containing sprite frames
    framesRight = []
    framesLeft = []
    
    direction = 'R'

    #sprites the player can touch -- will be taken from levels
    level = None
    
    #METHODS---------------------------
    
    #constuctor -- loads all sprite and sets starting frame
    def __init__ (self):
        
        pygame.sprite.Sprite.__init__(self)
        sheet = spriteSheet("sprites\character_spritesheet.png")

        #load all images into lists
        #left (framesLeft[])
        image = sheet.getImage(282, 0, 140, 238) #1-run 1
        self.framesLeft.append(image)
        image = sheet.getImage(0, 239, 140, 238) #2-step 1
        self.framesLeft.append(image)
        image = sheet.getImage(141, 239, 140, 238) #3-run 2
        self.framesLeft.append(image)
        image = sheet.getImage(282, 239, 140, 238) #4-step 2
        self.framesLeft.append(image)

        #right (framesRight[]) -- flip horizontally
        image = sheet.getImage(282, 0, 140, 238) #1-run 1
        image = pygame.transform.flip(image, True, False)
        self.framesRight.append(image)
        image = sheet.getImage(0, 239, 140, 238) #2-step 1
        image = pygame.transform.flip(image, True, False)
        self.framesRight.append(image)
        image = sheet.getImage(141, 239, 140, 238) #3-run 2
        image = pygame.transform.flip(image, True, False)
        self.framesRight.append(image)
        image = sheet.getImage(282, 239, 140, 238) #4-step 2
        image = pygame.transform.flip(image, True, False)
        self.framesRight.append(image)

        #starting sprite
        self.image = self.framesRight[0]

        self.rect = self.image.get_rect()

    #move the player
    def update (self):

        self.calcGravity()

        #moving right or left
        self.rect.x += self.playerVelX
        
        position = self.rect.x + self.level.worldShift

        #character sprite animation
        if self.direction == 'R':
            frame = (position//30) % len(self.framesRight)
            self.image = self.framesRight[frame]
        elif self.direction == 'L':
            frame = (position//30) % len (self.framesLeft)
            self.image = self.framesLeft[frame]

        #check for collision
        blockHitList = pygame.sprite.spritecollide (self, self.level.platformList, False)

        for block in blockHitList:
            #if hit, right side of player becomes left side of item and vice versa
            if self.playerVelX > 0:
                self.rect.right = block.rect.left
            elif self.playerVelX < 0:
                self.rect.left = block.rect.right

        #moving up or down
        self.rect.y += self.playerVelY

        #check for collision
        blockHitList = pygame.sprite.spritecollide (self,self.level.platformList, False)

        #if hit, bottom of player becomes top of item and vice versa
        for block in blockHitList:
            if self.playerVelY > 0:
                self.rect.bottom = block.rect.top
            elif self.playerVelY < 0:
                self.rect.top = block.rect.bottom
        
    #calculate gravity - 
    def calcGravity (self):
        if self.playerVelY == 0:
            self.playerVelY = 1
        else:
            self.playerVelY += 0.35
        
    #when user hits up arrow
    def jump(self):

        #check if platform is below player
        self.rect.y += 2
        platformHitList = pygame.sprite.spritecollide(self,self.level.platformList, False)
        self.rect.y -=2                                              

        #if player is on platform, then jump
        if len(platformHitList) > 0:
            self.playerVelY = -10
            
            #sfx
            jump_sfx = pygame.mixer.Sound('sounds/jumpsfx.wav')
            jump_sfx.set_volume(0.8)
            jump_sfx.play()

    #horizontal movement
    def goLeft (self):                                                
        self.playerVelX = -6
        self.direction = 'L'      
        
    def goRight (self):
        self.playerVelX = 6
        self.direction = 'R'

    #when nothing is pressed
    def stop (self):
        self.playerVelX = 0
        self.image = self.framesRight[0]
    
