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
    inv_list = [x[0] for x in idic.keys() if (states['inv'][x] > 0 and states['inv'][x] < 9)]
    inv_list.sort(key=string.lower)

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
        if 'no_ob' in idic[item][states['inv'][item]][use][rm].keys():
            exec idic[item][states['inv'][item]][use][rm]['no_ob']
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

idic[key] = copy.deepcopy(idic[beads])
idic[key_bt] = copy.deepcopy(idic[beads])

idic[bottle] = copy.deepcopy(idic[beads])
idic[powder] = copy.deepcopy(idic[beads])
idic[refresher] = copy.deepcopy(idic[beads])
idic[bongos] = copy.deepcopy(idic[beads])
idic[tripod] = copy.deepcopy(idic[beads])
idic[up_bongos] = copy.deepcopy(idic[beads])
idic[rope] = copy.deepcopy(idic[beads])
idic[teaspoon] = copy.deepcopy(idic[beads])
idic[seashell] = copy.deepcopy(idic[beads])
idic[paperclip] = copy.deepcopy(idic[beads])
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
idic[beads][1][use] = {}

idic[key][9] = {}
idic[key][9][look] = "print wr('''Which key do you want to look at? You can use the code in square brackets to refer to a particular key.''')"
idic[key][9][use] = {'entryrm':{},'bottomrm':{}}
idic[key][9][use]['entryrm']['no_ob'] = "print wr('''You don't have a key that works here.''')"
idic[key][9][use]['mainrm'] = copy.deepcopy(idic[key][9][use]['entryrm'])
idic[key][9][use]['strangerm'] = copy.deepcopy(idic[key][9][use]['entryrm'])
idic[key][9][use]['charmrm'] = copy.deepcopy(idic[key][9][use]['entryrm'])
idic[key][9][use]['uprm'] = copy.deepcopy(idic[key][9][use]['entryrm'])
idic[key][9][use]['downrm'] = copy.deepcopy(idic[key][9][use]['entryrm'])
idic[key][9][use]['bottomrm']['no_ob'] = """if states['inv'][key_bt] == 1:
    print wr('''You better use the key on the trapdoor.''')
else:
    print wr('''You don't have a key that works here.''')
"""
idic[key][9][use]['bottomrm'][trapdoor] = """if states['inv'][key_bt] == 1:
    exec idic[key_bt][1][use]['bottomrm'][trapdoor]
else:
    print wr('''You don't have a key that works here.''')"""
idic[key][9][use]['toprm'] = copy.deepcopy(idic[key][9][use]['entryrm'])
idic[key][9][use]['muneurm'] = copy.deepcopy(idic[key][9][use]['entryrm'])


idic[key_bt][1][look] = "print wr('''An old steel key that opens the trapdoor in the bottom room.''')"    
idic[key_bt][1][use] = {'bottomrm':{},'inv':{}}
idic[key_bt][1][use]['bottomrm'][trapdoor] = """if states['bottomrm'][pauli] == 1:
    exec dic['bottomrm'][pauli][1][talk]
else:
    print wr('''With a satisfying, metallic thunk, the key turns in the lock of the trapdoor. You push the trapdoor up -- it's damn heavy! -- and it swings wide open.

Pauli beckons you and you run down the stairs. 'Great stuff, friend!' he says. 'Now get yourself up there and grab my Strongforce powder. It's under my bed. Just give the dials a good spin.' ''')
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
    powder: """if states['inv'][powder] == 1:
    print wr('''You can't just go pouring an indiscriminate amount of powder into your bottle. Have you seen what excessive energy drink consumption can do to your heart?''')
elif states['inv'][powder] == 2:
    print wr('You pour the StrongForce powder into your bottle and swirl it around some. You hear an energetic fizzing coming from the bottle. Perfect.')
    states['inv'][bottle] = 0
    states['inv'][powder] = 0
    states['inv'][refresher] = 1"""
    }
idic[bottle][1][use]['inv'][powder] = copy.deepcopy(idic[bottle][1][combine][powder])
idic[bottle][1][drink] = "print wr('Aahh ... nothing like a refreshing drink of cold, clear H20.')"
idic[bottle][2] = copy.deepcopy(idic[bottle][1])
idic[bottle][2][look] = "print wr('Your trusty BPA- and phthalate-free metal water bottle, now empty.')"
idic[bottle][2][use] = {}
idic[bottle][2][combine] = {}
idic[bottle][2][drink] = "print wr('''It's empty now, I'm afraid. You'll have to go thirsty.''')"


idic[powder][1][look] = "print wr('A small vial containing an unspecified amount of powdered StrongForce Energy Refresher. The label warns you not to take more than four teaspoons of powder a day.')"
idic[powder][1][open] = "print wr('You open the vial and sniff the powder. Smells kind of lemony. You screw the lid back on.')"
idic[powder][1][use] = {'bottomrm':{},'inv':{}}
idic[powder][1][use]['bottomrm'][pauli] = """print wr('''Pauli lights up when he sees you have the powder.

'Wonderful!' he says. 'But now the problem is, it can only be taken in liquid form. The powder on its own does me no good whatsoever. So I must ask you to do a little more work for me, and bring me the StrongForce in drink form.' ''')"""
idic[powder][1][combine] = {
    teaspoon: """print wr('''You carefully measure out four teaspoons of StrongForce powder -- the prescribed amount -- and throw away the excess. The vial now contains exactly the right amount of powder. Having no more need for the teaspoon, you discard it.''')
