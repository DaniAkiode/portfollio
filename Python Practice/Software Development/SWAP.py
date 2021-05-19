#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guest123
#
# Created:     09/02/2018
# Copyright:   (c) Guest123 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

list = [10, 1, 8, 3, 5]
list[0],list[4] = list[4],list[0]
list[1],list[3] = list[3],list[1]
print(list)