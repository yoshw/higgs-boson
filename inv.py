# This Python file uses the following encoding: utf-8

from gametext import *
from states import *
from funcs import *

# Inv Boilerplate

inv_txt = """
---------------------------------------------------

                I N V E N T O R Y
                - - - - - - - - -

              This is your inventory.
 Standard actions are <look>, <use> and <combine>;
           <inv> will reprint this list.
"""
inv2_txt = """
---------------------------------------------------
"""

# Beads

beadmap = {
'a': "           ========================= ",
'b': ["          | ","   ","  ","   ","  ","   ","  || ","     "," |"],
'c': ["          | ","   ","  ","   ","  ","   ","  || ","     "," |"],
'd': ["          | ","    "," ","    "," ","    "," || ","     "," |"],
'e': ["          | ","   ","  ","   ","  ","   ","  || ","     "," |"],
'f': "           ========================= "
}

def beadprint():
    for i in states[beads].keys():
        if states[beads][i] == 1:
            beadshow(i)
        elif states[beads][i] == 0:
            beadhide(i)
    
    k = beadmap.keys()
    k.sort()
    for i in k:
        i = ''.join(beadmap[i])
        print i

bead_disp = {
    'u': ['b',1,'(u)','   '],
    'd': ['c',1,'(d)','   '],
    'c': ['b',3,'(c)','   '],
    's': ['c',3,'(s)','   '],
    't': ['b',5,'(t)','   '],
    'b': ['c',5,'(b)','   '],
    've': ['d',1,u'(νe)','    '],
    'vmu': ['d',3,u'(νμ)','    '],
    'vtau': ['d',5,u'(ντ)','    '],
    'e': ['e',1,'(e)','   '],
    'mu': ['e',3,'(μ)','   '],
    'tau': ['e',5,'(τ)','   '],
    'y': ['b',7,u'[ γ ]','     '],
    'g': ['c',7,'[ g ]','     '],
    'Z': ['d',7,'[ Z ]','     '],
    'W': ['e',7,'[ W ]','     ']
    }

def beadshow(bead):
    beadmap[bead_disp[bead][0]][bead_disp[bead][1]] = bead_disp[bead][2]

def beadhide(bead):
    beadmap[bead_disp[bead][0]][bead_disp[bead][1]] = bead_disp[bead][3]
        
# Functions

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
    raw = raw_input(invprmpt).lower().split()

    if "inv" in raw or "inventory" in raw:
        invprint()
        return
    elif "help" in raw or "info" in raw or "instructions" in raw:
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
            print wr("It's your trusty shoulder bag -- now doubling as an item inventory.")
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
    for x in dic[rm].keys():
        for n in x:
            if states[rm][x] != 0 and n in raw:
                obj.append(x)
    obj = list(set(obj))

        #    print "item:", item
        #    print "objects:", obj

    if len(obj) > 1:
        print fail_txt
        return 0
    elif len(obj) == 0:
        if roomd in idic[item][states['inv'][item]][use].keys():
            exec idic[item][states['inv'][item]][use][roomd]
            return 2
        else:
            print "You need to use the %s with another (present) object." % item[0]
            return 0
    elif obj[0] in idic[item][states['inv'][item]][use].keys():
        exec idic[item][states['inv'][item]][use][obj[0]]
        return 2
    else:
        print "You can't use the %s in that way." % item[0]
        return 0


## Inventory Dic

idic = {}

idic[beads] = {
    0: {},
    1: {},
    2: {}
    }

idic[bongos] = copy.deepcopy(idic[beads])
idic[tripod] = copy.deepcopy(idic[beads])
idic[up_bongos] = copy.deepcopy(idic[beads])
idic[rope] = copy.deepcopy(idic[beads])
idic[teaspoon] = copy.deepcopy(idic[beads])
#New inventory items get added here!

idic[beads][1][look] = """print '''
---------------------------------------------------

      You have collected the following beads:
'''
beadprint()
print '''
---------------------------------------------------
'''
"""
idic[beads][1][use] = "print wr('''You can't use them yet.''')"

idic[bongos][1][look] = "print wr('A set of cheap bongos with blue and red stars painted on the side.')"
idic[bongos][1][use] = {
    feynman: """print wr('''You pull the bongos out of your bag. Feynman's eyes light up and he jumps from his chair.

'Hey, brilliant! I love the bongos.' He takes the drums off you, and turns them over in his hands. 'But wait a second.' He cocks his head to one side. 'I can't play these. There's no stand. You can't play the drums sitting down. You gotta move your body, that's where the rhythm comes from.' He hands the drums back to you and returns to his seat.''')"""
    }
idic[bongos][1][combine] = {
    tripod: """print wr('You jam the bongos down onto the top of the tripod. Not a perfect fit, but it holds firm. You now have a serviceable set of upright bongos.')
states['inv'][bongos] = 0
states['inv'][tripod] = 0
states['inv'][up_bongos] = 1"""
    }
idic[bongos][1][use][tripod] = copy.deepcopy(idic[bongos][1][combine][tripod])
idic[bongos][1][drum] = "print wr('''You try tapping out a rhythm on the bongos, but resign yourself to the fact that you'll never be any good.''')"

idic[tripod][1][look] = "print wr('A rusty old tripod.')"
idic[tripod][1][use] = {
    feynman: """print wr("'Why the hell are you showing me this?' Feynman scowls.")"""
    }
idic[tripod][1][combine] = {
    bongos: """print wr('You jam the bongos down onto the top of the tripod. Not a perfect fit, but it holds firm. You now have a serviceable set of upright bongos.')
states['inv'][bongos] = 0
states['inv'][tripod] = 0
states['inv'][up_bongos] = 1"""
    }
idic[tripod][1][use][bongos] = copy.deepcopy(idic[tripod][1][combine][bongos])

idic[up_bongos][1][look] = "print wr('A cheap pair of bongos wedged onto the top of a rusty old tripod.')"
idic[up_bongos][1][use] = {
    feynman: """print wr('''You pull the bongos out of your bag. Feynman's eyes light up and he jumps from his chair.

'Hey, brilliant! I love the bongos.' He takes the drums off you, extends the legs of the tripod, and sets it on the ground. 'Watch this, fella,' he says, and begins to play. The music is odd. But he's well and truly distracted, so you can finally get through that door.''')
states['muneurm'][feynman] = 3
states['muneurm'][s_door] = 2
states['muneurm'][e_door] = 2
states['muneurm'][w_door] = 2
states['inv'][up_bongos] = 0"""
    }

idic[rope][1][look] = "print wr('A long coil of rope.')"
idic[rope][1][use] = {
    gellmann: """print wr("'Great,' Gell-Mann says, 'so you got yourself a rope. Now what?'")""",
    hadrons: """print wr("You attach one end of the rope to the handle of the briefcase, using a highly secure knot passed down to you by your father (now deceased).")
states["inv"][rope] = 0
states['downrm'][rope] = 3
states['downrm'][gellmann] = 3
states['downrm'][roomd] = 2
states['uprm'][hadrons] = 2
states['uprm'][rope] = 1"""
    }

idic[teaspoon][1][look] = "print wr('A silver teaspoon.')"
idic[teaspoon][1][use] = {
    }
