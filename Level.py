import pygame, sys, math

from Wall import Wall
from Tile import Tile
from StartBlock import StartBlock
from EndBlock import EndBlock


class Level():
    def __init__(self, screenSize, blockSize = 30):
        self.screenSize = screenSize
        self.blockSize = blockSize
        self.level = ""
        self.monsterList = []
        
    def loadLevel(self, level):
        self.level = level
        levelFile = "Resources/Maps/level" + str(level) + ".lvl"
        self.monsterList = []

        f = open(levelFile, "r")
        lines = f.readlines()
        f.close()
        
        newlines = []
        
        for line in lines:
            newline = ""
            for c in line:
                if c != "\n":
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == " ":
                    Tile([x*self.blockSize,y*self.blockSize])
                if c == "#":
                    Wall([x*self.blockSize,y*self.blockSize])
                if c == "s":
                    StartBlock([x*self.blockSize,y*self.blockSize])
                if c == "e":
                    EndBlock([x*self.blockSize,y*self.blockSize])
                if c == "m":
                    Tile([x*self.blockSize,y*self.blockSize])
                    self.monsterList += [[x*self.blockSize,y*self.blockSize]]
