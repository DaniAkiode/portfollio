#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     12/01/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#class imports
from MAP import Map #import class 'Map' from MAP module
from SEEKER import Seeker1 #import class 'Seeker1' from SEEKER module
from BALLS import Snitch #import class 'Snitch' from BALLS module

#add in the pygame imports
import random, sys, copy, os, pygame # import random modules
from pygame.locals import * #import python package

#Set Variable to classess
map1 = Map() #Set variable map1 to Map() class
seeker1 = Seeker1("^", 10, 5) #Set variable seeker1 to Seeker1() class as on spite on 10,5 map co-ordinates
seeker2 = Seeker1("*", 10, 15) # Set variable seeker2 to Seeker1() class as on spite on 10,15 map co-ordinates
snitch = Snitch("@", 18 ,10) #Set variable snitch to Seeker1 as on spite on 18,10 map co-ordinates
bludger1 = Snitch("=", 7, 7) #set variable bludger1 class as on spite on 7,7 map co-ordinates
bludger2 = Snitch("=", 14, 14) #Set variable bludger2 class as on spite on 14,14 map co-ordinates


FPS = 30 #Set Frame Per Second to 30
WIDTH = 1000 # Set Width of inteface to 1000
HEIGHT = 700 # Set Width of inteface to 700
HALF_WIDTH = int(WIDTH / 2) #Set variable to half of the width
HALF_HEIGHT = int(HEIGHT / 2) #Set variable to half of the height

TILEWIDTH = 32 #Width of tile is 32 pixels
TILEHEIGHT = 32 #Height of tile is 32 pixels
TILEFLOORHEIGHT = 32 # Floor Height is 32 pixels

#Set Colors
BRIGHTBLUE = (  0, 170, 255) #Set BRIGHTBLUE to color code (  0, 170, 255)
WHITE      = (255, 255, 255) #Set WHITE to color code (255, 255, 255)
BGCOLOR = BRIGHTBLUE #Set variable BGCOLOR to Variable BRIGHTBLUE
TEXTCOLOR = WHITE #Set variable TEXTCOLOR to variable WHTIE

#Assign sprite from file
#Set varible IMGDICT to dicctionary
IMGDICT = { 'grass': pygame.image.load("Images/darkgrass.gif"), #assign 'grass' to grass image from file
            'wall': pygame.image.load("Images/Wall.gif"), #assign 'wall' to wall image from file
            'snitch': pygame.image.load("Images/NewGoldenSnitch.gif"), #assign 'snitch' to snitch image from file
            'seeker1': pygame.image.load("Images/Seeker1G.gif"), #assign 'seeker1' to seeker1 image from file
            'seeker2': pygame.image.load("Images/Seeker2.gif"), #assign 'seeker2' to seeker2 image from file
            'bludger': pygame.image.load("Images/Bludger.gif")} #assign 'bludger' to bludger image from file

#Set sprites to characters
#Set Varible TILEMAPPING to dictionary
TILEMAPPING = { '#':IMGDICT['wall'], # assign '#' to 'wall
                ' ':IMGDICT['grass'], # assign ' ' to 'grass'
                '@':IMGDICT['snitch'], # assign '@' to 'snitch'
                '^':IMGDICT['seeker1'], # assign '^' to 'seeker1'
                '*':IMGDICT['seeker2'], # assign '*' to 'seeker2'
                '=':IMGDICT['bludger']} # assign '=' to 'bludger'



pygame.init() #initialise all imported pygame
FPSCLOCK = pygame.time.Clock() # creates a clock object that can be used to track the time
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT)) #display interface
pygame.display.set_caption('Seekers and Snitches') #Pygame Caption
BASICFONT = pygame.font.Font('freesansbold.ttf', 18) #Font

Seeker1Score = 0 #Set Seeker 1's score to 0
Seeker2Score = 0 #Set Seeker 2's score to 0

Seeker1Moves = 0 #Set Seeker 1's moves to 0
Seeker2Moves = 0 #Set Seeker 2's moves to 0

