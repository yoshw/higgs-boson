# This Python file uses the following encoding: utf-8

from gametext import *
#from states import *
#from smdmap import *
from textwrap import wrap

prompt = "\n> "

# MISC FUNCTIONS

def menu():
    print menu_txt
    while True:
        menu = raw_input(prmpt).lower().split()

        if "1" in menu or "start" in menu:
            print wr(start_txt)
            return
        elif "2" in menu or "help" in menu:
            instruct()
            print menu_txt
        elif "3" in menu or "exit" in menu or "quit" in menu:
            print "Goodbye!\n"
            exit()
        else:
            print fail_txt

def gameover(why):
    global xflag
    print "\nOh no, you", why, "You're dead!"
    print gameover_txt
    xflag = True
    return
    
def instruct():
    print instruct_txt1
    print wr(instruct_txt2)
    print instruct_txt3

def wr(str):
    split = str.splitlines(1)
    l = []

    for i in range(0,len(split)):
        if split[i] == '\n':
            l += split[i]
        else:
            x = wrap(split[i],55)
            l += x

    jstr = '\n'.join(l)
    return jstr.replace('\n\n\n','\n\n')
