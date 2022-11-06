#Tori Wu
#June 10, 2019
#NEO-HEIST/MAIN.py
#main program that puts together every other class and starts game

#reference/base for game: http://programarcadegames.com/python_examples/en/sprite_sheets/
#used pygame's sprite class: https://www.pygame.org/docs/ref/sprite.html

import pygame
import constant

import levels
from player import Player

#-------menu functions for loading screens-------#
def loadTitle():
    title = pygame.image.load("images/titlemenu.png").convert()
    screen.blit(title,(0,0))
    pygame.display.update()

def loadInstructions():
    howToPlay = pygame.image.load("images/Howtoplay.png").convert()
    screen.blit(howToPlay,(0,0))
    pygame.display.update()

def loadGameOver():
    gameOver = pygame.image.load("images/gameover.png").convert()
    screen.blit(gameOver,(0,0))
    pygame.display.update()

def loadWinScreen():
    winScreen = pygame.image.load("images/missionaccomplished.png").convert()
    screen.blit(winScreen, (0,0))
    pygame.display.update()

#------------------------------#
#       MAIN PROGRAM           #
#------------------------------#

pygame.init()

#create scren and window caption
screen = pygame.display.set_mode((constant.WIDTH,constant.HEIGHT))
pygame.display.set_caption("NEO-HEIST")

#music 
pygame.mixer.music.load('sounds/Defense Line.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

#--------starting menus--------#
inMenu = True
startGame = True
menuScreen = 0 #keeps track of which screen should show

while inMenu:

    #load main menu screen
    if menuScreen == 0:
        loadTitle()

        #get mouse position
        mousePos = pygame.mouse.get_pos() #0=x, 1=y

        #user input (mouse and escape key)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    #quit
                    inMenu = False
                    startGame = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mousePos[0]<=545 and mousePos[0]>=240:
                    if mousePos[1]<=350 and mousePos[1]>=280: #play
                        inMenu=False
                    elif mousePos[1]<=445 and mousePos[1]>=370: #how to play
                        menuScreen = 1
                    elif mousePos[1]<= 535 and mousePos[1]>= 465: #quit                 
                        startGame = False
                        inMenu = False

    #load how to play screen     
    elif menuScreen == 1:
        loadInstructions()

        #get mouse position
        mousePos = pygame.mouse.get_pos() #0=x, 1=y

        #user input (mouse and escape key)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #quit
                    inMenu = False
                    startGame = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mousePos[0]>=70 and mousePos[0]<=355: #back to menu
                    if mousePos[1]<=590 and mousePos[1]>=530:   
                        menuScreen=0

#-------game specifics--------#
if startGame == False:
    pygame.quit()

else:
    #create player
    player = Player()

    #load levels into a list containing all levels
    levelList = []
    levelList.append(levels.Level_01(player))
    levelList.append(levels.Level_02(player))
    levelList.append(levels.Level_03(player))

    #set current level
    levelNum = 0 #starts at level 1
    currentLevel = levelList[levelNum]

    #create an updatable sprite list/group for the player 
    activeSpriteList = pygame.sprite.Group()

    #appends all platforms player can touch into the level list in the player class
    player.level = currentLevel

    #set starting position of player
    player.rect.x = 150
    player.rect.y = 350
    activeSpriteList.add(player) 

    #loop game until finished or exit
    done = False

    #game over or win
    gameOver = False
    playerWin = False

    #timer to manage how fast screen updates
    clock = pygame.time.Clock()

    #--------GAME START--------#

    while not done:
                
        #check if player has died
        if player.rect.y + 238 >= constant.HEIGHT:
            gameOver = True

        #check to see if player is caught by a guard
        guardHitList = pygame.sprite.spritecollide (player,player.level.enemyList, False)
        #if yes, gameover
        for guard in guardHitList:
            gameOver = True

        #when player loses, load game over screen
        if gameOver:
            loadGameOver()
            while gameOver:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE: #quit
                            gameOver = False
                            done = True
                        if event.key == pygame.K_SPACE: #retry
                            gameOver = False
                            #reset player position to place before the fell/got caught
                            player.rect.x = 50
                            player.rect.y = 0
                            currentLevel.moveWorld(200)

        #player input during game (moves or stops player)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_LEFT:
                    player.goLeft()
                elif event.key == pygame.K_RIGHT:
                    player.goRight()
                elif event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.playerVelX < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.playerVelX > 0:
                    player.stop()

        #updates player
        activeSpriteList.update()

        #update level items
        currentLevel.update()

        #moves world left (-x) if player gets near the right side
        if player.rect.x >= 500:
            difference = player.rect.x - 500
            player.rect.x = 500
            currentLevel.moveWorld(-difference)

        #moves world right (+x) if player gets near the left side
        if player.rect.x <=120:
            difference = 120 - player.rect.x
            player.rect.x = 120
            currentLevel.moveWorld(difference)

        #gets player's current X position
        currentPos = player.rect.x + currentLevel.worldShift
        
        #check if player is at the start of the map (cannot pass)
        if currentPos <= currentLevel.levelBoundary and currentLevel.worldShift>=0:
            player.rect.x = currentLevel.levelBoundary
        
        #check if player has reached the end of the level
        if currentPos < currentLevel.levelEnd:
            #check if player has won
            if levelNum == 2:
                playerWin = True
                #if player has won, show mission accomplished screen
                loadWinScreen()
                while playerWin:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                playerWin = False
                                done = True
                                
            #if they have not won, continue to the next level
            else:
                #starting position
                player.rect.x = 300
                player.rect.y = 350
                #change level
                if levelNum <len(levelList)-1:
                    levelNum += 1
                    currentLevel = levelList[levelNum]
                    player.level = currentLevel
                
        #draw everything
        currentLevel.draw(screen)
        activeSpriteList.draw(screen)

        #display current level on top left corner
        font = pygame.font.SysFont("System", 40)
        levelCounter = font.render("Level: " + str(levelNum+1), 1, constant.WHITE)
        screen.blit(levelCounter, (25,25))

        #30 frames per second
        clock.tick(constant.FPS)

        #update screen
        pygame.display.flip()

    pygame.quit()
