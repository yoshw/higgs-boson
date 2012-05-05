# This Python file uses the following encoding: utf-8

from gametext import *
from states import *
from funcs import *
import string

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
    invq = 0
    
    raw = raw_input(invprmpt).lower().split()
    ralpha = []
    for i in range(len(raw)):
#        print i,":",raw[i]
        raw[i] = raw[i].translate(None,string.punctuation)
        if raw[i].isalpha() == True and not raw[i] in ignore:
            ralpha.append(raw[i])
#    print "ralpha:", ralpha

    if "inv" in ralpha or "inventory" in ralpha:
        invprint()
        return
    elif "help" in ralpha or "info" in ralpha or "instructions" in ralpha:
        instruct()
        return
    elif raw == ["map"] or raw == ["save"]:
        print wr("You can't do that from inside your inventory.")
        return
    elif "exit" in ralpha or "quit" in ralpha or "return" in ralpha:
        return 1

    item = []
    mode = []

    for x in invmodes:
        for n in x:
            if n in ralpha:
                mode.append(x)
#    print "mode:",mode

    if len(mode) == 0:
        print "You have to include an action word I understand."
        return
    elif len(mode) > 1:
        print "No more than one action at a time, thanks."
        return
    elif not (ralpha[0] in mode[0]):
        print wr("Your command must start with an action word.")
        return

    for x in ralpha[1:]:
        iflag = oflag = 0
        for n in idic.keys():
            if states['inv'][n] != 0 and x in n:
                item.append(n)
                iflag = 1
        for n in dic[rm].keys():
            if states[rm][n] != 0 and x in n:
                oflag = 1
        if iflag == 0 and oflag == 0:
            print "I only understood you as far as wanting to %s." % ralpha[0]
#            print "offender:",x
            return rm

    item = list(set(item))
#    print "item:",item

    if len(item) == 0:
        if ralpha == ['look']:
            print wr("It's your trusty shoulder bag -- now doubling as an item inventory.")
        else:
            print fail_txt
        return

    if len(item) > 2:
        print fail_txt
        return

    if len(item) == 2:
        if mode[0] == combine:
            if item[1] in idic[item[0]][states['inv'][item[0]]][combine].keys():
                exec idic[item[0]][states['inv'][item[0]]][combine][item[1]]
                return
            else:
                print "Those items can't be combined."
                return
        elif mode[0] == use:
            if item[1] in idic[item[0]][states['inv'][item[0]]][use]['inv'].keys():
                exec idic[item[0]][states['inv'][item[0]]][use]['inv'][item[1]]
                return
            else:
                print fail_txt
                return
        else:
            print fail_txt
            return

    # we now know that len[item] == 1

    if mode[0] == combine:
        print "You need two items to combine."
        return    
    elif mode[0] == look:
        exec idic[item[0]][states['inv'][item[0]]][look]
        return
    elif mode[0] == use:
        invq = invuse(item[0], ralpha, rm)
        return invq
    else:
        if mode[0] in idic[item[0]][states['inv'][item[0]]].keys():
            exec idic[item[0]][states['inv'][item[0]]][mode[0]]
            return invq
        else:
            print fail_txt
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
        return
    elif not rm in idic[item][states['inv'][item]][use].keys():
        print "You can't use the %s in that way." % item[0]
        return
    elif len(obj) == 0:
        if roomd in idic[item][states['inv'][item]][use][rm].keys():
            exec idic[item][states['inv'][item]][use][rm][roomd]
            return 2
        else:
            print "You need to use the %s with another (present) object." % item[0]
            return
    elif obj[0] in idic[item][states['inv'][item]][use][rm].keys():
        exec idic[item][states['inv'][item]][use][rm][obj[0]]
        return 2
    else:
        print "You can't use the %s in that way." % item[0]
        return


## Inventory Dic

idic = {}

idic[beads] = {
    0: {},
    1: {},
    2: {}
    }

idic[key_bt] = copy.deepcopy(idic[beads])

idic[bottle] = copy.deepcopy(idic[beads])
idic[powder] = copy.deepcopy(idic[beads])
idic[energydrink] = copy.deepcopy(idic[beads])
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


