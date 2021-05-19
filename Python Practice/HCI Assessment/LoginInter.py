#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     11/12/2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import os
import re
import datetime
import random

temp = 'tempfile.txt'



def time():
    localtime = datetime.datetime.now()
    localtime = localtime.replace(second=0, microsecond=0)
    t = Tk()
    t.title()
    t.configure(bg = 'Dark Blue')
    t.geometry('150x50')
    tlbl = Label(t, text=str(localtime))
    tlbl.configure(fg = 'Yellow')
    tlbl.configure(bg = 'Dark Blue')
    tlbl.pack()
    t.mainloop


def Randomize(r):
    r = random.randint(1000,9999)
    return r


def GeneratePassword():

    r1 = 0
    r2 = 0

    r1 = Randomize(r1)
    r2 = Randomize(r2)

    passE1.delete(0, END)
    passE1.insert(0, r1)

    passE2.delete(0, END)
    passE2.insert(0, r2)

    print(str(r1) + str(r2))



def SignUp():
    global passE1
    global passE2
    global userE
    global roots

    roots = Tk()
    roots.title('SignUp')
    roots.configure(background='Dark Blue')
    intruction = Label(roots, text="""Enter new username.
                            Enter 4 numbers in 1 boxes and the other for in the other box
                            or click "Generate Password
                            The password should be 8 numbers only no more or no less """)
    intruction.grid(row=0, column=0, sticky=E)
    intruction.configure(fg = 'Yellow')
    intruction.configure(bg = 'Dark Blue')


    userL = Label(roots, text ='New Username:')
    passL = Label(roots, text ='New Password:')
    userL.grid(row=1, column=0, sticky=W)
    passL.grid(row=2, column=0, sticky=W)
    userL.configure(fg = 'Yellow')
    userL.configure(bg = 'Dark Blue')
    passL.configure(fg = 'Yellow')
    passL.configure(bg = 'Dark Blue')


    userE = Entry(roots)
    passE1 = Entry(roots)
    passE2 = Entry(roots)


    userE.grid(row=1, column=1)
    passE1.grid(row=2, column=1)
    passE2.grid(row=3, column=1)

    Rand = Button(roots, text='Generate Password', command=GeneratePassword)
    Rand.grid(columnspan=3, row = 5, sticky=W)

    signupButton = Button(roots, text='SignUp', command=FSSignUp)
    signupButton.grid(columnspan=2, row= 5, sticky=E)
    roots.mainloop()

def FSSignUp():

    with open(temp, 'a') as f:

        clock = datetime.datetime.now()
        clock = clock.replace(second=0, microsecond=0)

        f.write(str(clock))
        f.write('#l#')
        f.write(userE.get())
        f.write('#p#')
        f.write(passE1.get())
        f.write(passE2.get())
        f.write('#e#')
        f.write('\n')
        f.close()
    roots.destroy()
    Login()

def Login():

    global userEL
    global passEL
    global root1

    root1 = Tk()
    root1.title('Login')
    root1.configure(background='Dark Blue')

    intruction = Label(root1, text="""Enter your username and passwords then click 'Log-in' \n
                                      If you have not made an account yet then click 'Sign-Up' \n
                                      If you want to check the time then click on 'Time'  """)
    intruction.grid(sticky=E)
    intruction.configure(fg = 'Yellow')
    intruction.configure(bg = 'Dark Blue')

    userL = Label(root1, text='Username: ')
    passL = Label(root1, text='Password: ')
    userL.grid(row=1, sticky=W)
    passL.grid(row=2, sticky=W)
    userL.configure(fg = 'Yellow')
    userL.configure(bg = 'Dark Blue')
    passL.configure(fg = 'Yellow')
    passL.configure(bg = 'Dark Blue')


    userEL = Entry(root1)
    passEL = Entry(root1, show='*')
    userEL.grid(row=1, column=1)
    passEL.grid(row=2, column=1)

    loginB = Button(root1, text='Login', command=CheckLogin)
    loginB.grid(columnspan=2, sticky=W)

    signupButton = Button(root1, text='SignUp', command=NewSignUp)
    signupButton.grid(columnspan=2, sticky=W)

    TimeButton = Button(root1, text='Time', command=time)
    TimeButton.grid(columnspan=2, sticky=W)

    Exit = Button(root1, text='Quit', fg='red', command=Quit)
    Exit.grid(columnspan=2, sticky=W)
    root1.mainloop()

def NewSignUp():
    root1.destroy()
    SignUp()

def CheckLogin():
   with open(temp) as f:
    #for line in open(temp,"r").readlines():
        #data = f.readlines()
        LD = f.read()
        passw = re.findall("#p#(.*?)#e#", LD)
        usern = re.findall("#l#(.*?)#p#", LD)

   lead = 0
   RealName = False

   for i in usern:
        if userEL.get() == i:
            RealName = True
            break
        else:
            lead += 1

   #print(usern)
   #print(passw)

   if RealName == True and passEL.get() == passw[lead]:
        r = Tk()
        r.title(':D')
        r.configure(bg = 'Dark Blue')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[+] Logged In')
        rlbl.configure(fg = 'Yellow')
        rlbl.configure(bg = 'Dark Blue')
        rlbl.pack()
        r.mainloop()
   else:
        r = Tk()
        r.title('D:')
        r.configure(bg = 'Dark Blue')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[+] Access Denied')
        rlbl.configure(fg = 'Yellow')
        rlbl.configure(bg = 'Dark Blue')
        rlbl.pack()
        r.mainloop()

def Quit():
    root1.destroy()


if os.path.isfile(temp):
    Login()
else:
    SignUp()





