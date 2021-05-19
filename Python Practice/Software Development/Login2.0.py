#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Guest123
#
# Created:     06/02/2018
# Copyright:   (c) Guest123 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Enter Username
Username = str(input("What is your username "))
#Enter Password
Password = input("What is your password")
#Password is invalid if the pasword length is over 8 characters
if len(Password) > 8  :
    print("password invalid! no more then 8 characters")
#Password valid if the password is less then 8 characters
else:
    print (Username ,"Password valid")
#Enter Username again
NewUsername = str(input("what is your username"))
#Enter Passwaord again
NewPassword = input("What is your password")
#Checks if the New input is the same as the current input
if (NewUsername == Username) and (NewPassword == Password):
    print("Welcome New User")

else:
    print("Sorry Try again")







