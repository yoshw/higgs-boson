# This Python file uses the following encoding: utf-8

from funcs import *

xflag = False

def prompter(rm):
    global xflag
    raw = raw_input(prmpt).lower()

    if raw == "inv" or raw == "inventory":
        inv(rm)
        return prompter(rm)
    elif raw == "instr" or raw == "instruct" or raw == "instructions":
        instruct()
        return prompter(rm)
    elif raw == "map":
        print fullmap
        return prompter(rm)
    elif "exit" in raw:
        print "\nGoodbye!\n"
        xflag = True
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
        return prompter(rm)

    md_list = dic[rm][obj[0]][states[rm][obj[0]]].keys()

    for md in md_list:
        if md in raw:
            mode.append(md)
#    print "mode:", mode
    item = [x[0] for x in idic.keys() for n in x if (n in raw and states['inv'][x] == 1)]

    if len(obj) == 1 and len(mode) == 0:
        print "I don't understand that action."
        return prompter(rm)
    elif len(obj) > 1 or len(mode) > 1:
        print "No more than one action or object at a time, please."
        return prompter(rm)
    elif len(obj) == 1 and mode[0] == 'use' and len(item) > 0:
        print "Try opening your inventory first."
        return prompter(rm)
    else:
        exec dic[rm][obj[0]][states[rm][obj[0]]][mode[0]]
        return prompter(rm)

def room(rm):
    raw_input("\nENTER TO CONTINUE >\n")
    exec dic[rm][roomd][states[rm][roomd]]["look"]
    while True:
        if xflag == False:
            prompter(rm)
        else:
            exit()
        
print title_txt
menu()
