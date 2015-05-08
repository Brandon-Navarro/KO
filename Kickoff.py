import pygame, sys, random
from Ball import Ball
from Player import Player
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block
from Opponent import Opponent
pygame.init()

clock = pygame.time.Clock()

width = 1229
height = 577
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("field.png").convert()
bgRect = bgImage.get_rect()

balls = pygame.sprite.Group()
players = pygame.sprite.Group()
opps = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Ball.containers = (all, balls)
Player.containers = (all, players)
BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
Score.containers = (all, hudItems)
Opponent.containers = (all, opps)


run = False

startButton = Button([width/2, height-300], 
                     "images/Buttons/Start Base.png", 
                     "images/Buttons/Start Clicked.png")
                     
                     
                     

while True:
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = True
                    
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        clock.tick(60)
        
    BackGround("field.png")
    
    player = Player([width/6, height/2])
    opps = [Opponent([width/1.5, height/2]), 
            Opponent([width/1.5, height/1.5]), 
            Opponent([width/3, height/.2]), 
            Opponent([width/1.5, height/4]), 
            Opponent([width/1.5, height/.25]), 
            Opponent([width/1.5, height/5])]
    
    level = Level(size, 50)
    level.loadLevel("1")

    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 6

    score = Score([width-80, height-25], "Score: ", 36)
    while run and len(players) == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
                          
        
        
        if timerWait < timerWaitMax:
            timerWait += 1
        else:
            timerWait = 0
            timer.increaseScore(.1)
        
        playersHitBalls = pygame.sprite.groupcollide(players, balls, False, True)
        ballsHitBalls = pygame.sprite.groupcollide(balls, balls, False, False)
        playersHitOpponents = pygame.sprite.groupcollide(players, opps, True, False)


        all.update(width, height, player.rect.center)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    run = False
        
        
        
        
        
        
        
                
        
        
        
