# This Python file uses the following encoding: utf-8

from gametext import *
from funcs import *
from states import *
from smdmap import *
from inv import *
import traceback
import string

qflag = False

def prompter(rm):
    global qflag
    newrm = rm

    raw = raw_input(prmpt).lower().split()
    ralpha = []
    for i in range(len(raw)):
        print i,":",raw[i]
        raw[i] = raw[i].translate(None,string.punctuation)
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
            newrm = prompteralt(rm)
            if qflag == True:
                print "Goodbye!\n"
                exit()
        rm = newrm


def prompteralt(rm):
    global qflag
    newrm = rm
    
    raw = raw_input(prmpt).lower().split()
    ralpha = []
    for i in range(len(raw)):
        #        print i,":",raw[i]
        raw[i] = raw[i].translate(None,string.punctuation)
        if raw[i].isalpha() == True and not raw[i] in ignore:
            ralpha.append(raw[i])
    print "ralpha:", ralpha

    # remove ignored words here!
    
    if "inv" in raw or "inventory" in raw:
        inv(rm)
        return rm
    elif "help" in raw or "info" in raw or "instructions" in raw:
        instruct()
        return rm
    elif raw == ["map"]:
        mapp(rm)
        return rm
    elif raw == ["save"]:
        print "Watch this space."
        return rm
    elif "exit" in raw or "quit" in raw:
        qflag = True
        return rm
#    elif raw == ["traceback"]:
#        traceback.print_stack()
#        return rm

    mode = []
    item = []
    obj = []

    for x in modes:
        for n in x:
            if n in ralpha:
                mode.append(x)
    print "mode:", mode

    if len(mode) == 0:
        print "You have to enter an action word I can understand."
        return rm
    elif len(mode) > 1:
        print "No more than one action at a time, thanks."
        return rm
    elif not (ralpha[0] in mode[0]):
        print wr("Your command must start with an action word.")
        return rm

    for x in ralpha[1:]:
        iflag = 0
        oflag = 0
        for n in idic.keys():
            if states['inv'][n] != 0 and x in n:
                item.append(n)
                iflag = 1
        for n in dic[rm].keys():
            if states[rm][n] != 0 and x in n:
                obj.append(n)
                oflag = 1
        if iflag == 0 and oflag == 0:
            print "I only understood you as far as wanting to %s." % ralpha[0]
            print "offender:",x
            return rm

    item = list(set(item))
    obj = list(set(obj))
    print "obj:", obj
    print "item:", item

    if len(item) > 1:
        print fail_txt
        return rm
    elif len(obj) > 1:
        print fail_txt
        return rm
    elif len(item) == 0 and len(obj) == 0:
        if mode[0] is look:
            exec dic[rm][roomd][states[rm][roomd]][look]
            return rm
        else:
            print fail_txt
            return rm

    if len(item) == 1:
        if mode[0] is use:
            invuse(item[0], ralpha, rm)
            return newrm
        else:
            print fail_txt
            return rm

    exec dic[rm][obj[0]][states[rm][obj[0]]][mode[0]]
    return newrm
    
"""
    for x in idic.keys():
        for n in x:
            if (n in ralpha and states['inv'][x] != 0):
                item.append(x)
    item = list(set(item))
    print "item:", item

    for x in dic[rm].keys():
        for n in x:
            if (n in ralpha and states[rm][x] != 0):
                obj.append(x)
    obj = list(set(obj))
    print "obj:", obj
"""

        
print title_txt
menu()
room()
