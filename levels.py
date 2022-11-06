#Tori Wu
#June 10, 2019
#NEO-HEIST/levels.py
#contains level-related code -- classes and functions 

import pygame
import constant
import platforms
import enemies

#super/parent class
class Level():

    #lists for platforms and mobs in each level
    platformList = None 
    enemyList = None 

    #background
    background = None

    #treasure
    treasure = None

    #variables for moving world and world restrictions
    worldShift = 0
    levelEnd = -1000
    levelBoundary = 0

    #loads all platforms, enemies, and the player
    def __init__ (self, player):
        self.platformList = pygame.sprite.Group()
        self.enemyList = pygame.sprite.Group()
        self.player = player

    #update everything in level
    def update (self):
        self.platformList.update()
        self.enemyList.update()

    #draws everything in the level
    def draw (self, screen):
        #background
        screen.fill(constant.BLACK)
        screen.blit(self.background, (self.worldShift // 3,0))

        #treasure
        screen.blit(self.treasure, (self.worldShift, 0))

        #sprites
        self.platformList.draw(screen)
        self.enemyList.draw(screen)

    #calculates how much the world scrolls left and right when character moves
    def moveWorld (self, shiftX):

        self.worldShift += shiftX

        #move all platforms and enemies along with the world
        for platform in self.platformList:
            platform.rect.x += shiftX

        for enemy in self.enemyList:
            enemy.rect.x += shiftX            

#create level 1
class Level_01 (Level):

    def __init__ (self, player):

        #calls parent constructor
        Level.__init__(self, player)

        #create backgrounds and world restrictions
        self.background = pygame.image.load("images/background.png").convert()
        self.background.set_colorkey(constant.BLACK)
        self.levelEnd = -3850
        self.levelBoundary = -15
        
        #load a transparent png for treasure because it doesn't exist in this level
        self.treasure = pygame.image.load("images/notreasure.png").convert()
        self.treasure.set_colorkey(constant.BLACK)
        
        #create all platforms in level using the platform class-- block type, x, y
        level = [ [platforms.BUILDING_TOP, 0, 550],
                  [platforms.BUILDING_TOP, 75, 550],
                  [platforms.BUILDING_TOP, 150, 550],
                  [platforms.BUILDING_TOP, 225, 550],
                  [platforms.BUILDING_TOP, 300, 550],
                  [platforms.BUILDING_TOP, 375, 550],
                  [platforms.BUILDING_TOP, 450, 550],
                  [platforms.BUILDING_TOP, 525, 550],
                  [platforms.BUILDING_TOP, 600, 550],
                  [platforms.BUILDING_RIGHTCORNER, 675, 550],
                  
                  [platforms.BLOCK_LEFT, 800, 400],
                  [platforms.BLOCK_MIDDLE, 875, 400],
                  [platforms.BLOCK_MIDDLE, 950, 400],
                  [platforms.BLOCK_MIDDLE, 1025, 400],
                  [platforms.BLOCK_RIGHT,1100, 400],

                  [platforms.BLOCK_LEFT, 1300, 450],
                  [platforms.BLOCK_MIDDLE, 1375, 450],
                  [platforms.BLOCK_MIDDLE, 1450, 450],
                  [platforms.BLOCK_MIDDLE, 1525, 450],
                  [platforms.BLOCK_RIGHT, 1600, 450],

                  [platforms.BLOCK_LEFT, 1300, 450],
                  [platforms.BLOCK_MIDDLE, 1375, 450],
                  [platforms.BLOCK_RIGHT, 1600, 450],

                  [platforms.BLOCK_LEFT, 1750, 300],
                  [platforms.BLOCK_RIGHT, 1825, 300],

                  [platforms.BLOCK_LEFT, 1950, 200],
                  [platforms.BLOCK_RIGHT, 2025, 200],

                  [platforms.BLOCK_LEFT, 2200, 450],
                  [platforms.BLOCK_MIDDLE, 2275, 450],
                  [platforms.BLOCK_MIDDLE, 2350, 450],
                  [platforms.BLOCK_MIDDLE, 2425, 450],
                  [platforms.BLOCK_MIDDLE, 2500, 450],
                  [platforms.BLOCK_MIDDLE, 2575, 450],
                  [platforms.BLOCK_MIDDLE, 2650, 450],
                  [platforms.BLOCK_MIDDLE, 2725, 450],
                  [platforms.BLOCK_MIDDLE, 2800, 450],
                  [platforms.BLOCK_MIDDLE, 2875, 450],
                  [platforms.BLOCK_RIGHT, 2950, 450],

                  [platforms.BLOCK_LEFT, 3200, 500],
                  [platforms.BLOCK_MIDDLE, 3275, 500],
                  [platforms.BLOCK_RIGHT, 3350, 500],

                  [platforms.BLOCK_LEFT, 3500, 400],
                  [platforms.BLOCK_MIDDLE, 3575, 400],
                  [platforms.BLOCK_RIGHT, 3650, 400],

                  [platforms.BUILDING_LEFTCORNER, 3800, 300],
                  [platforms.BUILDING_TOP, 3875, 300],
                  [platforms.BUILDING_TOP, 3950, 300],
                  [platforms.BUILDING_TOP, 4025, 300],
                  [platforms.BUILDING_TOP, 4100, 300],
                  [platforms.BUILDING_TOP, 4175, 300],
                  [platforms.BUILDING_TOP, 4250, 300],
                  [platforms.BUILDING_TOP, 4325, 300],
                  [platforms.BUILDING_TOP, 4400, 300],
                  [platforms.BUILDING_TOP, 4475, 300],
                  [platforms.BUILDING_RIGHTCORNER, 4550, 300],
                  [platforms.BUILDING_LEFTSIDE, 3800, 375],
                  [platforms.BUILDING_MIDDLE, 3875, 375],
                  [platforms.BUILDING_MIDDLE, 3950, 375],
                  [platforms.BUILDING_MIDDLE, 4025, 375],
                  [platforms.BUILDING_MIDDLE, 4100, 375],
                  [platforms.BUILDING_MIDDLE, 4175, 375],
                  [platforms.BUILDING_MIDDLE, 4250, 375],
                  [platforms.BUILDING_MIDDLE, 4325, 375],
                  [platforms.BUILDING_MIDDLE, 4400, 375],
                  [platforms.BUILDING_MIDDLE, 4475, 375],
                  [platforms.BUILDING_RIGHTSIDE, 4550,375],
                  [platforms.BUILDING_LEFTSIDE, 3800, 450],
                  [platforms.BUILDING_MIDDLE, 3875, 450],
                  [platforms.BUILDING_MIDDLE, 3950, 450],
                  [platforms.BUILDING_MIDDLE, 4025, 450],
                  [platforms.BUILDING_MIDDLE, 4100, 450],
                  [platforms.BUILDING_MIDDLE, 4175, 450],
                  [platforms.BUILDING_MIDDLE, 4250, 450],
                  [platforms.BUILDING_MIDDLE, 4325, 450],
                  [platforms.BUILDING_MIDDLE, 4400, 450],
                  [platforms.BUILDING_MIDDLE, 4475, 450],
                  [platforms.BUILDING_RIGHTSIDE, 4550,450],
                  [platforms.BUILDING_LEFTSIDE, 3800, 525],
                  [platforms.BUILDING_MIDDLE, 3875, 525],
                  [platforms.BUILDING_MIDDLE, 3950, 525],
                  [platforms.BUILDING_MIDDLE, 4025, 525],
                  [platforms.BUILDING_MIDDLE, 4100, 525],
                  [platforms.BUILDING_MIDDLE, 4175, 525],
                  [platforms.BUILDING_MIDDLE, 4250, 525],
                  [platforms.BUILDING_MIDDLE, 4325, 525],
                  [platforms.BUILDING_MIDDLE, 4400, 525],
                  [platforms.BUILDING_MIDDLE, 4475, 525],
                  [platforms.BUILDING_RIGHTSIDE, 4550,525],
                  
                  [platforms.BUILDING_LEFTCORNER, 4850, 300],
                  [platforms.BUILDING_TOP, 4925, 300],
                  [platforms.BUILDING_TOP, 5000, 300],
                  [platforms.BUILDING_TOP, 5075, 300],
                  [platforms.BUILDING_LEFTSIDE,4850, 375],
                  [platforms.BUILDING_MIDDLE, 4925, 375],
                  [platforms.BUILDING_MIDDLE, 5000, 375],
                  [platforms.BUILDING_MIDDLE, 5075, 375],
                  [platforms.BUILDING_LEFTSIDE,4850, 450],
                  [platforms.BUILDING_MIDDLE, 4925, 450],
                  [platforms.BUILDING_MIDDLE, 5000, 450],
                  [platforms.BUILDING_MIDDLE, 5075, 450],
                  [platforms.BUILDING_LEFTSIDE,4850, 525],
                  [platforms.BUILDING_MIDDLE, 4925, 525],
                  [platforms.BUILDING_MIDDLE, 5000, 525],
                  [platforms.BUILDING_MIDDLE, 5075, 525] ]

        #add all platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platformList.add(block)

        #add guards
        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 2500
        guard.rect.y = 355
        guard.boundaryLeft = 2250
        guard.boundaryRight = 2900
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 4000
        guard.rect.y = 205
        guard.boundaryLeft = 3850
        guard.boundaryRight = 4500
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

#create level 2
class Level_02 (Level):

    def __init__ (self, player):

        #parent constructor
        Level.__init__(self,player)

        #create backgrounds and world restrictions
        self.background = pygame.image.load("images/background.png").convert()
        self.background.set_colorkey(constant.BLACK)
        self.levelEnd = -3850
        self.levelBoundary = -15

        #load a transparent png for treasure because it doesn't exist in this level
        self.treasure = pygame.image.load("images/notreasure.png").convert()
        self.treasure.set_colorkey(constant.BLACK)
        
        #create all platforms in level using the platform class-- block type, x, y
        level = [ [platforms.BUILDING_TOP, 0, 550],
                  [platforms.BUILDING_TOP, 75, 550],
                  [platforms.BUILDING_TOP, 150, 550],
                  [platforms.BUILDING_TOP, 225, 550],
                  [platforms.BUILDING_TOP, 300, 550],
                  [platforms.BUILDING_TOP, 375, 550],
                  [platforms.BUILDING_TOP, 450, 550],
                  [platforms.BUILDING_TOP, 525, 550],
                  [platforms.BUILDING_TOP, 600, 550],
                  [platforms.BUILDING_RIGHTCORNER, 675, 550],
                  
                  [platforms.BLOCK_LEFT, 900, 400],
                  [platforms.BLOCK_MIDDLE, 975, 400],
                  [platforms.BLOCK_MIDDLE, 1050, 400],
                  [platforms.BLOCK_MIDDLE, 1125, 400],
                  [platforms.BLOCK_MIDDLE, 1200, 400],
                  [platforms.BLOCK_MIDDLE, 1275, 400],
                  [platforms.BLOCK_MIDDLE, 1350, 400],
                  [platforms.BLOCK_MIDDLE, 1425, 400],
                  [platforms.BLOCK_MIDDLE, 1500, 400],
                  [platforms.BLOCK_MIDDLE, 1575, 400],
                  [platforms.BLOCK_RIGHT, 1650, 400],

                  #on top previous
                  [platforms.BLOCK_LEFT, 1125, 250],
                  [platforms.BLOCK_MIDDLE, 1200, 250],
                  [platforms.BLOCK_MIDDLE, 1275, 250],
                  [platforms.BLOCK_MIDDLE, 1350, 250],
                  [platforms.BLOCK_MIDDLE, 1425, 250],
                  [platforms.BLOCK_RIGHT, 1500, 250],

                  [platforms.BLOCK_LEFT, 1850,300],
                  [platforms.BLOCK_MIDDLE, 1925,300],
                  [platforms.BLOCK_MIDDLE, 2000,300],
                  [platforms.BLOCK_MIDDLE, 2075,300],
                  [platforms.BLOCK_RIGHT, 2150,300],
                  
                  [platforms.BLOCK_LEFT, 2300, 200],
                  [platforms.BLOCK_MIDDLE, 2375,200],
                  [platforms.BLOCK_RIGHT, 2450,200],

                  [platforms.BUILDING_LEFTCORNER, 2500, 450],
                  [platforms.BUILDING_TOP, 2575, 450],
                  [platforms.BUILDING_TOP, 2650, 450],
                  [platforms.BUILDING_TOP, 2725, 450],
                  [platforms.BUILDING_TOP, 2800, 450],
                  [platforms.BUILDING_RIGHTCORNER, 2875, 450],
                  [platforms.BUILDING_LEFTSIDE, 2500, 525],
                  [platforms.BUILDING_MIDDLE, 2575, 525],
                  [platforms.BUILDING_MIDDLE, 2650, 525],
                  [platforms.BUILDING_MIDDLE, 2725, 525],
                  [platforms.BUILDING_MIDDLE, 2800, 525],
                  [platforms.BUILDING_RIGHTSIDE, 2875, 525],          

                  [platforms.BLOCK_LEFT, 3175, 450],
                  [platforms.BLOCK_MIDDLE, 3250, 450],
                  [platforms.BLOCK_MIDDLE, 3325, 450],
                  [platforms.BLOCK_MIDDLE, 3400, 450],
                  [platforms.BLOCK_MIDDLE, 3475, 450],
                  [platforms.BLOCK_RIGHT, 3550, 450],

                  [platforms.BUILDING_LEFTCORNER, 3800, 300],
                  [platforms.BUILDING_TOP, 3875, 300],
                  [platforms.BUILDING_TOP, 3950, 300],
                  [platforms.BUILDING_TOP, 4025, 300],
                  [platforms.BUILDING_TOP, 4100, 300],
                  [platforms.BUILDING_TOP, 4175, 300],
                  [platforms.BUILDING_TOP, 4250, 300],
                  [platforms.BUILDING_TOP, 4325, 300],
                  [platforms.BUILDING_TOP, 4400, 300],
                  [platforms.BUILDING_TOP, 4475, 300],
                  [platforms.BUILDING_RIGHTCORNER, 4550, 300],
                  [platforms.BUILDING_LEFTSIDE, 3800, 375],
                  [platforms.BUILDING_MIDDLE, 3875, 375],
                  [platforms.BUILDING_MIDDLE, 3950, 375],
                  [platforms.BUILDING_MIDDLE, 4025, 375],
                  [platforms.BUILDING_MIDDLE, 4100, 375],
                  [platforms.BUILDING_MIDDLE, 4175, 375],
                  [platforms.BUILDING_MIDDLE, 4250, 375],
                  [platforms.BUILDING_MIDDLE, 4325, 375],
                  [platforms.BUILDING_MIDDLE, 4400, 375],
                  [platforms.BUILDING_MIDDLE, 4475, 375],
                  [platforms.BUILDING_RIGHTSIDE, 4550,375],
                  [platforms.BUILDING_LEFTSIDE, 3800, 450],
                  [platforms.BUILDING_MIDDLE, 3875, 450],
                  [platforms.BUILDING_MIDDLE, 3950, 450],
                  [platforms.BUILDING_MIDDLE, 4025, 450],
                  [platforms.BUILDING_MIDDLE, 4100, 450],
                  [platforms.BUILDING_MIDDLE, 4175, 450],
                  [platforms.BUILDING_MIDDLE, 4250, 450],
                  [platforms.BUILDING_MIDDLE, 4325, 450],
                  [platforms.BUILDING_MIDDLE, 4400, 450],
                  [platforms.BUILDING_MIDDLE, 4475, 450],
                  [platforms.BUILDING_RIGHTSIDE, 4550,450],
                  [platforms.BUILDING_LEFTSIDE, 3800, 525],
                  [platforms.BUILDING_MIDDLE, 3875, 525],
                  [platforms.BUILDING_MIDDLE, 3950, 525],
                  [platforms.BUILDING_MIDDLE, 4025, 525],
                  [platforms.BUILDING_MIDDLE, 4100, 525],
                  [platforms.BUILDING_MIDDLE, 4175, 525],
                  [platforms.BUILDING_MIDDLE, 4250, 525],
                  [platforms.BUILDING_MIDDLE, 4325, 525],
                  [platforms.BUILDING_MIDDLE, 4400, 525],
                  [platforms.BUILDING_MIDDLE, 4475, 525],
                  [platforms.BUILDING_RIGHTSIDE, 4550,525],
                  
                  [platforms.BUILDING_LEFTCORNER, 4850, 300],
                  [platforms.BUILDING_TOP, 4925, 300],
                  [platforms.BUILDING_TOP, 5000, 300],
                  [platforms.BUILDING_TOP, 5075, 300],
                  [platforms.BUILDING_LEFTSIDE,4850, 375],
                  [platforms.BUILDING_MIDDLE, 4925, 375],
                  [platforms.BUILDING_MIDDLE, 5000, 375],
                  [platforms.BUILDING_MIDDLE, 5075, 375],
                  [platforms.BUILDING_LEFTSIDE,4850, 450],
                  [platforms.BUILDING_MIDDLE, 4925, 450],
                  [platforms.BUILDING_MIDDLE, 5000, 450],
                  [platforms.BUILDING_MIDDLE, 5075, 450],
                  [platforms.BUILDING_LEFTSIDE,4850, 525],
                  [platforms.BUILDING_MIDDLE, 4925, 525],
                  [platforms.BUILDING_MIDDLE, 5000, 525],
                  [platforms.BUILDING_MIDDLE, 5075, 525] ]

        #add all platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platformList.add(block)

        #add guards
        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 1250
        guard.rect.y = 305
        guard.boundaryLeft = 900
        guard.boundaryRight = 1600
        guard.VelX = 6
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 2650
        guard.rect.y = 355
        guard.boundaryLeft = 2500
        guard.boundaryRight = 2850
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 4000
        guard.rect.y = 205
        guard.boundaryLeft = 3850
        guard.boundaryRight = 4500
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

#create level 3
class Level_03 (Level):

    def __init__ (self, player):

        #parent constructor
        Level.__init__(self,player)

        #create backgrounds and world restrictions
        self.background = pygame.image.load("images/background.png").convert()
        self.background.set_colorkey(constant.BLACK)
        self.levelEnd = -3850
        self.levelBoundary = -15

        #create treasure that appears at the end of this level
        self.treasure = pygame.image.load("images/treasure.png").convert()
        self.treasure.set_colorkey(constant.BLACK)
        
        #create all platforms in level using the platform class-- block type, x, y
        level = [ [platforms.BUILDING_TOP, 0, 550],
                  [platforms.BUILDING_TOP, 75, 550],
                  [platforms.BUILDING_TOP, 150, 550],
                  [platforms.BUILDING_TOP, 225, 550],
                  [platforms.BUILDING_TOP, 300, 550],
                  [platforms.BUILDING_TOP, 375, 550],
                  [platforms.BUILDING_TOP, 450, 550],
                  [platforms.BUILDING_TOP, 525, 550],
                  [platforms.BUILDING_TOP, 600, 550],
                  [platforms.BUILDING_RIGHTCORNER, 675, 550],

                  [platforms.BLOCK_LEFT, 900,500],
                  [platforms.BLOCK_MIDDLE, 975, 500],
                  [platforms.BLOCK_MIDDLE, 1050, 500],
                  [platforms.BLOCK_MIDDLE, 1125, 500],
                  [platforms.BLOCK_MIDDLE, 1200, 500],
                  [platforms.BLOCK_MIDDLE, 1275, 500],
                  [platforms.BLOCK_MIDDLE, 1350, 425],
                  [platforms.BLOCK_MIDDLE, 1425, 425],
                  [platforms.BLOCK_MIDDLE, 1500, 425],
                  [platforms.BLOCK_MIDDLE, 1575, 425],
                  [platforms.BLOCK_MIDDLE, 1650, 350],
                  [platforms.BLOCK_MIDDLE, 1725, 350],
                  [platforms.BLOCK_RIGHT, 1800, 350],

                  [platforms.BLOCK_LEFT, 1950, 450],
                  [platforms.BLOCK_RIGHT, 2025, 450],

                  [platforms.BLOCK_LEFT, 2150, 300],
                  [platforms.BLOCK_RIGHT, 2225, 300],

                  [platforms.BLOCK_LEFT, 2400, 200],
                  [platforms.BLOCK_MIDDLE, 2475, 200],
                  [platforms.BLOCK_MIDDLE, 2550, 200],
                  [platforms.BLOCK_MIDDLE, 2625, 200],
                  [platforms.BLOCK_MIDDLE, 2700, 200],
                  [platforms.BLOCK_MIDDLE, 2775, 200],
                  [platforms.BLOCK_RIGHT, 2850, 200],

                  [platforms.BLOCK_LEFT, 3000, 450],
                  [platforms.BLOCK_RIGHT, 3075, 450],

                  [platforms.BLOCK_LEFT, 3200, 300],
                  [platforms.BLOCK_RIGHT, 3275, 300],

                  [platforms.BLOCK_LEFT, 3400, 200],
                  [platforms.BLOCK_MIDDLE, 3475, 200],
                  [platforms.BLOCK_MIDDLE, 3550, 200],
                  [platforms.BLOCK_RIGHT, 3625, 200],

                  [platforms.BUILDING_LEFTCORNER, 3800, 300],
                  [platforms.BUILDING_TOP, 3875, 300],
                  [platforms.BUILDING_TOP, 3950, 300],
                  [platforms.BUILDING_TOP, 4025, 300],
                  [platforms.BUILDING_TOP, 4100, 300],
                  [platforms.BUILDING_TOP, 4175, 300],
                  [platforms.BUILDING_TOP, 4250, 300],
                  [platforms.BUILDING_TOP, 4325, 300],
                  [platforms.BUILDING_TOP, 4400, 300],
                  [platforms.BUILDING_TOP, 4475, 300],
                  [platforms.BUILDING_RIGHTCORNER, 4550, 300],
                  [platforms.BUILDING_LEFTSIDE, 3800, 375],
                  [platforms.BUILDING_MIDDLE, 3875, 375],
                  [platforms.BUILDING_MIDDLE, 3950, 375],
                  [platforms.BUILDING_MIDDLE, 4025, 375],
                  [platforms.BUILDING_MIDDLE, 4100, 375],
                  [platforms.BUILDING_MIDDLE, 4175, 375],
                  [platforms.BUILDING_MIDDLE, 4250, 375],
                  [platforms.BUILDING_MIDDLE, 4325, 375],
                  [platforms.BUILDING_MIDDLE, 4400, 375],
                  [platforms.BUILDING_MIDDLE, 4475, 375],
                  [platforms.BUILDING_RIGHTSIDE, 4550,375],
                  [platforms.BUILDING_LEFTSIDE, 3800, 450],
                  [platforms.BUILDING_MIDDLE, 3875, 450],
                  [platforms.BUILDING_MIDDLE, 3950, 450],
                  [platforms.BUILDING_MIDDLE, 4025, 450],
                  [platforms.BUILDING_MIDDLE, 4100, 450],
                  [platforms.BUILDING_MIDDLE, 4175, 450],
                  [platforms.BUILDING_MIDDLE, 4250, 450],
                  [platforms.BUILDING_MIDDLE, 4325, 450],
                  [platforms.BUILDING_MIDDLE, 4400, 450],
                  [platforms.BUILDING_MIDDLE, 4475, 450],
                  [platforms.BUILDING_RIGHTSIDE, 4550,450],
                  [platforms.BUILDING_LEFTSIDE, 3800, 525],
                  [platforms.BUILDING_MIDDLE, 3875, 525],
                  [platforms.BUILDING_MIDDLE, 3950, 525],
                  [platforms.BUILDING_MIDDLE, 4025, 525],
                  [platforms.BUILDING_MIDDLE, 4100, 525],
                  [platforms.BUILDING_MIDDLE, 4175, 525],
                  [platforms.BUILDING_MIDDLE, 4250, 525],
                  [platforms.BUILDING_MIDDLE, 4325, 525],
                  [platforms.BUILDING_MIDDLE, 4400, 525],
                  [platforms.BUILDING_MIDDLE, 4475, 525],
                  [platforms.BUILDING_RIGHTSIDE, 4550,525],
                  
                  [platforms.BUILDING_LEFTCORNER, 4850, 300],
                  [platforms.BUILDING_TOP, 4925, 300],
                  [platforms.BUILDING_TOP, 5000, 300],
                  [platforms.BUILDING_TOP, 5075, 300],
                  [platforms.BUILDING_LEFTSIDE,4850, 375],
                  [platforms.BUILDING_MIDDLE, 4925, 375],
                  [platforms.BUILDING_MIDDLE, 5000, 375],
                  [platforms.BUILDING_MIDDLE, 5075, 375],
                  [platforms.BUILDING_LEFTSIDE,4850, 450],
                  [platforms.BUILDING_MIDDLE, 4925, 450],
                  [platforms.BUILDING_MIDDLE, 5000, 450],
                  [platforms.BUILDING_MIDDLE, 5075, 450],
                  [platforms.BUILDING_LEFTSIDE,4850, 525],
                  [platforms.BUILDING_MIDDLE, 4925, 525],
                  [platforms.BUILDING_MIDDLE, 5000, 525],
                  [platforms.BUILDING_MIDDLE, 5075, 525] ]

        #add all platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platformList.add(block)

        #add guards
        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 1250
        guard.rect.y = 405
        guard.boundaryLeft = 900
        guard.boundaryRight = 1270
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 1450
        guard.rect.y = 330
        guard.boundaryLeft = 1400
        guard.boundaryRight = 1550
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 2650
        guard.rect.y = 105
        guard.boundaryLeft = 2400
        guard.boundaryRight = 2800
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 3900
        guard.rect.y = 205
        guard.boundaryLeft = 3850
        guard.boundaryRight = 4500
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

        guard = enemies.movingMob(enemies.MOB_SPRITE)   
        guard.rect.x = 4500
        guard.rect.y = 205
        guard.boundaryLeft = 3850
        guard.boundaryRight = 4500
        guard.VelX = 2
        guard.player = self.player
        guard.level = self
        self.enemyList.add(guard)

