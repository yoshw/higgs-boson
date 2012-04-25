# This Python file uses the following encoding: utf-8

from gametext import *
from funcs import *
from states import *
from smdmap import *
from inv import *
import traceback

qflag = False

def prompter(rm):
    global qflag
    newrm = rm

    raw = raw_input(prmpt).lower().split()
    ralpha = []
    for i in range(len(raw)):
        print i,":",raw[i]
        if raw[i].isalpha() == True:
            ralpha.append(raw[i])
    print "ralpha:", ralpha
    
    if "inv" in raw or "inventory" in raw:
        inv(rm)
        return rm
    elif "help" in raw or "info" in raw or "instructions" in raw:
        instruct()
        return rm
    elif raw == ["map"]:
        mapp(rm)
        return rm
    elif "exit" in raw or "quit" in raw:
        qflag = True
        return rm
    elif raw == ["traceback"]:
        traceback.print_stack()
        return rm

    item = []
    obj = []
    mode = []

    for x in idic.keys():
        for n in x:
            if (n in raw and states['inv'][x] != 0):
                item.append(x)
                #print item

    item = list(set(item))
    
    if len(item) > 2:
        print wr("Whoa, too many items there.")
    elif len(item) == 2:
        if raw[0] in combine:
            print wr("You'll need to be in your inventory to combine those items.")
        else:
            print wr("Whoa, too many items there.")
    elif len(item) == 1:
        print "bla bla bla"

    for x in dic[rm].keys():
        for n in x:
            if (n in raw and states[rm][x] != 0):
                obj.append(x)

    obj = list(set(obj))
    #    print "obj:", obj

    if len(obj) == 0:
        if raw == ['look']:
            exec dic[rm][roomd][states[rm][roomd]][look]
        else:
            print fail_txt
        return rm

    #    md_list = dic[rm][obj[0]][states[rm][obj[0]]].keys()

    for md in dic[rm][obj[0]][states[rm][obj[0]]].keys():
        for name in md:
            if name in raw:
                mode.append(md)
    #    print "mode:", mode

    if len(obj) == 1 and len(mode) == 0:
        print "I don't understand that action."
        return rm
    elif len(obj) > 1 or len(mode) > 1:
        print "No more than one action or object at a time, please."
        return rm
    elif len(obj) == 1 and mode[0] == 'use' and len(item) > 0:
        print "Try opening your inventory first."
        return rm
    else:
        exec dic[rm][obj[0]][states[rm][obj[0]]][mode[0]]
        return newrm

def room():
    rm = "entryrm"
    newrm = rm

    while True:
        raw_input("\nENTER TO CONTINUE >\n")
        exec dic[rm][roomd][states[rm][roomd]][look]
        while newrm == rm:
            newrm = prompter(rm)
            if qflag == True:
                print "Goodbye!\n"
                exit()
        rm = newrm

        
print title_txt
menu()
room()