#This function moves seeker 1 to the left
def MoveSeeker1Left(): #Define MoveSeeker1Left function
    global Seeker1Score, Seeker1Moves #Make Seeker1score and Seeker1Moves global varibals
    #Set X to the position of the seeker1 -1 colum
    x = map1.getCharAtPos(seeker1.getRow(), seeker1.getCol() - 1)
    if x == "#": # if seeker 1 meets the wall
        pass #Wall Collision
    elif x == "*": # if seeker 1 meets seeker 2
        pass #Seeker 2 Collision
    elif x == "=": # if seeker meets blugder
        pass #Bludger collision
    else: #otherwise.....
        if x == "@": # If the seeker catches the snitch
            print("Seeker1 caught the snitch") #display Seeker1has cuaght the snitch
            Seeker1Score +=1 # Add Seeker 1 score by 1
            print("Seeker1:", Seeker1Score)
            seeker1.CatchSnitch() # Calls CatchSnitch Function in the Seeker1 class
            snitch.DeleteSnitch() #Calls DeleteSnitch function in the Seeker1 class
        map1.ClearAtPos(seeker1.getRow(), seeker1.getCol()) #Clears the tile before the move
        seeker1.moveLeft() #moves the seeker to the left
        Seeker1Moves += 1 #Add numbers of moves by 1
        print("Seeker1 Movement:", Seeker1Moves) #display number of moves
        map1.SeekerPos(seeker1.getChar(), seeker1.getRow(), seeker1.getCol()) # Marks new position
    #print (map1.__str__())

    #print (map1.toString())

#This function moves seeker 1 to the Right
def MoveSeeker1Right(): #Call MoveSeeker1Right
    global Seeker1Score, Seeker1Moves#Make Seeker1score and Seeker1Moves global varibals
    x = map1.getCharAtPos(seeker1.getRow(), seeker1.getCol() + 1)  #Set X to the position of the seeker1 +1 colum
    if x == "#": # if seeker 1 meets the wall
        pass #Wall Collision
    elif x == "*": # if seeker 1 meets seeker 2
        pass #Seeker 2 Collision
    elif x == "=": # if seeker meets blugder
        pass #Bludger collision
    else: #otherwise.....
        if x == "@": # If the seeker catches the snitch
            print("Seeker1 caught the snitch") #display Seeker1has cuaght the snitch
            Seeker1Score +=1 # Add Seeker 1 score by 1
            print("Seeker1:", Seeker1Score)
            seeker1.CatchSnitch() # Calls CatchSnitch Function in the Seeker1 class
            snitch.DeleteSnitch() #Calls DeleteSnitch function in the Seeker1 class
        map1.ClearAtPos(seeker1.getRow(), seeker1.getCol()) #Clears the tile before the move
        seeker1.moveRight() #moves the seeker to the right by calling moveRight() function in seeker1 class
        Seeker1Moves += 1 #Adds 1 to Seeker1Moves Variable
        print("Seeker1 Movement:", Seeker1Moves) #displays number of moves
        map1.SeekerPos(seeker1.getChar(), seeker1.getRow(), seeker1.getCol()) #Marks new seeker posistion
    #print (seeker1.toString())
    #print (map1.toString())
#This function moves seeker 1 to the up
def MoveSeeker1Up(): #define MoveSeeker1Up()
    global Seeker1Score, Seeker1Moves #Make Seeker1score and Seeker1Moves global varibals
    x = map1.getCharAtPos(seeker1.getRow() -1 , seeker1.getCol()) #Set x to seeker posistion -1 row
    if x == "#": # if seeker 1 meets the wall
        pass #Wall Collision
    elif x == "*": # if seeker 1 meets seeker 2
        pass #Seeker 2 Collision
    elif x == "=": # if seeker meets blugder
        pass #Bludger collision
    else: #otherwise.....
        if x == "@": #if seeker cataches the snitch
            print("Seeker1 caught the snitch") #display message
            Seeker1Score +=1 # Add 1 to Seeker1Score Variable
            print("Seeker1:", Seeker1Score) # dislpay message
            seeker1.CatchSnitch() # call CatchSnitch() in seeker1 class
            snitch.DeleteSnitch() #call DeleteSnitch() in seeker1 class
        map1.ClearAtPos(seeker1.getRow(), seeker1.getCol()) #Clear posistion next to seeker
        seeker1.moveUp() # moves up
        Seeker1Moves += 1 # Adds 1 to seeker1Moves
        print("Seeker1 Movement:", Seeker1Moves) #Displays message
        map1.SeekerPos(seeker1.getChar(), seeker1.getRow(), seeker1.getCol())
    #print (seeker1.toString())
    #print (map1.toString())
