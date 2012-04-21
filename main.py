# This Python file uses the following encoding: utf-8

from funcs import *

qflag = False

def prompter(rm):
    global qflag
    raw = raw_input(prmpt).lower().split()

    if "inv" in raw or "inventory" in raw:
        inv(rm)
        return
    elif "instr" in raw or "instruct" in raw or "instructions" in raw:
        instruct()
        return
    elif raw == "map":
        print fullmap
        return
    elif "exit" in raw or "quit" in raw:
        qflag = True
        return

    obj = []
    mode = []

    ob_list = dic[rm].keys()

    for ob in ob_list:
        for name in ob:
            if name in raw:
                obj.append(ob)
    #    print "ob_list:", ob_list

    obj = list(set(obj))
    #print "obj:", obj

    if len(obj) == 0:
        print fail_txt
        return

    md_list = dic[rm][obj[0]][states[rm][obj[0]]].keys()

    for md in md_list:
        if md in raw:
            mode.append(md)
#    print "mode:", mode
    item = [x[0] for x in idic.keys() for n in x if (n in raw and states['inv'][x] == 1)]

    if len(obj) == 1 and len(mode) == 0:
        print "I don't understand that action."
        return
    elif len(obj) > 1 or len(mode) > 1:
        print "No more than one action or object at a time, please."
        return
    elif len(obj) == 1 and mode[0] == 'use' and len(item) > 0:
        print "Try opening your inventory first."
        return
    else:
        exec dic[rm][obj[0]][states[rm][obj[0]]][mode[0]]
        return

def room(rm):
    raw_input("\nENTER TO CONTINUE >\n")
    exec dic[rm][roomd][states[rm][roomd]]["look"]
    while True:
        if qflag == False:
            prompter(rm)
        else:
            print "\nGoodbye!\n"
            exit()
        
print title_txt
menu()
room('entryrm')
