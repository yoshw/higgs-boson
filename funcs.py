# This Python file uses the following encoding: utf-8

from gametext import *
from states import *
#from smdmap import *
from textwrap import wrap
import os
import glob
import pickle

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

def save(states,map):
    existing = []
    for x in glob.glob(os.getcwd()+'/save*.txt'):
        a = x.partition('save_')
        b = a[2].partition('.txt')
        existing.append(b[0])
    
    print "Enter a name for your save file (avoiding special characters such as: / \ ? % * : | \" ' < > . ( ) ; # &)."
    print "\nEXISTING FILES: "+', '.join(existing)
    print "Retype an existing file name to save over it.\n"

    badlist = ["/","\\","?","%","*",":","|",'"',"'","<",">",".","(",")",";","#","&"]

    while True:
        raw = raw_input("File name: ").lower()

        if ('exit' in raw) or ('cancel' in raw):
            print "Save aborted."
            return
        
        fail = []
        for i in range(len(raw)):
            if raw[i] in badlist:
                fail.append(raw[i])
                
        if len(fail) > 0:
            print "Invalid file name!\n"
        elif raw in existing:
            x = 0
            while True:
                saveover = raw_input("\nAre you sure you want to save over this file? (y/n)  ").lower()
                if (saveover == "n") or (saveover == "no"):
                    break
                elif (saveover == "y") or (saveover == "yes"):
                    x = 1
                    break
                else: pass
            if x == 0:
                pass
            else: break
        else: break

    filename = "save_"+''.join(raw.split())+".txt"
    SFILE = open(filename,"w")
    pickle.dump(states, SFILE)
    pickle.dump(map, SFILE)
    SFILE.close()

    print "\nFile '%s' saved." % ''.join(raw.split())
    
def load():    
    existing = []
    for x in glob.glob(os.getcwd()+'/save*.txt'):
        a = x.partition('save_')
        b = a[2].partition('.txt')
        existing.append(b[0])

    print "Which file do you want to load?\n"
    print '\n'.join(existing)

    while True:
        raw = raw_input('\n--> ').lower()

        if ('exit' in raw) or ('cancel' in raw):
            print "Load aborted."
            return

        if raw not in existing:
            print "That file does not exist. Please specify an existing file."
        else: break

    filename = os.getcwd()+"/save_"+raw+".txt"

    LFILE = open(filename,'r')
    tastes = pickle.load(LFILE)
    pamdms = pickle.load(LFILE)
    LFILE.close()

    print "File loaded."
    return tastes,pamdms
