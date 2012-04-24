# This Python file uses the following encoding: utf-8

from funcs import *
import traceback

qflag = False

def prompter(rm):
    global qflag
    newrm = rm
    
    raw = raw_input(prmpt).lower().split()
    # print "raw:", raw
    
    if "inv" in raw or "inventory" in raw:
        inv(rm)
        return rm
    elif "instr" in raw or "instruct" in raw or "instructions" in raw:
        instruct()
        return rm
    elif raw == ["map"]:
        print fullmap
        return rm
    elif "exit" in raw or "quit" in raw:
        qflag = True
        return rm
    elif raw == ["traceback"]:
        traceback.print_stack()
        return rm

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
        if raw == ['look']:
            exec dic[rm][roomd][states[rm][roomd]][look]
        else:
            print fail_txt
        return rm

    md_list = dic[rm][obj[0]][states[rm][obj[0]]].keys()

    for md in md_list:
        for name in md:
            if name in raw:
                mode.append(md)
    #    print "mode:", mode
    item = [x[0] for x in idic.keys() for n in x if (n in raw and states['inv'][x] == 1)]

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
