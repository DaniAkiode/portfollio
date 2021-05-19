#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniel Akiode
#
# Created:     02/03/2018
# Copyright:   (c) Daniel Akiode 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def CheckNumbers(NewUser): #Checks for numbers in the username
    number = ['1','2','3','4','5','6','7','8','9'] # stores array of numbers between 1-9
    for i in range(len(number)): #Checks for numbers in variable NewUser
        if number[i] in NewUser: #If numbers 1-9 are in the varible then
            print ("Username is Strong")#display message
            return NewUser #return new data

        elif number[i] not in NewUser: #if numbers between 1-9 is not in the variable then
            print("Username is Weak")#print message
            NewUser= input("Create New Login name") #Prompt user input


def CheckLength(NewPassW): #Checks for length in password
    while len(NewPassW) < 8: #Checks if the password length is less the 8
        print("Password is too short") #Displays message
        NewPassW = input("Create New Password") # prompts user input


    print("password is strong") #Display Message

    return NewPassW #return new variable


def NewU(): #This Function creates new accounts for user
    NewUser= input("Create New Login name")#Prompt users to create a username
    NewUser = CheckNumbers(NewUser)#calls CheckNumbers function
    if NewUser in users: #checks if NewUser data is in the isers directory
        print("Username has been taken") #displays message
    else: #if the NewUser data is not in the user directory
        NewPassW = input("Create New Password") #Prompts user to create a password
        NewPassW = CheckLength(NewPassW) #Calls CheckLength function with passing parameter NewPassW
        details(NewUser,NewPassW) #calls details function with passing parameter NewUser and NewPassW
        print("Your Account has been created! Welcome", NewUser) #Print Message


def OldU():#This function prompt the user to log into their account
    user = input("Enter Your Username") #Prompts user to type in their username
    passW = input("Enter Your Password") #Prompt user to type in their password

    for line in open("LoginData.txt","r").readlines(): #Opens and reads files line by line
        LogData = line.split() #splits the string into two so it reads to lines
        if user == LogData[0] and passW ==LogData[1]: #Combines the first and second lines
            print("You are logged in") #Displays Message


def details(NewUser,NewPassW): #Stores usernames and passwords
    Login = open("LoginData.txt","a+") # Creates or opens LoginData.txt file
    Login.write(NewUser) #Writes data for new username
    Login.write(" ") #Creats a space between username and passwoed
    Login.write(NewPassW)#writes data for new password
    Login.write("\n") #creates new line
    Login.close #closes file

users = {} #User Dictionary
option = "" #Define global variable "Option"


while option != "Q": #Checks to make sure that Q has not been pressed

    option = input("Do you have an account? Type 'Y' or 'N', Q for quit ") #Prompt user to type in Y , N or Q

    if option == "Y": #Checks if Y has been typed
        OldU() #calls OldU Function
    elif option == "N": #Checks if N has been pressed
        NewU() # calls NewU Function



