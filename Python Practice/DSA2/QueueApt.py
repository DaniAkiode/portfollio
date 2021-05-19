#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     14/11/2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
queue=[] #initalise queue

def Size(queue): #Define size function
    print("Number of items in the queue is", len(queue)) #Display length of queue

def IsEmpty(queue): #Define IsEmpty

    if len(queue) == 0: #if length is 0 then
        print ("Queue is empty") # print message
        return True
    else:
        print ("Queue is not empty")# print message
        return False

def Pop(queue): #define Pp[
    if IsEmpty(queue) == True: # if Istmpy function is true
        print("Empty Queue") # Display message
    else:
        value = queue.pop(0) #Delete first value
        print("Value removed", value) #display message

def Push(queue): #define Push
    queue.append(input("What value do you want to add")) #Add value
    print(queue)# Display message

def menu():# Define Menu
    option = "" #Set option to string
    while option != "q": # Loop unitl user types Q
        option = input(""""Menu
        1) To Push Value
        2) To Pop Value
        3) To Check if List is empty
        4) To Check the size """) #User input
        if option == "1": Push(queue) #Call Push
        elif option == "2": Pop(queue) #Call Pop
        elif option == "3": IsEmpty(queue) # Call IsEmpty
        elif option == "4": Size(queue) # Call Size
menu() # Call Menu