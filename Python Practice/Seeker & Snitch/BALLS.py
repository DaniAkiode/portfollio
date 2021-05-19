#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     06/02/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Import randomizer
import random
#Ball Class
class PlayBall:
    #Initalise variables
    def __init__(self, x, r, c):
        self.char = x
        self.row = r
        self.col = c
    #Return Row
    def getRow(self):
        return self.row
    #Return Column
    def getCol(self):
        return self.col
    #Return Character
    def getChar(self):
        return self.char
    #Set row to r
    def setRow(self, r):
        self.row = r
    #Set Column to C
    def setCol(self, c):
        self.col = c

#Snitch class inherited from ball class
class Snitch(PlayBall):
    #Initalise variables
    def __init__(self, x, r, c):
        #inherited varibales
        super().__init__(x, r, c)
        self.Snitch = 1
    #Add snitch
    def AddSnitch(self):
        self.Snitch += 1
    #Delete snitch
    def DeleteSnitch(self):
        self.Snitch -= 1
    #Return Snitch
    def getSnitch(self):
        return self.Snitch
    #Move Function
    def Move(self, map1):
        #Object randomly move left and right
        rrow = random.randint(-1,1)
        #Object randomly move up and down
        rcol = random.randint(-1,1)
        #Marks Posistion
        map1.SeekerPos(self.getChar(), self.getRow(), self.getCol())
        # If the next posistion is a seeker, bludger, snitch or wall the it would collide
        if map1.getCharAtPos(self.getRow()+rrow, self.getCol()+rcol) in ["^", "=", "@", "#", "*"]:
            pass
        else:
            #Clear posistion for object
            map1.ClearAtPos(self.getRow(), self.getCol())
            self.setRow(self.getRow() + rrow)
            self.setCol (self.getCol() + rcol)
            map1.SeekerPos(self.getChar(), self.getRow(), self.getCol())