idic[key_bt][1][look] = "print wr('''An old steel key that opens the trapdoor in the bottom room.''')"    
idic[key_bt][1][use] = {'bottomrm':{},'toprm':{}}
idic[key_bt][1][use]['bottomrm'][trapdoor] = """print wr('''With a satisfying, metallic thunk, the key turns in the lock of the trapdoor. You push the trapdoor up -- it's damn heavy! -- and it swings wide open.

Pauli beckons you and you run down the stairs. 'Great stuff, friend!' he says. 'Now get yourself up there and grab my energy drink powder. It's under my bed.' ''')
states['inv'][key_bt] = 0
states['bottomrm'][trapdoor] = 4
states['bottomrm'][stairs] = 4
states['bottomrm'][upstairs] = 4
states['bottomrm'][downstairs] = 1
states['bottomrm'][pauli] = 3
states['bottomrm'][roomd] = 2"""

idic[bottle][1][look] = "print wr('Your trusty BPA- and phthalate-free metal water bottle, topped up with clear, ice-cold water.')"
idic[bottle][1][use] = {'bottomrm':{},'downrm':{},'charmrm':{},'strangerm':{},'muneurm':{},'inv':{}}
idic[bottle][1][use]['muneurm'][feynman] = """print wr('''You offer Feynman your water bottle, but he turns his nose up. 'What is this, water?' he asks. 'Don't you have anything harder?' ''')"""
idic[bottle][1][use]['downrm'][gellmann] = """print wr('''You offer Gell-Mann your water bottle. 'Oh, thank you,' he says. 'That's kind, but I'm not really thirsty.' ''')"""
idic[bottle][1][use]['charmrm'][sagan] = """print wr('''You offer Sagan your water bottle. He turns it over in his hands, an enigmatic smile playing on his lips. 'Water is a truly fascinating substance,' he says. 'Don't you agree?' ''')"""
idic[bottle][1][use]['strangerm'][dirac] = """print wr('''You offer Dirac your water bottle. He sniffs loudly. He won't even look at you.''')"""
idic[bottle][1][use]['bottomrm'][pauli] = """print wr('''You offer Pauli your water bottle. He accepts it gratefully and takes a swig. 'Thank you,' he says, wiping his mouth. 'That's very good. But what I really need, you know, is some StrongForce!' ''')"""
idic[bottle][1][combine] = {
    powder: """print wr('You pour the StrongForce powder into your bottle and swirl it around some. You hear an energetic fizzing coming from the bottle. Perfect.')
states['inv'][bottle] = 0
states['inv'][powder] = 0
states['inv'][energydrink] = 1"""
    }
idic[bottle][1][use]['inv'][powder] = copy.deepcopy(idic[bottle][1][combine][powder])
idic[bottle][1][drink] = "print wr('Aahh ... nothing like a refreshing drink of cold, clear H20.')"
idic[bottle][2] = copy.deepcopy(idic[bottle][1])
idic[bottle][2][look] = "print wr('Your trusty BPA- and phthalate-free metal water bottle, now empty.')"
idic[bottle][2][use] = {}
idic[bottle][2][combine] = {}
idic[bottle][2][drink] = "print wr('''It's empty now, I'm afraid. You'll have to go thirsty.''')"


idic[powder][1][look] = "print wr('Precisely four teaspoons of StrongForce energy drink powder.')"
idic[powder][1][use] = {'bottomrm':{},'inv':{}}
idic[powder][1][use]['bottomrm'][pauli] = """print wr('''Pauli lights up when he sees you have the powder.

'Wonderful!' he says. 'But now the problem is, it can only be taken in liquid form. The powder does me no good whatsoever. So I must ask you to do a little more work for me, and bring me the drink.' ''')"""
idic[powder][1][combine] = {
    bottle: """print wr('You pour the StrongForce powder into your bottle and swirl it around some. You hear an energetic fizzing coming from the bottle. Perfect.')
states['inv'][bottle] = 0
states['inv'][powder] = 0
states['inv'][energydrink] = 1"""
    }
idic[powder][1][use]['inv'][bottle] = copy.deepcopy(idic[powder][1][combine][bottle])


idic[energydrink][1][look] = "print wr('A water bottle full of StrongForce energy drink, fizzing away.')"
idic[energydrink][1][use] = {'bottomrm':{},'strangerm':{},'downrm':{}}
idic[energydrink][1][use]['bottomrm'][pauli] = """print wr('''Pauli's face fills with glee.

'This is truly splendid!' he says. 'Nothing gets me going like StrongForce!'

He takes the bottle from you, unscrews the lid, and downs the contents in one long gulp. He wipes his mouth and throws the bottle back to you.

'Yes, oh yes! Feel the surge!' he says. He shivers, bounces up and down on the spot a couple of times, then making something approaching a war cry, he bounds up the steep staircase with ease.

He disappears through the trapdoor. A few moments pass, in which you can hear rustling from upstairs. You scratch your elbow. Then Pauli's voice floats down from above:

'Before you leave, friend, why don't you pop up here. I have something to give you for your hard work.' ''')
states['inv'][energydrink] = 0
states['inv'][bottle] = 2
states['bottomrm'][pauli] =
states['toprm'][pauli] =
etc. etc.
"""
idic[energydrink][1][use]['downrm'][gellmann] = """print wr('''You offer Gell-Mann the energy drink. 'Oh, thank you,' he says. 'But I really have as much energy as I need.' ''')"""
idic[energydrink][1][use]['strangerm'][dirac] = """print wr('''You offer Dirac the energy drink. His eyes widen. 'What is this!' he shouts. 'Some kind of insult? Fiend!' ''')"""
idic[energydrink][1][drink] = "print wr('''You'd better not drink it. That would make Pauli very unhappy.''')"


