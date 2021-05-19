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

Evens = 0
Odds = 0

Number = int(input("Enter a value or 0 to stop: "))

while Number !=0:
    if Number % 2==1:
        Odds += 1

    else:
        Evens += 1

    Number = int(input("Enter a value or 0 to stop:"))

print("Even number:",Evens)
print("Odds number:",Odds)