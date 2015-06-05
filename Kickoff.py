import pygame, sys, random
from Wall import Wall
from Tile import Tile
from StartBlock import StartBlock
from EndBlock import EndBlock
from Button import Button
from Level import Level
from BackGround import BackGround
from Player import Player
from HUD import Score
from HUD import Text
from enemy2 import Enemy
pygame.init()

#64.35.192.215

clock = pygame.time.Clock()

width = 731
height = 669
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("field1.png").convert()
bgRect = bgImage.get_rect()

players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
startBlocks = pygame.sprite.Group()
tiles = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
walls = pygame.sprite.Group()
endBlocks = pygame.sprite.Group()
blocks = pygame.sprite.Group()
score = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Tile.containers = (all, tiles)
Player.containers = (all, players)
Enemy.containers = (all, enemies)
StartBlock.containers = (all, startBlocks)
Score.containers = (all, hudItems)
BackGround.containers = (all, backgrounds)
EndBlock.containers = (all, endBlocks)
Wall.containers = (all, walls)




run = False

startButton = Button([width/2, height-300], 
                     "Resources/Objects/Game/Start Base.png", 
                     "Resources/Objects/Game/Start Clicked.png")

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
        
    BackGround("field1.png")
    
    level = Level(size, 30)
    lev = 1
    level.loadLevel(lev)
    for monsterPos in level.monsterList:
        Enemy(monsterPos,[random.randint(-2,2),random.randint(-2,2)])
    player = Player(startBlocks.sprites()[0].rect.center)

    timer = Score([80, height - 25], "Time: ", 36)
    timerWait = 0
    timerWaitMax = 6

    score = Score([width-80, height-25], "Score: ", 36)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
                    print "YAS"
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
                if event.key == pygame.K_k:
                    player.go("juke down")
                if event.key == pygame.K_j:
                    player.go("juke up")
                if event.key == pygame.K_i:
                    player.go("spin up")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
                if event.key == pygame.K_k:
                    player.go("stop juke down")
                if event.key == pygame.K_j:
                    player.go("stop juke up")
                if event.key == pygame.K_i:
                    player.go("stop spin up")
                          
        if timerWait < timerWaitMax:
            timerWait += 1
        else:
            timerWait = 0
            timer.increaseScore(.1)
        
        playersHitenemies = pygame.sprite.groupcollide(players, enemies, True, False)
        playersHitWalls = pygame.sprite.groupcollide(players, walls, False, False)
        playersHitEnds = pygame.sprite.groupcollide(players, endBlocks, False, False)
        enemiesHitWalls = pygame.sprite.groupcollide(enemies, walls, False, False)
        
        for player in playersHitWalls:
            for wall in playersHitWalls[player]:
                player.collideWall(wall)
                
        for enemy in enemiesHitWalls:
            for wall in enemiesHitWalls[enemy]:
                enemy.collideWall(wall)

        for player in playersHitEnds:
            for wall in playersHitEnds[player]:
                for obj in all.sprites():
                    obj.kill()
                all.update(width, height)
                BackGround("field2.png")
                lev += 1
                level.loadLevel(lev)
                for monsterPos in level.monsterList:
                    Enemy(monsterPos)
                player = Player(startBlocks.sprites()[0].rect.center)


        all.update(width, height, player.rect.center)
        
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick()
    run = False