states['inv'][powder] = 2
states['inv'][teaspoon] = 0""",
    bottle: """print wr('''You can't just go pouring an indiscriminate amount of powder into your bottle. Have you seen what excessive energy drink consumption can do to your heart?''')"""
    }
idic[powder][1][use]['inv'][bottle] = copy.deepcopy(idic[powder][1][combine][bottle])
idic[powder][1][use]['inv'][teaspoon] = copy.deepcopy(idic[powder][1][combine][teaspoon])
idic[powder][2][look] = "print wr('A small vial containing exactly four teaspoons of powdered StrongForce energy refresher.')"
idic[powder][2][open] = "print wr('You open the vial and sniff the powder. Smells kind of lemony. You screw the lid back on.')"
idic[powder][2][use] = {'bottomrm':{},'inv':{}}
idic[powder][2][use]['bottomrm'][pauli] = """print wr('''Pauli lights up when he sees you have the powder.

'Wonderful!' he says. 'But now the problem is, it can only be taken in liquid form. The powder on its own does me no good whatsoever. So I must ask you to do a little more work for me, and bring me the StrongForce in drink form.' ''')"""
idic[powder][2][combine] = {
    bottle: """print wr('You pour the StrongForce powder into your water bottle and swirl it around some. You hear an energetic fizzing coming from the bottle. Perfect.')
states['inv'][bottle] = 0
states['inv'][powder] = 0
states['inv'][refresher] = 1"""
    }
idic[powder][2][use]['inv'][bottle] = copy.deepcopy(idic[powder][2][combine][bottle])


idic[refresher][1][look] = "print wr('A water bottle full of StrongForce refresher, fizzing away.')"
idic[refresher][1][use] = {'bottomrm':{},'strangerm':{},'downrm':{},'inv':{}}
idic[refresher][1][use]['bottomrm'][pauli] = """print wr('''Pauli's face fills with glee.

'This is truly splendid!' he says. 'Nothing gets me going like StrongForce!'

He takes the bottle from you, unscrews the lid, and downs the contents in one long gulp. He wipes his mouth and throws the bottle back to you.

'Yes, oh yes! Feel the surge!' he says. He shivers, bounces up and down on the spot a couple of times, then, with a great yelping and yodelling, bounds up the steep staircase with ease.

He disappears through the trapdoor. A few moments pass, in which you can hear rustling from upstairs. You scratch your elbow. Then Pauli's voice floats down from above:

'Before you leave, friend, why don't you pop up here. I have something to give you for your hard work.' ''')
states['inv'][refresher] = 0
states['inv'][bottle] = 2
states['bottomrm'][pauli] = 4
states['bottomrm'][roomd] = 3
states['toprm'][pauli] = 1
states['toprm'][roomd] = 3
states['toprm'][chair] = 2
states['toprm'][drawer] = 6
states['toprm'][desk] = 2
"""
idic[refresher][1][use]['downrm'][gellmann] = """print wr('''You offer Gell-Mann the energy drink. 'Oh, thank you,' he says. 'But I really have as much energy as I need.' ''')"""
idic[refresher][1][use]['strangerm'][dirac] = """print wr('''You offer Dirac the energy refresher. His eyes widen. 'What is this!' he shouts. 'Some kind of insult? Harridan! Begone, fiend!' ''')"""
idic[refresher][1][drink] = "print wr('''You'd better not drink it. That would make Pauli very unhappy.''')"


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
idic[teaspoon][1][use]['strangerm']['no_ob'] = "print wr('''A magical feeling comes over you as you wave the teaspoon around the room. Dirac is unimpressed.''')"
idic[teaspoon][1][combine] = {
    powder: """print wr('''You carefully measure out four teaspoons of StrongForce powder -- the prescribed amount -- and throw away the excess. The vial now contains exactly the right amount of powder. Having no more need for the teaspoon, you discard it.''')
states['inv'][powder] = 2
states['inv'][teaspoon] = 0"""
    }
idic[teaspoon][1][use]['inv'][powder] = copy.deepcopy(idic[teaspoon][1][combine][powder])


idic[seashell][1][look] = "print wr('A Dirac seashell. It glows with an eerie power and vibrates softly.')"
idic[seashell][1][use] = {'strangerm':{},'downrm':{},'bottomrm':{},'muneurm':{},'inv':{}}
idic[seashell][1][use]['downrm'][gellmann] = """print wr(''''Beautiful, a Dirac seashell,' Gell-Mann says, glancing up from his hadrons. 'You enjoy that.' ''')"""
idic[seashell][1][use]['bottomrm'][pauli] = """print wr(''''Oh, yes, the seashell,' Pauli says. 'It is Dirac's. I snuck it away from him for a joke. But it is bad luck, that thing. Perhaps it is responsible for my current predicament.' ''')"""
idic[seashell][1][use]['strangerm'][dirac] = """print wr('''Dirac's eyes nearly bug out of his head.

'My ... my seashell!' he says. 'You found it! Praise you, strange interloper.' ''')"""
idic[seashell][1][use]['muneurm'][feynman] = """print wr(''''Neato,' says Feynman.''')"""
idic[seashell][1][listen] = "print wr('''Gingerly, you put the Dirac seashell to your ear. You hear a strange whistling: the roaring song of the negative particles.''')"

idic[paperclip][1][look] = "print wr('A metal paperclip.')"
idic[paperclip][1][use] = {'inv':{}}
idic[paperclip][1][bend] = """print wr('You straighten the paperclip.')
states['inv'][paperclip] = 2"""
idic[paperclip][2][look] = "print wr('A straightened metal paperclip.')"
idic[paperclip][2][use] = {'inv':{}}
idic[paperclip][2][bend] = """print wr('''If you bend it any more, you'll break it.''')"""
