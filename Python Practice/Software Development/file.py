#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guest123
#
# Created:     17/02/2018
# Copyright:   (c) Guest123 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------
file = open("testfile.txt","w")

file.write("Hello World.\n")
file.write("This is our new text file,\n")
file.write("and this is another line.\n")
file.write("Why? Because we can\n.")

file.close()

file = open("testfile.txt", "r")
print (file.readline(3))
