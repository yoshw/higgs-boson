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
        menu = raw_input(prmpt).lower().split()

        if "1" in menu or "start" in menu:
            print w(start_txt)
            return
        elif "2" in menu or "instructions" in menu or "instruct" in menu:
            instruct()
            print menu_txt
        elif "3" in menu or "exit" in menu or "quit" in menu:
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
    while invq != 1 and invq != 2:
        invq = invprompter(rm)
    if invq == 1:
        print "You close your bag and sling it back over your shoulder."
    return

def invprompter(rm):
    raw = raw_input("\nINV >> ").lower().split()

    if "inv" in raw or "inventory" in raw:
        invprint()
        return
    elif "instr" in raw or "instruct" in raw or "instructions" in raw:
        instruct()
        return
    elif "exit" in raw or "quit" in raw or "return" in raw:
        invq = 1
        return invq

    obj = []
    mode = []

    ob_list = [x for x in idic.keys() if states['inv'][x] != 0]

    for ob in ob_list:
        for name in ob:
            if name in raw:
                obj.append(ob)
                #    print "invob_list:", ob_list

    obj = list(set(obj))

    if len(obj) == 0:
        if raw == ['look']:
            print w("It's your trusty shoulder bag -- now doubling as an item inventory.")
        else:
            print fail_txt
        return

    md_list = idic[obj[0]][states["inv"][obj[0]]].keys()

    for md in md_list:
        for name in md:
            if name in raw:
                mode.append(md)

    if len(mode) == 0:
        print "I don't understand that action."
        return
    elif len(mode) > 1:
        print "No more than one action at a time, please."
        return
    elif len(obj) > 1 and mode[0] != combine:
        print fail_txt
        return
    elif mode[0] == look:
        exec idic[obj[0]][states['inv'][obj[0]]][look]
        return
    elif mode[0] == combine and len(obj) != 2:
        print "You can only combine two items. No more, no less."
        return
    elif mode[0] == combine:
        if obj[1] in idic[obj[0]][states['inv'][obj[0]]][combine].keys():
            exec idic[obj[0]][states['inv'][obj[0]]][combine][obj[1]]
            return
        else:
            print "Those items can't be combined."
            return
    elif mode[0] == use:
        if len(obj) != 1:
            print fail_txt
            return
        else:
            invq = invuse(obj[0], raw, rm)
            return invq
    else:
        exec idic[obj[0]][states['inv'][obj[0]]][mode[0]]
        return

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

        #    print "item:", item
        #    print "objects:", obj

    if len(obj) > 1:
        print fail_txt
        return 0
    elif len(obj) == 0:
        print "You need to use the %s with another (present) object." % item[0]
        return 0
    elif obj[0] in idic[item][states['inv'][item]][use].keys():
        exec idic[item][states['inv'][item]][use][obj[0]]
        return 2
    else:
        print "You can't use the %s in that way." % item[0]
        return 0
