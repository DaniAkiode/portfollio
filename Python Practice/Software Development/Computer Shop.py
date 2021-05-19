#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guest123
#
# Created:     06/02/2018
# Copyright:   (c) Guest123 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
name = input("What is your name")
student = input("are you a student?")


if student == "yes" or "Yes":
    scard = input("do you have a student card ")
    if scard == "yes" or "Yes":
        print("Congrats" , name , "You can get a discount")

    else:
        print("Sorry, you can't have a discount")
else:
   print("Sorry, you can't have a discount")
