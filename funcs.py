# This Python file uses the following encoding: utf-8

from gametext import *
from states import *
from inv import *
from textwrap import wrap

prompt = "\n> "


# MISC FUNCTIONS

def menu():
    print menu_txt
    while True:
        menu = raw_input(prmpt).lower()

        if menu == "1" or menu == "start" or menu == "start game":
            print w(start_txt)
            return room('entryrm')
        elif menu == "2" or menu == "instructions" or menu == "instruct":
            instruct()
            print menu_txt
        elif menu == "3" or "exit" in menu:
            print "\nGoodbye!\n"
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
    print instruct_txt

def w(str):
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


# INVENTORY FUNCTIONS

def invprint():
    inv_list = [x[0] for x in idic.keys() if states['inv'][x] == 1]

    print inv_txt
    if len(inv_list) == 0:
        print "        - Nothing here right now!"
    else:
        for i in range(0, len(inv_list)):
            print "        - ", inv_list[i]
    print inv2_txt
            
def inv(rm):
    invprint()

    invq = 0
    while invq != 1:
        invq = invprompter(rm)
        print invq
    print "You close your bag and sling it back over your shoulder.\n"
    return

def invprompter(rm):
    raw = raw_input("\nINV >> ").lower()

    if raw == "inv" or raw == "inventory":
        invprint()
        return
    elif raw == "instr" or raw == "instruct" or raw == "instructions":
        instruct()
        return
    elif "exit" in raw or "return" in raw:
        invq = 1
        return invq

    obj = []
    mode = []

    ob_list = [x for x in idic.keys() if states['inv'][x] == 1]

    for ob in ob_list:
        for name in ob:
            if name in raw:
                obj.append(ob)
                #    print "invob_list:", ob_list

    obj = list(set(obj))

    if len(obj) == 0:
        print fail_txt
        return

    md_list = ['look','use','combine']

    for md in md_list:
        if md in raw:
            mode.append(md)

    if len(obj) == 1 and len(mode) == 0:
        print "I don't understand that action."
        return
    elif len(obj) > 1 and len(mode) == 0:
        print fail_txt
        return
    elif len(mode) > 1:
        print "No more than one action at a time, please."
        return
    elif mode[0] == 'look' and len(obj) == 1:
        exec idic[obj[0]][1]['d']
        return
    elif mode[0] == 'look':
        print "You can only look at one item at a time."
        return
    elif mode[0] == 'combine' and (len(obj) != 2):
        print "You need to combine (exactly) two items."
        return
    elif mode[0] == 'combine':
        exec idic[obj[0]][1]['combine'][obj[1]]
        invq = 1
        return invq
    elif mode[0] == 'use' and len(obj) != 1:
        print fail_txt
        return
    else:
        invuse(obj[0], raw, rm)
        invq = 1
        return invq

def invuse(item, raw, rm):
    obj = []
    ob_list = dic[rm].keys()
    for ob in ob_list:
        for name in ob:
            if name in raw:
                obj.append(ob)
    obj = list(set(obj))

    if item in obj:
        obj.remove(item)

    if len(obj) > 1:
        print fail_txt
        return
    elif len(obj) == 0:
        print "You need to use the %s with another object." % item[0]
        return
    elif obj[0] in idic[item][1]['use'].keys():
        exec idic[item][1]['use'][obj[0]]
    else:
        print "You can't use the %s in that way." % item[0]
        return
