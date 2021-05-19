#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guest123
#
# Created:     13/02/2018
# Copyright:   (c) Guest123 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Functions
def CheckLength (password):
        while len(Password) > 8  :
            if len(Password) > 8  :
                print("password invalid! no more then 8 characters")

                Password = input("What is your password")

            else:
                print (Username ,"Password valid")

        return password


def Checkusername (Username):
     Username = str(input("Conform username"))



def checkpassword ():


#-------------------------------------------------------------------------------

#Intorduction

Register = input("do you want to register? ")
while Register != "x":
    if Register == "yes" or "Yes" or "Y" or "y" or "YES":

        Username = str(input("What is your username"))

        Password = input("What is your password")


        CheckLength(Password) :


        NewUsername = str(input("what is your username"))

        NewPassword = input("What is your password")

        if (NewUsername == Username) and (NewPassword == Password):
            print("Welcome New User")

        else:
            print("Sorry Try again")

    if Register == "No" or "no" or "N" or "n" or "NO" :
        login = input("Do you have an account")
        if login == "yes" or "Yes" or "Y" or "y" or "YES":
            LoginUsername = str(input("What is your Username"))
            LoginPassword = str(input("What is your password"))
            if (LoginUsername == NewUsername) and (LoginPassword == NewPassword):
                print("You have logged in")

            else:
                print("Login details Invalid")

        if login == "No" or "no" or "N" or "n" or "NO" :
            print("Thank you for using out program")

    else:
        print("input invalid")

    Register = input("do you want to register")