#This function moves seeker 1 to the Down
def MoveSeeker1Down():
    global Seeker1Score, Seeker1Moves
    x = map1.getCharAtPos(seeker1.getRow() +1 , seeker1.getCol()) #Set x to seeker posistion +1 row
    if x == "#": # if seeker 1 meets the wall
        pass #Wall Collision
    elif x == "*": # if seeker 1 meets seeker 2
        pass #Seeker 2 Collision
    elif x == "=": # if seeker meets blugder
        pass #Bludger collision
    else: #otherwise.....
        if x == "@": # if seeker 1 meets wall
            print("Seeker1 caught the snitch") #display message
            Seeker1Score +=1 # Add 1 to Seeker1score
            print("Seeker1:", Seeker1Score) #Display Message
            seeker1.CatchSnitch() #Catch snitch
            snitch.DeleteSnitch() #Deletesnitch
        map1.ClearAtPos(seeker1.getRow(), seeker1.getCol())#clears posistion
        seeker1.moveDown() #moves seeker down
        Seeker1Moves += 1 #Adds one to move count
        print("Seeker1 Movement:", Seeker1Moves) #Display messege
        map1.SeekerPos(seeker1.getChar(), seeker1.getRow(), seeker1.getCol())# New Seeker posistion
    #print (seeker1.toString())
    #print (map1.toString())
#This function moves seeker 2 to the left
def MoveSeeker2Left(): #define MoveSeeker2left function
    global Seeker2Score, Seeker2Moves #Make Seeker2score and Seeker2moves global
    x = map1.getCharAtPos(seeker2.getRow(), seeker2.getCol() - 1) #set x to seeker position -1 column
    if x == "#": #If seeker meest the wall
        pass #wall collision
    elif x == "^": #if seeker2 meets seeker1
        pass #seeker1 collision
    elif x == "=": #if seeker meets bludger
        pass #bludger
    else: #otherwise..
        if x == "@": # if seeker 1 meets wall
            print("Seeker2 caught the snitch") #display message
            Seeker2Score +=1 # Add 1 to Seeker1score
            print("Seeker2:", Seeker2Score) #Display Message
            seeker2.CatchSnitch() #Catch snitch
            snitch.DeleteSnitch() #Deletesnitch
        map1.ClearAtPos(seeker2.getRow(), seeker2.getCol()) #Clear Posistion
        seeker2.moveLeft() #Move left
        Seeker2Moves += 1 #Add one to move count
        print("Seeker2 Movement:", Seeker2Moves) #Display message
        map1.SeekerPos(seeker2.getChar(), seeker2.getRow(), seeker2.getCol()) #NewPosition
    #print (map1.__str__())

    #print (map1.toString())
#This function moves seeker 2 to the right
def MoveSeeker2Right(): #define MoveSeeker2Right function
    global Seeker2Score, Seeker2Moves #Make Seeker2score and Seeker2moves global
    x = map1.getCharAtPos(seeker2.getRow(), seeker2.getCol() + 1) #set x to seeker posision +1 coloumn
    if x == "#": #If seeker meest the wall
        pass #wall collision
    elif x == "^": #if seeker2 meets seeker1
        pass #seeker1 collision
    elif x == "=": #if seeker meets bludger
        pass #bludger
    else: #otherwise..
        if x == "@": # if seeker 1 meets wall
            print("Seeker2 caught thde snitch") #display message
            Seeker2Score +=1 # Add 1 to Seeker1score
            print("Seeker2:", Seeker2Score) #Display Message
            seeker2.CatchSnitch() #Catch snitch
            snitch.DeleteSnitch() #Deletesnitch
        map1.ClearAtPos(seeker2.getRow(), seeker2.getCol()) #clear posisiton
        seeker2.moveRight() #move right
        Seeker2Moves += 1 #add 1 to move count
        print("Seeker2 Movement:", Seeker2Moves) #display movements
        map1.SeekerPos(seeker2.getChar(), seeker2.getRow(), seeker2.getCol()) #New Posistion
    #print (seeker1.toString())
    #print (map1.toString())
