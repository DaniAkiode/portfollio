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

Username = str(input("What is your username "))
Password = input("What is your password")

if len(Password) > 8  :
    print("password invalid! no more then 8 characters")

else:
    print (Username ,"Password valid")

NewUsername = str(input("what is your username"))
NewPassword = input("What is your password")

if (NewUsername == Username) and (NewPassword == Password):
    print("Welcome New User")

else:
    print("Sorry Try again")







