#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     28/11/2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#Defineing the class that will create the nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Defiining the class that will create the linked stack
class LinkedStack:
    def __init__(self):
        self.top = None

#Defining function that checks if the stack is empty
    def IsEmpty (self):
        if self.top is None:
            print("Stack is empty")
            return True
        else:
            print("Stack is not empty ")
            return False

#Defining function that push the data into the stack
    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.top
        self.top = NewNode
        print (str(data), "Data pushed to the stack")


#Defining function that pops the data out of the stack
    def pop(self):
        if self.IsEmpty():
            print("Stack is empty")
        else:
            popped = self.top.data
            self.top = self.top.next
            print (str(popped), "Data poped out of stack")
            return popped
    def DisplayStack(self):
        value = self.top
        while value != None:
            print(value.data)
            value = value.next
    def NumberOfItems(self):
        tempo = self.top
        items = 0
        while (tempo):
            items += 1
            tempo = tempo.next
        print("Number of items in the stack are:", items)
        return items


#Main Program
stack = LinkedStack()
while True:
    opt = int(input("""Please select an option
                    1. Check if empty
                    2. Push
                    3. Pop
                    4. Display Stack
                    5. Number Of items
                    6. Quit"""))
    if opt == 1:
        stack.IsEmpty()
    elif opt == 2:
        data = int(input("Pick a number"))
        stack.push(data)
    elif opt == 3:
        popped = stack.pop()
    elif opt == 4:
        stack.DisplayStack()
    elif opt == 5:
        stack.NumberOfItems()
    elif opt == 6:
        break




