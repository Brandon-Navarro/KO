import pygame,math,random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, speed=[1,1]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages =    [pygame.image.load("Resources/Objects/Enemy/up1.png")]

        self.leftImages =  [pygame.image.load("Resources/Objects/Enemy/left1.png")]

        self.rightImages = [pygame.image.load("Resources/Objects/Enemy/right1.png")]

        self.downImages =  [pygame.image.load("Resources/Objects/Enemy/down1.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = 3
        self.kind = "zombie"
        self.speedx = speed[0]
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.animate()
        self.move()
        self.facePlayer(playerPos)
        self.changed = False
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
        self.move()
        
    def collideWall(self, other):
        #print "hitting"
        if self.rect.right < other.rect.left or self.rect.left > other.rect.right:
            self.speedx = 0
            self.didBounceX = True
        if self.rect.top < self.rect.bottom or self.rect.bottom > other.rect.top:
            self.speedy = 0
            self.didBounceY = True
        
        
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]