idic[bongos][1][look] = "print wr('A set of cheap bongos with blue and red stars painted on the side.')"
idic[bongos][1][use] = {'muneurm':{},'inv':{}}
idic[bongos][1][use]['muneurm'][feynman] = """print wr('''You pull the bongos out of your bag. Feynman's eyes light up and he jumps from his chair.

'Hey, brilliant! I love the bongos.' He takes the drums off you, and turns them over in his hands. 'But wait a second.' He cocks his head to one side. 'I can't play these. There's no stand. You can't play the drums sitting down. You gotta move your body, that's where the rhythm comes from.' He hands the drums back to you and returns to his seat.''')"""
idic[bongos][1][combine] = {
    tripod: """print wr('You jam the bongos down onto the top of the tripod. Not a perfect fit, but it holds firm. You now have a serviceable set of upright bongos.')
states['inv'][bongos] = 0
states['inv'][tripod] = 0
states['inv'][up_bongos] = 1"""
    }
idic[bongos][1][use]['inv'][tripod] = copy.deepcopy(idic[bongos][1][combine][tripod])
idic[bongos][1][drum] = """print wr('''You try tapping out a rhythm on the bongos, but resign yourself to the fact that you'll never be any good.''')"""


idic[tripod][1][look] = "print wr('A rusty old tripod.')"
idic[tripod][1][use] = {'muneurm':{},'inv':{}}
idic[tripod][1][use]['muneurm'][feynman] = """print wr("'Why the hell are you showing me this?' Feynman scowls.")"""
idic[tripod][1][combine] = {
    bongos: """print wr('You jam the bongos down onto the top of the tripod. Not a perfect fit, but it holds firm. You now have a serviceable set of upright bongos.')
states['inv'][bongos] = 0
states['inv'][tripod] = 0
states['inv'][up_bongos] = 1"""
    }
idic[tripod][1][use]['inv'][bongos] = copy.deepcopy(idic[tripod][1][combine][bongos])


idic[up_bongos][1][look] = "print wr('A cheap pair of bongos wedged onto the top of a rusty old tripod.')"
idic[up_bongos][1][use] = {'muneurm':{},'inv':{}}
idic[up_bongos][1][use]['muneurm'][feynman] = """print wr('''You pull the bongos out of your bag. Feynman's eyes light up and he jumps from his chair.

'Hey, brilliant! I love the bongos.' He takes the drums off you, extends the legs of the tripod, and sets it on the ground. 'Watch this, fella,' he says, and begins to play. The music is odd. But he's well and truly distracted, so you can finally get through that door.''')
states['muneurm'][feynman] = 3
states['muneurm'][s_door] = 2
states['muneurm'][e_door] = 2
states['muneurm'][w_door] = 2
states['inv'][up_bongos] = 0"""


idic[rope][1][look] = "print wr('A long coil of rope.')"
idic[rope][1][use] = {'downrm':{},'uprm':{},'inv':{}}
idic[rope][1][use]['downrm'][gellmann] = """print wr("'Great,' Gell-Mann says, 'so you got yourself a rope. Now what?'")"""
idic[rope][1][use]['uprm'][hadrons] = """print wr("You attach one end of the rope to the handle of the briefcase, using a highly secure knot passed down to you by your father (now deceased).")
states["inv"][rope] = 0
states['downrm'][rope] = 3
states['downrm'][gellmann] = 3
states['downrm'][roomd] = 2
states['uprm'][hadrons] = 2
states['uprm'][rope] = 1"""


idic[teaspoon][1][look] = "print wr('A silver teaspoon.')"
idic[teaspoon][1][use] = {'strangerm':{},'inv':{}}
idic[teaspoon][1][use]['strangerm'][roomd] = "print wr('''A magical feeling comes over you as you wave the teaspoon around the room. Dirac is unimpressed.''')"
