#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     14/11/2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a=set("")#Initialise set a
b=set("12345") #Initialise set b
option = "" # set "option" to string

def IsEmpty(a): #Define function "IsEmpty"
    if len(a) == 0: # If the length of a is 0 then
        print("Set is empty") # Display "Set is empty"
        return True
    else:# If the length of a is not 0 then
        print("Set not empty") # Display "Set not empty"
        return False

def isize(a): #Define function "isize"
    print(len(a)) #Display size

def difference(a,b):#Define function difference"
    dif = a-b #Set dif to the substraction of a and b
    print(dif) # Print diff

def intersection(a,b):#Define function intersection"
    intersection = a&b #Intersection of a and b
    print(intersection) #Print intersection

def Remove(a):#Define function Remove
    string = input("Pick a number to remove") #Set String to user input
    a.remove(string) #Remove number from user input
    print(a) #Print a
    return a # return a

def Add(a): #Define function Add
    string = input("Pick a number to add")#Set String to user input
    a.add(string) #Add number from user input
    print(a) # Print a
    return a # return a


def menu(option): #Define function menu
    while option != "q": # Loop unitl user types Q
        option = input(""""Menu
        1) Add A string
        2) remove a string
        3) intersection
        4) Difference
        5) Check Size
        6) Check if empty""") #Set Option to user input
        if option == "1": Add(a) # if 1 is pressed call Add (a)
        elif option == "2": Remove(a) # if 2 is pressed call Remove(a)
        elif option == "3": intersection(a,b) # if 3 is pressed call intersection(a,b)
        elif option == "4": difference(a,b) # if 4 is pressed call difference(a,b)
        elif option == "5": isize(a) # if 5 is pressed call isize(a)
        elif option == "6": IsEmpty(a) # if 6 is pressed call is empty(a)

menu(option) #Call menu(option)