#This function moves seeker 2 to the up
def MoveSeeker2Up():
    global Seeker2Score, Seeker2Moves #Make Seeker2score and Seeker2moves global
    x = map1.getCharAtPos(seeker2.getRow() -1 , seeker2.getCol()) #set x to seeker posision -1 column
    if x == "#": #If seeker meest the wall
        pass #wall collision
    elif x == "^": #if seeker2 meets seeker1
        pass #seeker1 collision
    elif x == "=": #if seeker meets bludger
        pass #bludger
    else: #otherwise..
        if x == "@": # if seeker 1 meets wall
            print("Seeker2 caught the snitch") #display message
            Seeker2Score +=1 # Add 1 to Seeker1score
            print("Seeker2:", Seeker2Score) #Display Message
            seeker2.CatchSnitch() #Catch snitch
            snitch.DeleteSnitch() #Deletesnitch
        map1.ClearAtPos(seeker2.getRow(), seeker2.getCol()) #clears posistion
        seeker2.moveUp() #moves up
        Seeker2Moves += 1 #Add 1 to move count
        print("Seeker2 Movement:", Seeker2Moves) #display message
        map1.SeekerPos(seeker2.getChar(), seeker2.getRow(), seeker2.getCol()) #New posistion
    #print (seeker1.toString())
    #print (map1.toString())
#This function moves seeker 2 to the down
def MoveSeeker2Down():
    global Seeker2Score, Seeker2Moves #Make Seeker2score and Seeker2moves global
    x = map1.getCharAtPos(seeker2.getRow() +1 , seeker2.getCol())
    if x == "#": #If seeker meest the wall
        pass #wall collision
    elif x == "^": #if seeker2 meets seeker1
        pass #seeker1 collision
    elif x == "=": #if seeker meets bludger
        pass #bludger
    else: #otherwise..
        if x == "@": # if seeker 1 meets wall
            print("Seeker2 caught the snitch") #display message
            Seeker2Score +=1 # Add 1 to Seeker1score
            print("Seeker2:", Seeker2Score) #Display Message
            seeker2.CatchSnitch() #Catch snitch
            snitch.DeleteSnitch() #Deletesnitch
        map1.ClearAtPos(seeker2.getRow(), seeker2.getCol()) #Clear Position
        seeker2.moveDown()# move down
        Seeker2Moves += 1 #Add 1 to move count
        print("Seeker2 Movement:", Seeker2Moves) #Display message
        map1.SeekerPos(seeker2.getChar(), seeker2.getRow(), seeker2.getCol()) #New posistion
    #print (seeker1.toString())
    #print (map1.toString())

