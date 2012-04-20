# This Python file uses the following encoding: utf-8

from gametext import *
from states import *
from inv import *
from textwrap import wrap

prompt = "\n> "

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

"""def prompter(rm):
    raw = raw_input(prompt).lower()

    if raw == "inv" or raw == "inventory":
        inv()
        return prompter(rm)
    elif raw == "instr" or raw == "instruct" or raw == "instructions":
        instruct()
        return prompter(rm)    
    elif raw == "exit":
        print "\nGoodbye!\n"
        exit(0)

    obj = []
    mode = []

    ob_list = dic[rm].keys()

    for ob in ob_list:
        for name in ob:
            if name in raw:
                obj.append(ob)
#    print "ob_list:", ob_list

    obj = list(set(obj))
#    print "obj:", obj

    if len(obj) == 0:
        print "I don't understand that."
        return prompter(rm)

    md_list = dic[rm][obj[0]][states[rm][obj[0]]].keys()

    for md in md_list:
        if md in raw:
            mode.append(md)
#    print "mode:", mode

    if len(obj) == 1 and len(mode) == 0:
        print "What do you want to do with that object?"
        return prompter(rm)
    elif len(obj) > 1 or len(mode) > 1:
        print "No more than one action or object at a time, please."
        return prompter(rm)
    else:
        exec dic[rm][obj[0]][states[rm][obj[0]]][mode[0]]
        return prompter(rm)"""
        
#def use(str):


def inv(rm):
    inv_list = [x[0] for x in idic.keys() if states['inv'][x] == 1]

    print inv_txt
    if len(inv_list) == 0:
        print "        - Nothing here right now!"
    for i in range(0, len(inv_list)):
        print "        - ", inv_list[i]
    print inv2_txt

    invprompter(rm)

def invprompter(rm):
    raw = raw_input("\nINV >> ").lower()

    if raw == "inv" or raw == "inventory":
        inv(rm)
    elif raw == "instr" or raw == "instruct" or raw == "instructions":
        instruct()
        invprompter(rm)
    elif "exit" in raw or "return" in raw:
        print "You close your bag and sling it back over your shoulder.\n"
        return

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
        return invprompter(rm)

    md_list = ['look','use','combine']

    for md in md_list:
        if md in raw:
            mode.append(md)

    if len(obj) == 1 and len(mode) == 0:
        print "I don't understand that action."
        return invprompter(rm)
    elif len(obj) > 1 and len(mode) == 0:
        print fail_txt
        return invprompter(rm)
    elif len(mode) > 1:
        print "No more than one action at a time, please."
        return invprompter(rm)
    elif mode[0] == 'look' and len(obj) == 1:
        exec idic[obj[0]][1]['d']
        return invprompter(rm)
    elif mode[0] == 'look':
        print "You can only look at one item at a time."
        return invprompter(rm)
    elif mode[0] == 'combine' and (len(obj) != 2):
        print "You need to combine (exactly) two items."
        return invprompter(rm)
    elif mode[0] == 'combine':
        exec idic[obj[0]][1]['combine'][obj[1]]
        return None
    elif mode[0] == 'use' and len(obj) != 1:
        print fail_txt
        return invprompter(rm)
    else:
        invuse(obj[0], raw, rm)
        return None

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

    if len(obj) != 1:
        print fail_txt
        return invprompter(rm)
    elif obj[0] in idic[item][1]['use'].keys():
        exec idic[item][1]['use'][obj[0]]
    else:
        print "You can't use the %s in that way." % item[0]
        return invprompter(rm)
