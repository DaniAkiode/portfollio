#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guest123
#
# Created:     27/02/2018
# Copyright:   (c) Guest123 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

users = {} #User Dictionary
option = "" #Define global variable "Option"

def CheckNumbers(NewUser):
    number = ['1','2','3','4','5','6','7','8','9']
    for i in range(len(number)):
        if number[i] in NewUser:
            print ("Username is Strong")
            return NewUser

        elif number[i] not in NewUser:
            print("Username is Weak")
            NewUser= input("Create New Login name")


def CheckLength(NewPassW):
    while len(NewPassW) < 8:
        print("Password is too short")
        NewPassW = input("Create New Password")


    print("password is strong")

    return NewPassW


def NewU():
    NewUser= input("Create New Login name")
    NewUser = CheckNumbers(NewUser)
    if NewUser in users:
        print("Username has been taken")
    else:
        NewPassW = input("Create New Password")
        NewPassW = CheckLength(NewPassW)
        details(NewUser,NewPassW)
        print("Your Account has been created! Welcome", NewUser)


def OldU():
    user = input("Enter Your Username")
    passW = input("Enter Your Password")

    for line in open("LoginData.txt","r").readlines():
        LogData = line.split()
        if user == LogData[0] and passW ==LogData[1]:
            print("You are logged in")
            Menu()
    print("Incorrect")





def Menu():
    option = input("Do you have an account? Type 'Y' or 'N', Q for quit ")

    if option == "Y":
        OldU()
    elif option == "N":
        NewU()



def details(NewUser,NewPassW):
    Login = open("LoginData.txt","a+")
    Login.write(NewUser)
    Login.write(" ")
    Login.write(NewPassW)
    Login.write("\n")
    Login.close


while option != "Q":
    Menu()