#Main Program
def main(): #define Main Function
    #Global Variables
    global FPSCLOCK, DISPLAYSURF, IMGDICT, TILEMAPPING, BASICFONT
    #Set Positions
    map1.SeekerPos('^', 10,5)
    map1.SeekerPos('*', 10,15)
    #Call draw function
    draw(map1)

    while True:
        #Get controls
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN: #if event is using the keyboard
                if event.key == K_RIGHT: #if key is the right arrow than
                    MoveSeeker1Right() #Call Function
                elif event.key == K_LEFT:#if key is the left arrow than
                    MoveSeeker1Left()#Call Function
                elif event.key == K_UP:#if key is the up arrow than
                    MoveSeeker1Up()#Call Function
                elif event.key == K_DOWN:#if key is the down arrow than
                    MoveSeeker1Down()#Call Function
                elif event.key == K_SPACE:#if key is the space than
                    restart()# Restart Level


                elif event.key == K_a: #If key is the A then
                    MoveSeeker2Left()
                elif event.key == K_w: #If key is the W then
                    MoveSeeker2Up()
                elif event.key == K_d: #If key is the D then
                    MoveSeeker2Right()
                elif event.key == K_s: #If key is the S then
                    MoveSeeker2Down()

            if snitch.getSnitch() == 0: #if get snitch is 0
                map1.changeStatus(True) # Call function
                if map1.getchangedstatus() and map1.getLevel() < 5: #If changed status is true and get level is under 5
                    map1.updateLevel() #Changelevel
                elif map1.getchangedstatus() and map1.getLevel() == 5: #if changed state is true and get level is 5
                    print("Seeker1:", Seeker1Score,"-", Seeker2Score,":Seeker2" ) #display message
                    print("Total Seeker1 moves:", Seeker1Moves) #display message
                    print("Total Seeker2 moves:", Seeker2Moves) #display message
                    if Seeker1Score > Seeker2Score: #if Seeker1's score is larger then seeker2's
                        print("Seeker1 has won") #display message
                    else: #otherwise....
                        print("Seeker2 has won") #display message

                    terminate() # end game
                restart() #restart level
            # Make bludger move if seeker gets to level 4
            if map1.getLevel() >= 4:
                bludger1.Move(map1)
                bludger2.Move(map1)

            #If get level is 5 then the snitch should move
            if map1.getLevel() == 5:
                snitch.Move(map1)


            MapNeedsReDraw = True #Set MapNeeedsReDraw to true
        #Redraw map
        DISPLAYSURF.fill(BGCOLOR) #fill background color
        if MapNeedsReDraw: #If map needs to be ReDrawn
            mapSurf = draw(map1) #Call draw function
            MapNeedsReDraw = False #Set variable to false

        mapSurfRect = mapSurf.get_rect() #Get the Rect.
        mapSurfRect.center = (HALF_WIDTH, HALF_HEIGHT) #Set to center

        DISPLAYSURF.blit(mapSurf, mapSurfRect) #draw images on the surface

        pygame.display.update() #Update interface
        FPSCLOCK.tick()

#Draws map
def draw(map1):
    mapSurfWidth = map1.getWidth() * TILEWIDTH #Set the width of the surface
    mapSurfHeight = map1.getHeight() * TILEHEIGHT #Set the height of the surface
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight)) #creates surface
    mapSurf.fill(BGCOLOR) #Background Color

    for h in range(map1.getHeight()): #For loop for height
        for w in range(map1.getWidth()): #for loop for width
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT)) #place tiles on surface
            if map1.getCharAtPos(h, w) in TILEMAPPING: #If characters are in the mapping
                baseTile = TILEMAPPING[map1.getCharAtPos(h,w)] #Place character tiles
            mapSurf.blit(baseTile, thisTile) #draw images

    return mapSurf

def restart(): #define restart()
    # Assign levels in dictionary
    levels = {1:map1.__init__, 2:map1.gotoLevel2, 3:map1.gotoLevel3, 4:map1.gotoLevel4, 5:map1.gotoLevel5}
    #Assign posistions
    seeker1.setRow(10)
    seeker1.setCol(5)
    seeker2.setRow(10)
    seeker2.setCol(15)
    snitch.AddSnitch() #Adds the snitch everytime the level restart
    levels[map1.getLevel()]() #Stores lest of levels
    map1.changeStatus(False) #Calls changeStatus function in Map class
    map1.SeekerPos(seeker1.getChar(), seeker1.getRow(), seeker1.getCol()) #Seeker 1 posistion
    map1.SeekerPos(seeker2.getChar(), seeker2.getRow(), seeker2.getCol()) #Seeker 2 posistion
    draw(map1)#Draw Map

#This function ends the game
def terminate():
    #shutdown routine
    pygame.quit()
    sys.exit()

#exception handler
try:
    import pygame

except ModuleNotFoundError:
    print("Program not found")


if __name__ == '__main__':
    main()












