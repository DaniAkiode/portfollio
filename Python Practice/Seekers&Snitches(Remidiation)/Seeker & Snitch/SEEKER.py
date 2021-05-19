#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     09/01/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Seeker Class
class Seeker1:
    #Initalise variables
    def __init__(self, x, r, c):

        self.char = x
        self.row = r
        self.col = c
        self.snitch = 0
    #Displays text
    def toString():
        info = "Seeker" + self.char + "At row " + str(self.row) + " and column " + str(self.col)
        info = info + " has caught " + str(self.snitch) + " snitch today."
        return info
    #Returns row
    def getRow(self):
        return self.row
    #Returns column
    def getCol(self):
        return self.col
    #Returns Character
    def getChar(self):
        return self.char
    #Returns snitch
    def getSnitch(self):
        return self.snitch
    #Sets the row to r
    def setRow(self, r):
        self.row = r
    #Sets the Coloumn to c
    def setCol(self, c):
        self.col = c
    #Allows seeker to move left
    def moveLeft(self):
        self.col -= 1
    #Allows seeker to move right
    def moveRight(self):
        self.col += 1
    #Allows seeker to move Up
    def moveUp(self):
        self.row -= 1
    #Allows seeker to move down
    def moveDown(self):
        self.row += 1
    #Allow seeker to catch snitch
    def CatchSnitch(self):
        self.snitch += 1