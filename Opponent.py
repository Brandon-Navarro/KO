import pygame,math,random
from Ball import Ball


class Opponent(Ball):
    def __init__(self, pos):
        Ball.__init__(self, "images/Ball/ball.png", [0,0], pos)
        self.upImages = [pygame.image.load("images/Ball/ball.png"), pygame.image.load("images/Ball/ball.png")]
        self.downImages = [pygame.image.load("images/Ball/ball.png"), pygame.image.load("images/Ball/ball.png")]
        self.leftImages = [pygame.image.load("images/Ball/ball.png"), pygame.image.load("images/Ball/ball.png")]
        self.rightImages = [pygame.image.load("images/Ball/ball.png"), pygame.image.load("images/Ball/ball.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 2.8
        self.kind = "zombie"

        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        Ball.update(self, width, height)
        self.animate()
        self.facePlayer(playerPos)
        self.changed = False
        
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
                #print "hit xWall"
    
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
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False


