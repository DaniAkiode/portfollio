#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     19/12/2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import collections

contactsBook = collections.OrderedDict()


def AddEntry(FirstName, Address, contactsBook):
    FirstName = input("What is your first name?")
    if FirstName in contactsBook:
        print(contactsBook)
        print(FirstName, "Already Exists")
    else:
        Address = input("What is your Address")
        contactsBook[FirstName] = Address
        for k, v in contactsBook.items():
            print (k,v)
        return contactsBook


def FindAddress(contactsBook,FirstName):
    FirstName = input("What is your name")
    if FirstName in contactsBook:
        print(contactsBook[FirstName])
    else:
        print("Name not found")


def DeleteCurrentEntry(contactsBook):
    Name = input("Pick A Name")
    if Name in contactsBook:
        del contactsBook[Name]
        print(Name, "has been deleted")
    else:
        print("Name is not in dictionary ")

def ClearAllEntry(contactsBook):
    contactsBook.clear()
    print(contactsBook)
    print("Book cleared")
    return contactsBook

def ListAll(FirstName, Address, contactsBook):
    contactsBook[FirstName] = Address
    for k, v in contactsBook.items():
        print (k,v)

FirstName = ""
Address = ""
option = ""
while option != "q":
    option = input("""What do you want
                    a. Add Entry
                    b. Find Address
                    c. Delete Current Entry
                    d. Clears All Entry
                    e. List All
                    q. Quit""")
    if option == "a": AddEntry(FirstName, Address, contactsBook)
    elif option == "b": FindAddress(contactsBook, FirstName)
    elif option == "c": DeleteCurrentEntry(contactsBook)
    elif option == "d": ClearAllEntry(contactsBook)
    elif option == "e": ListAll(FirstName, Address, contactsBook)

