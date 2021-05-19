#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guest123
#
# Created:     07/02/2018
# Copyright:   (c) Guest123 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

max = -999999999
counter = 0
number = int(input("Enter a value: "))

while number != -1:

    if number == -1:
        continue
    counter += 1

    if number > max:
        max = number
if counter:
    print("The largest number is", max )
else:
    print ("Are you Kidding me? You haven't entered any value!")