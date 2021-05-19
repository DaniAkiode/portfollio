#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guest123
#
# Created:     08/02/2018
# Copyright:   (c) Guest123 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

numbers = [10, 5, 7, 2, 1]
numbers[0] = 111
numbers[1] = numbers[4]

numbers.append(4)
numbers.insert(0,222)
numbers.insert(1,333)
print(len(numbers))
print(numbers)