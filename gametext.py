# This Python file uses the following encoding: utf-8

import copy

prmpt = "\n >> "

fail_txt = "I'm sorry, I don't understand that."

title_txt = """
===================================================
*****            - -   - - - - - -            *****
*****      +:+   I N   S E A R C H   +:+      *****
*****               O F   T H E               *****
***** ___  ___  ____  ________  ________  ________*
*****/  / /  /*/   /*/  _____/*/  _____/*/  _____/*
****/  /_/  /*/   /*/  /____ */  /____ */  /____ **
***/  __   /*/   /*/  / 7  /*/  / 7  /*/____   /***
**/  / /  /*/   /*/  /_/  /*/  /_/  /*_____/  /****
*|__/ /__/*|___/*|_______/*|_______/*|_______/*****
*                                             *****
*****          +:+   B O S O N   +:+          *****
*****                - - - - -                *****
===================================================

            Y O S H U A   W A K E H A M
            & D A V I D   W A K E H A M

                    (ɔ) 2 0 1 2
       A L L   R I G H T S   R E V E R S E D


"""

gameover_txt = """
Your atoms slowly disintegrate and merge
once more with the infinite.

      - - - -   - - - -
+:+   G A M E   O V E R   +:+
      - - - -   - - - -
"""

instruct_txt = """
---------------------------------------------------

              I N S T R U C T I O N S
              - - - - - - - - - - - -

This is a very simple game. Move from room to room,
interact with objects, and solve puzzles. When you
see the '>> ' prompt, enter your text. Try the following:

        - look
        - talk
        - go
        - use
        - open
        - get
        - inv/-entory
        - instr/-uct/-ions to see this again
        - exit/quit

Good luck, have fun, and remember not to stare at
the screen for too long. Your eyes will go square.

---------------------------------------------------
"""

menu_txt = """\
                [1]  START GAME
                [2]  INSTRUCTIONS
                [3]  EXIT
"""

start_txt = """
You trudge uphill through the thick, soupy fog. As you crest the hill, the mist clears and before you rises the ominous blockiness of the Standard Model Dungeon. Your long journey is approaching its end -- but you have a little farther to go before you can claim the elusive, powerful Higgs boson.

You brace yourself. This will not be easy. You take your water bottle from your laptop bag -- emptied out in case you need to carry anything -- and take a sip. Shoving it back in, you walk the final hundred metres to the dungeon and push open the grand steel doors."""



# VARIABLE WORDING

get = ('get', 'take', 'pickup', 'grab')
look = ('look', 'inspect')
talk = ('talk', 'chat', 'jaw')
opn = ('open', 'unwrap')
use = ('use', 'activate')
go = ('go', 'walk')
combine = ('combine', 'blend', 'mix')

roomd = ('room', 'env', 'environment')

sagan = ('carl sagan', 'carl', 'sagan')
feynman = ('richard feynman', 'richard', 'dick', 'feynman')
fermi = ('enrico fermi', 'enrico', 'fermi')
dirac = ('paul dirac', 'paul', 'dirac')
gellmann = ('murray gell-mann', 'murray', 'gell-mann', 'gellmann')
#pauli
#einstein
#higgs

chair = ('chair', 'armchair', 'seat')
fireplace = ('fireplace', 'fire', 'grate', 'hearth')
bongos = ('bongos', 'bongo', 'drum')
tripod = ('tripod', 'camera tripod', 'camera stand')
up_bongos = ('upright bongos', 'bongos', 'upright')
wardrobe = ('wardrobe', 'robe', 'cupboard', 'chest of drawers')
rope = ('rope', 'bale', 'cord', 'coil', 'cable')
teaspoon = ('teaspoon', 'spoon')
hadrons = ('briefcase full of hadrons', 'briefcase', 'case', 'hadrons')

key_a = ('key a', 'first key')
key_b = ('key b', 'second key')
key_c = ('key c', 'third key')

door = ('door', 'portal')
portal = ('portal', 'entrance')
n_door = ('north door', 'north', 'n')
e_door = ('east door', 'east', 'e')
w_door = ('west door', 'west', 'w')
s_door = ('south door', 'south', 's')
staircase = ('staircase', 'stairs', 'spiral staircase', 'spiral stairs', 'stairway')

# MAIN DICTIONARY

dic = {}


# ENTRYRM

dic["entryrm"] = {}

dic["entryrm"][roomd] = {
    0: {},
    1: {},
    2: {},
    3: {}
    }

dic["entryrm"][e_door] = copy.deepcopy(dic["entryrm"][roomd])
dic["entryrm"][w_door] = copy.deepcopy(dic["entryrm"][roomd])
dic["entryrm"][chair] = copy.deepcopy(dic["entryrm"][roomd])
dic["entryrm"][sagan] = copy.deepcopy(dic["entryrm"][roomd])

dic["entryrm"][roomd][0][look] = """print w('''You stumble into the entrance hall, the enormous double doors closing behind you. You suddenly find yourself upside down, legs kicking at the air, your laptop bag hanging down from your shoulder into empty space. You are in a small spherical chamber with no appreciable gravity.

You look around. In the eastern section of the curved wall, opposite the front entrance, is another, smaller steel door. The only other object in the room is a plush armchair a few metres away from you. Carl Sagan is sitting in the armchair, calmly reading a book. He looks up.

'Welcome to the Standard Model Dungeon, friend,' he says. 'Don't be afraid. The goal you seek is almost at hand. There are just a few final challenges you must face. But I am confident you'll attain your prize.' ''')
states["entryrm"][roomd] = 1
rmshow('entryrm')"""
dic["entryrm"][roomd][1][look] = "print w('You are in a small, gravityless spherical chamber. On the west side, the entrance to the Standard Model Dungeon. On the east, a large steel door. Carl Sagan floats in an armchair nearby.')"
dic["entryrm"][roomd][2][look] = """print w('''As the glow fades, you feel the floor drop from under your feet and realise you've materialised back in the weightless entrance chamber. Carl Sagan is still floating nearby. He looks up from his book.

'Hello again,' he says. 'I see you're one step closer to the boson. Astounding. Well, don't let me keep you.' ''')"""
dic["entryrm"][roomd][3][look] = """print w('''As usual, you find yourself back in the entrance chamber. This time, though, Sagan looks unusually animated. He throws his book down.

'This is it, friend!' he says. 'You have all the keys -- now there's nothing to stop you from claiming the boson! Quickly, no time to lose!' ''')"""


dic["entryrm"][e_door][1] = {
    look: "print w('A largeish steel door.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('You try the handle on the heavy steel door. It is unlocked, and opens slowly.')
newrm = 'mainrm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["entryrm"][e_door][1][use] = dic["entryrm"][e_door][1][go] = copy.deepcopy(dic["entryrm"][e_door][1][opn])
dic["entryrm"][e_door][2] = copy.deepcopy(dic["entryrm"][e_door][1])
dic["entryrm"][e_door][3] = copy.deepcopy(dic["entryrm"][e_door][1])
dic["entryrm"][e_door][3][look] = "print w('''Don't just look at it, go through the damn thing!''')"


dic["entryrm"][w_door][1] = {
    look: "print w('Enormous double doors. The entrance to the dungeon.')",
    talk: "print w('The door remains silent.')",
    opn: "print w('''Hey, what's the big idea? There's no going back now.''')",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["entryrm"][w_door][1][use] = dic["entryrm"][w_door][1][go] = copy.deepcopy(dic["entryrm"][w_door][1][opn])


dic["entryrm"][chair][1] = {
    look: "print w('A high-backed red velour armchair.')",
    talk: "print w('You talk to chairs? Like, regularly?')",
    opn: "print w('''You don't have anything to open it with.''')",
    use: "print w('''Sagan's already using it.''')",
    get: "print w('''I'm afraid you can't do that.''')"
    }
dic["entryrm"][chair][2] = copy.deepcopy(dic["entryrm"][chair][1])
dic["entryrm"][chair][3] = copy.deepcopy(dic["entryrm"][chair][1])
dic["entryrm"][chair][3][look] = "print w('Why would you look at a chair at a time like this?')"


dic["entryrm"][sagan][1] = {
    look: "print w('Carl Sagan: astrophysicist, science communicator, gentleman. Dressed in corduroy. A wry smile plays on his face.')",
    talk: "print w('''Sagan smiles benevolently. 'No point talking to me, friend. I don't have the boson. I suggest you try going through this door to the next room. Seems the logical thing to do.' ''')",
    opn: "print w('''That's just rude.''')",
    use: "print w('''You can't do that.''')",
    get: "print w('''Does anyone really 'get' Carl Sagan?''')"
    }
dic["entryrm"][sagan][2] = copy.deepcopy(dic["entryrm"][sagan][1])
dic["entryrm"][sagan][3] = copy.deepcopy(dic["entryrm"][sagan][1])
dic["entryrm"][sagan][3][look] = "print w('Sagan bounces up and down, pointing at the east door, muttering excitedly.')"
dic["entryrm"][sagan][3][talk] = "Sagan is too excited to talk. He bounces up and down, pointing at the east door."


#MAIN ROOM

dic["mainrm"] = {}

dic["mainrm"][roomd] = {
    0: {},
    1: {},
    2: {},
    3: {}
    }

dic["mainrm"][n_door] = copy.deepcopy(dic["mainrm"][roomd])
dic["mainrm"][e_door] = copy.deepcopy(dic["mainrm"][roomd])
dic["mainrm"][w_door] = copy.deepcopy(dic["mainrm"][roomd])
dic["mainrm"][s_door] = copy.deepcopy(dic["mainrm"][roomd])
dic["mainrm"][staircase] = copy.deepcopy(dic["mainrm"][roomd])
dic["mainrm"][fireplace] = copy.deepcopy(dic["mainrm"][roomd])


dic["mainrm"][roomd][0][look] = """print w('''The steel door slams shut behind you. Mercifully, you find your feet settling to the floor: normal gravity has been restored.

You are in a large, central hall. Its semicylindrical shape makes it feel like a miniature aircraft hangar. At the far east end of the room, directly ahead of you, is another door with a complicated lock. Closer by there are two other doors -- one in the north wall, one in the south. You shout out 'Anybody here?': the only reply is your echo.''')
states["mainrm"][roomd] = 1
rmshow('mainrm')"""
dic["mainrm"][roomd][1][look] = """print w('''You are in a long, hangar-shaped room with doors to the east, west, north and south. The west door leads back to the entrance chamber. The door to the east looks important -- it appears to have a large, complicated lock.''')"""


dic["mainrm"][e_door][1] = {
    look: "print w('An ornate steel door. It seems important.')",
    talk: "print w('The door remains silent.')",
    opn: "print w('There is a very complicated lock on it! More info to come.')",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["mainrm"][e_door][1][use] = dic["mainrm"][e_door][1][go] = copy.deepcopy(dic["mainrm"][e_door][1][opn])

dic["mainrm"][s_door][1] = {
    look: "print w('A black door with a round handle, set in the south wall.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('The door opens easily, and you pass through.')
newrm = 'muneurm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["mainrm"][s_door][1][use] = dic["mainrm"][s_door][1][go] = copy.deepcopy(dic["mainrm"][s_door][1][opn])

dic["mainrm"][n_door][1] = {
    look: "print w('A black door with a round handle, set in the north wall. There is an odd design painted on it: interlocking red, blue and green circles. I wonder what it means.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('The handle turns easily, and you pass through the door.')
newrm = 'strangerm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["mainrm"][n_door][1][use] = dic["mainrm"][n_door][1][go] = copy.deepcopy(dic["mainrm"][n_door][1][opn])

dic["mainrm"][w_door][1] = {
    look: "print w('''The steel door you just came through. You can go back if you like, but I wouldn't recommend it.''')",
    talk: "print w('The door remains silent.')",
    opn: """print w('With an effort, you push open the door and go back to the entrance chamber.')
newrm = 'entryrm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["mainrm"][w_door][1][use] = dic["mainrm"][w_door][1][go] = copy.deepcopy(dic["mainrm"][w_door][1][opn])

"""dic["mainrm"][staircase][1] = {
    look: "print w('A spiral staircase. It must have hundreds of steps.')",
    talk: "print w('That will not work.')",
    opn: "print w('Try using it instead.')",
    use: "print w('Off we go to visit the upper level!')",
    get: "print w('''Hey, you can't do that.''')"
    }"""


# QUARK ROOMS

#CHARM/STRANGE

dic["strangerm"] = {}

dic["strangerm"][roomd] = {
    0: {},
    1: {},
    2: {},
    3: {}
    }

dic["strangerm"][n_door] = copy.deepcopy(dic["strangerm"][roomd])
dic["strangerm"][e_door] = copy.deepcopy(dic["strangerm"][roomd])
dic["strangerm"][w_door] = copy.deepcopy(dic["strangerm"][roomd])
dic["strangerm"][s_door] = copy.deepcopy(dic["strangerm"][roomd])
dic["strangerm"][dirac] = copy.deepcopy(dic["strangerm"][roomd])

dic["strangerm"][roomd][0][look] = """print w('''You close the door behind you quietly. You are in a small room with identical, featureless doors to the west, north and east. In the centre of the room, a tall, thin man with a moustache paces back and forth, muttering to himself. You recognise him as Paul Dirac.

There's something altogether strange about this room, but you can't put your finger on what it is.''')
states["strangerm"][roomd] = 1
rmshow('strangerm')"""
dic["strangerm"][roomd][1][look] = """print w('You are in a small, strange room with identical doors to the west, north and east. In the centre of the room, Paul Dirac paces back and forth.')"""

dic["strangerm"][n_door][1] = {
    look: "print w('A featureless door.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('''As you go to open the door, Dirac quietly intercepts you and pushes you back.

'Tut tut,' he says, not looking you directly in the eyes. 'Not yet.' ''')""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["strangerm"][n_door][1][use] = dic["strangerm"][n_door][1][go] = copy.deepcopy(dic["strangerm"][n_door][1][opn])

dic["strangerm"][e_door][1] = {
    look: "print w('A featureless door.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('''As you go to open the door, Dirac quietly intercepts you and pushes you back.

'Tut tut,' he says, without making eye contact. 'Not yet.' ''')""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["strangerm"][e_door][1][use] = dic["strangerm"][e_door][1][go] = copy.deepcopy(dic["strangerm"][e_door][1][opn])

dic["strangerm"][s_door][1] = {
    look: "print w('The door you just came through.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('With an effort, you push open the door and go back to the central room.')
newrm = 'mainrm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["strangerm"][s_door][1][use] = dic["strangerm"][s_door][1][go] = copy.deepcopy(dic["strangerm"][s_door][1][opn])

dic["strangerm"][w_door][1] = {
    look: "print w('A featureless door.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('''As you open the door, you notice Dirac watching you. He seems to be smiling.''')
newrm = 'downrm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["strangerm"][w_door][1][use] = dic["strangerm"][w_door][1][go] = copy.deepcopy(dic["strangerm"][w_door][1][opn])

dic["strangerm"][dirac][1] = {
    look: "print w('Paul Dirac: a very tall, thin English physicist who predicted the existence of antimatter.')",
    talk: """print w('''You walk over to Dirac and try to grab his attention. He waves one hand absently.

'No no, not now,' he says. 'I can't talk now. It simply isn't possible. There isn't the slightest chance. Please leave me to my thoughts.'

You decide not to bother him further.''')""",
    opn: "print w('''That's just rude.''')",
    use: "print w('''Dirac's uses are many, but they are obscure.''')",
    get: "print w('''Now's not the time to be picking fights with geniuses.''')"
    }


dic["charmrm"] = {}

dic["charmrm"][roomd] = {
    0: {},
    1: {},
    2: {},
    3: {}
    }

dic["charmrm"][s_door] = copy.deepcopy(dic["charmrm"][roomd])


# UP/DOWN

dic["downrm"] = {}

dic["downrm"][roomd] = {
    0: {},
    1: {},
    2: {},
    3: {}
    }

dic["downrm"][n_door] = copy.deepcopy(dic["downrm"][roomd])
dic["downrm"][e_door] = copy.deepcopy(dic["downrm"][roomd])
dic["downrm"][gellmann] = copy.deepcopy(dic["downrm"][roomd])
dic["downrm"][wardrobe] = copy.deepcopy(dic["downrm"][roomd])
dic["downrm"][rope] = copy.deepcopy(dic["downrm"][roomd])
dic["downrm"][teaspoon] = copy.deepcopy(dic["downrm"][roomd])
dic["downrm"][tripod] = copy.deepcopy(dic["downrm"][roomd])
dic["downrm"][hadrons] = copy.deepcopy(dic["downrm"][roomd])

dic["downrm"][roomd][0][look] = """print w('''Yet another smallish, nondescript room. The wallpaper is starting to peel in a few places. Against the west wall is a tall, utilitarian wardrobe, its doors closed.

In the north wall is a strange-looking door -- or rather, a portal. There is no actual door, just an opening that comes about halfway up the wall; you'll have to stoop to go through it. Standing in front of the portal, with his back to you, is a short, hunched man with white hair. As you enter he whirls around.

'Oh, excuse me!' the man says. He's a portly chap with wire-rimmed glasses and a grey suit. You recognise him: it's Murray Gell-Mann.

'Listen,' Gell-Mann says, beckoning with one finger. 'Come over here. You have to help me.'

He turns back to the opening and you consider what to do next. Is it your imagination, or do you feel sort of heavier in here?''')
states["downrm"][roomd] = 1
rmshow('downrm')"""
dic["downrm"][roomd][1][look] = """print w('You are in a small room with a door to the east and an empty portal in the north wall. Murray Gell-Mann is hunched over near the portal. A tall wardrobe stands nearby.')"""
dic["downrm"][roomd][2][look] = """print w('Gell-Mann stands near the portal, looking at you expectantly. The end of the rope trails over the lintel of the portal then arcs down to the ground. The wardrobe stands nearby.')"""
dic["downrm"][roomd][3][look] = """print w('''You are in a small room with a door to the east and an empty portal in the north wall. There's an open wardrobe just near you. Murray Gell-Mann sits in the middle of the room, peering into his briefcase full of hadrons. You're glad you were able to help him out.''')"""

dic["downrm"][gellmann][1] = {
    look: "print w('Murray Gell-Mann: getting old now, but in his day one of the finest theoretical physicists in the world. First postulated the existence of quarks (though George Zweig was doing the same thing simultaneously). Gell-Mann is an avid birdwatcher, collector of antiquities, rancher, and a keen linguist.')",
    talk: """print w('''You walk over towards Gell-Mann. He turns and smiles as he sees you approaching.

'Thank goodness you're here,' he says. 'You can help me. Come here, look through into the next room.' You move past him and look through the portal. The room beyond it seems ordinary, much like the one you're standing in now. You shrug your shoulders.

'Don't you see?' Gell-Mann says, impatiently. 'Look up at the roof!' You look upwards. To your surprise, there's a briefcase stuck to the ceiling.

'You see it?' said Gell-Mann. 'That's my briefcase. It's full of precious, precious hadrons. All my favourite hadrons! I'm too old and weak to get it back. You're young and strong. Can you help me?'

You're not sure what to make of all this. Seems like Gell-Mann might be going a little batty. What sort of weirdo glues their briefcase to the ceiling?''')
states["downrm"][gellmann] = 2
states["downrm"][n_door] = 2
states["downrm"][portal] = 2""",
    opn: "print w('''That's just rude.''')",
    use: "print w('''You cruel person, you.''')",
    get: "print w('''Where would you put him? He sure won't fit in your shoulder bag.''')"
    }
dic["downrm"][gellmann][2] = copy.deepcopy(dic["downrm"][gellmann][1])
dic["downrm"][gellmann][3] = copy.deepcopy(dic["downrm"][gellmann][1])
dic["downrm"][gellmann][4] = copy.deepcopy(dic["downrm"][gellmann][1])
dic["downrm"][gellmann][2][talk] = """print w(''' 'Please help me, friend!' Gell-Mann says. He seems greatly distressed about his missing hadrons.''')"""
dic["downrm"][gellmann][3][talk] = """print w(''' 'Ingenious!' Gell-Mann says. 'I'll help you pull the case through.' ''')"""
dic["downrm"][gellmann][4][talk] = dic["downrm"][gellmann][4][look] = """print w('''Gell-Mann looks absolutely content. 'Oh, my dear hadrons,' he says quietly, peering into the case. 'How I've missed you!' ''')"""

dic["downrm"][e_door][1] = {
    look: "print w('The door you just came through.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('With an effort, you push open the door and go back.')
newrm = 'strangerm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["downrm"][e_door][1][use] = dic["downrm"][e_door][1][go] = copy.deepcopy(dic["downrm"][e_door][1][opn])

dic["downrm"][n_door][1] = {
    look: dic["downrm"][gellmann][1][talk],
    talk: "print w('The portal is silent.')",
    opn: dic["downrm"][gellmann][1][talk],
    get: "print w('''Hey, you can't do that.''')"
    }
dic["downrm"][n_door][1][use] = dic["downrm"][n_door][1][go] = copy.deepcopy(dic["downrm"][n_door][1][opn])
dic["downrm"][n_door][2] = copy.deepcopy(dic["downrm"][n_door][1])
dic["downrm"][n_door][2][look] = "print w('An empty portal leading to another room.')"
dic["downrm"][n_door][2][opn] = dic["downrm"][n_door][2][use] = dic["downrm"][n_door][2][go] = """print w('You stoop and pass through the portal.')
newrm = 'uprm'"""
dic["downrm"][portal] = copy.deepcopy(dic["downrm"][n_door])

dic["downrm"][wardrobe][1] = {
    look: "print w('A tall, unadorned wardrobe. It looks as though it has been here for a long time.')",
    talk: "print w('''It's not saying anything right now.''')",
    opn: """print w('You swing open the old doors of the wardrobe. The inside smells of mothballs and old paint. There are no clothes in here, just an old tripod, a coil of rope, and what appears to be a silver teaspoon.')
states["downrm"][tripod] = 1
states["downrm"][rope] = 1
states["downrm"][teaspoon] = 1
states["downrm"][wardrobe] = 2
""",
    get: "print w('''That's not really feasible. It's a pretty big wardrobe.''')"
    }
dic["downrm"][wardrobe][1][use] = copy.deepcopy(dic["downrm"][wardrobe][1][opn])
dic["downrm"][wardrobe][2] = copy.deepcopy(dic["downrm"][wardrobe][1])
dic["downrm"][wardrobe][2][look] = "print w('A tall, unadorned wardrobe. Its doors stand open. It contains an old tripod, a coil of rope, and a silver teaspoon.')"
dic["downrm"][wardrobe][2][opn] = dic["downrm"][wardrobe][2][use] = "print w('You already opened it.')"
dic["downrm"][wardrobe][3] = copy.deepcopy(dic["downrm"][wardrobe][1])
dic["downrm"][wardrobe][3][look] = "print w('A tall, unadorned wardrobe. Its doors stand open. It once contained an old tripod, a coil of rope, and a silver teaspoon.')"

dic["downrm"][rope][0] = {}
dic["downrm"][rope][1] = {
    look: "print w('A long, cobwebby coil of thick rope.')",
    talk: "print w('''It's not saying anything right now.''')",
    opn: "print w('That makes no sense.')",
    use : "print w('''You can't use it here.''')",
    get: """print w('You brush the cobwebs off the rope and stuff it into your bag.')
states['downrm'][rope] = 2
states['inv'][rope] = 1
states['downrm'][wardrobe] = 3"""
    }
dic["downrm"][rope][2][look] = dic["downrm"][rope][2][talk] = dic["downrm"][rope][2][opn] = dic["downrm"][rope][2][use] = dic["downrm"][rope][2][get] = "print w('The rope is gone. You took it.')"
dic["downrm"][rope][3] = copy.deepcopy(dic["downrm"][rope][1])
dic["downrm"][rope][3][look] = "print w('The trailing end of the long rope. The other end is attached to the briefcase in the other room.')"
dic["downrm"][rope][3][use] = """print w('''You give Gell-Mann the nod and you both grab hold of the rope. Pulling with all your might, you feel the briefcase start to move across the ceiling. You keep pulling and you start to drag it up the wall between the two rooms. With one final, mighty yank, the briefcase climbs over the lintel into this room, and instantly falls to the ground with a thud.

Gell-Mann rushes over, opens the case and peers inside. An eerie glow washes over his face. 'Oh, I can't express how joyful this makes me, sir!' he says.

You're about to leave when Gell-Mann calls out. 'Hang on a minute,' he says. 'I have to give you a reward for being so kind.' He reaches into his pocket and pulls out some small and shiny objects. He deposits them into your outstretched palm.

You inspect his gift: two small glass beads, flecked with strange colours. One marked 'u', the other marked 'd'. Maybe these will come in handy later on?''')
states['downrm'][rope] = 4
states['downrm'][hadrons] = 1
states['downrm'][gellmann] = 4
states['downrm'][roomd] = 3
states['uprm'][hadrons] = 0
states['uprm'][roomd] = 2
states['uprm'][rope] = 0"""
dic["downrm"][rope][3][get] = "print w('''You can't take it.''')"
dic["downrm"][rope][4] = {}
dic["downrm"][rope][4][look] = dic["downrm"][rope][4][talk] = dic["downrm"][rope][4][opn] = dic["downrm"][rope][4][use] = dic["downrm"][rope][4][get] = "print w('''You've done all you can with the rope.''')"

dic["downrm"][tripod][0] = {}
dic["downrm"][tripod][1] = {
    look: "print w('A rusty old three-legged camera stand.')",
    talk: "print w('''It's not saying anything right now.''')",
    opn: "print w('You work the stiff legs of the tripod back and forth -- to little effect.')",
    use : "print w('''What are you going to use it for? You don't have anything to rest on it.''')",
    get: """print w('You fold up the tripod and stuff it into your bag. It pokes you when you walk.')
states['downrm'][tripod] = 2
states['inv'][tripod] = 1
states['downrm'][wardrobe] = 3"""
    }
dic["downrm"][tripod][2][look] = dic["downrm"][tripod][2][talk] = dic["downrm"][tripod][2][opn] = dic["downrm"][tripod][2][use] = dic["downrm"][tripod][2][get] = "print w('The tripod is gone. You took it.')"

dic["downrm"][teaspoon][0] = {}
dic["downrm"][teaspoon][1] = {
    look: "print w('A silver teaspoon.')",
    talk: "print w('''It's not saying anything right now.''')",
    opn: "print w('''It doesn't open.''')",
    use : "print w('''You can't use it here.''')",
    get: """print w('You pick up the spoon and stuff it in your bag.')
states['downrm'][teaspoon] = 2
states['inv'][teaspoon] = 1
states['downrm'][wardrobe] = 3"""
    }
dic["downrm"][teaspoon][2][look] = dic["downrm"][teaspoon][2][talk] = dic["downrm"][teaspoon][2][opn] = dic["downrm"][teaspoon][2][use] = dic["downrm"][teaspoon][2][get] = "print w('The teaspoon is gone. You took it.')"

dic["downrm"][hadrons][0] = {}
dic["downrm"][hadrons][1] = {
    look: "print w('''Gell-Mann's ratty old briefcase. From the outside, it doesn't look anything special, but powerful forces are at work within.''')",
    talk: "print w('''It's not saying anything right now.''')",
    opn: "print w('''Gell-Mann is using it right now.''')",
    use : "print w('''Gell-Mann is using it right now.''')",
    get: "print w('''Gell-Mann is using it right now.''')",
    }



dic["uprm"] = {}

dic["uprm"][roomd] = {
    0: {},
    1: {},
    2: {},
    3: {}
    }

dic["uprm"][s_door] = copy.deepcopy(dic["uprm"][roomd])
dic["uprm"][hadrons] = copy.deepcopy(dic["uprm"][roomd])
dic["uprm"][rope] = copy.deepcopy(dic["uprm"][roomd])

dic["uprm"][roomd][0][look] = """print w(''''What the --!' You're barely over the threshold when you find yourself falling upwards and crashing into the 'ceiling'. You collect yourself, rub your bruised shoulder, and wonder why Gell-Mann didn't warn you.

So, this is another one of those funny gravity rooms. At least that explains why the briefcase is stuck on the ceiling. Looking around, you see that the briefcase is the only thing of interest in the room.''')
states["uprm"][roomd] = 1"""
dic["uprm"][roomd][1][look] = """print w('''A strange room where gravity is reversed, and objects fall up instead of down. Gell-Mann's briefcase full of hadrons lies on the 'floor' nearby. The only way out is the portal back to the previous room, now raised halfway up the south wall.''')"""
dic["uprm"][roomd][2][look] = """print w('A strange room where gravity is reversed, and objects fall up instead of down. The only way out is the portal back to the previous room, now raised halfway up the south wall.')"""

dic["uprm"][hadrons][0] = {}
dic["uprm"][hadrons][1] = {
    look: "print w('''A ratty old briefcase. From the outside, it doesn't look anything special.''')",
    talk: "print w('''It's not saying anything right now.''')",
    opn: "print w('''Better not. Powerful forces are at work inside. Only Gell-Mann can master the hadrons.''')",
    use : "print w('''Better not. Powerful forces are at work inside. Only Gell-Mann can master the hadrons.''')",
    get: """print w('''You try to pick up the case, but you find it to be surprisingly heavy. You can drag it, slowly, but there's no way you can carry it back through the portal.''')"""
    }
dic["uprm"][hadrons][2] = copy.deepcopy(dic["uprm"][hadrons][1])
dic["uprm"][hadrons][2][look] = "print w('''A ratty old briefcase with the rope securely tied to its handle.''')"

dic["uprm"][s_door][1] = {
    look: "print w('An empty doorway, now about two metres off the ground, which leads back to the room you just came from.')" ,
    talk: "print w('The portal is silent.')",
    opn: """print w('You jump up, grab the lintel, and pull yourself through the portal.')
newrm = 'downrm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["uprm"][s_door][1][use] = dic["uprm"][s_door][1][go] = copy.deepcopy(dic["uprm"][s_door][1][opn])
dic["uprm"][portal] = copy.deepcopy(dic["uprm"][s_door])

dic["uprm"][rope][0] = {}
dic["uprm"][rope][1] = {
    look: "print w('''The rope is attached to the handle of the briefcase.''')",
    talk: "print w('''It's not saying anything right now.''')",
    opn: "print w('''Huh?''')",
    use : "print w('''Pulling on the rope, you drag the case over to the wall, but that's as far as you get.''')",
    get: "print w('''That's not a good idea.''')"
    }



# TOP/BOTTOM


# LEPTON ROOMS

# MUON NEUTRINO

dic["muneurm"] = {}

dic["muneurm"][roomd] = {
    0: {},
    1: {},
    2: {},
    3: {}
    }

dic["muneurm"][feynman] = copy.deepcopy(dic["muneurm"][roomd])
dic["muneurm"][tripod] = copy.deepcopy(dic["muneurm"][roomd])
dic["muneurm"][n_door] = copy.deepcopy(dic["muneurm"][roomd])
dic["muneurm"][e_door] = copy.deepcopy(dic["muneurm"][roomd])
dic["muneurm"][w_door] = copy.deepcopy(dic["muneurm"][roomd])
dic["muneurm"][s_door] = copy.deepcopy(dic["muneurm"][roomd])

dic["muneurm"][roomd][0][look] = """print w('''You enter the room, shutting the black door behind you. The room you have entered is quite poky. The ventilation is poor.

There is other shit going on here that I can't be bothered describing right now. The important stuff you need to know is that Richard P. Feynman is sitting on a camping chair in one corner of the room, staring at you over tented fingers. In one other corner of the room is a dusty, disused tripod. There are doors set in the east, west and south walls.''')
states["muneurm"][roomd] = 1"""
dic["muneurm"][roomd][1][look] = """print w('''A little room with Feynman in it and other shit.''')"""

dic["muneurm"][feynman][1] = {
    look: "print w('Dick Feynman: particle physicist, raconteur, man about town. Worked on the atomic bomb. Lived a high life. His hair is shoulder-length, his teeth are yellow, and he wears a shiteater grin at all times.')",
    talk: """print w('''You walk over to Feynman and offer your salutations. His grin widens.

'Hello there, bud,' he says. 'You think you're gettin' into the next room? Think again. Not as long as I'm around.' He folds his arm and grins EVEN WIDER.''')""",
    opn: "print w('''That's just rude.''')",
    use : "print w('''In Standard Model Dungeon, Dick Feynman uses YOU.''')",
    get: "print w('''Sure, he's a skinny guy, but he's wily. Don't underestimate his strength.''')"
    }
dic["muneurm"][feynman][2] = copy.deepcopy(dic["muneurm"][feynman][1])
dic["muneurm"][feynman][3] = copy.deepcopy(dic["muneurm"][feynman][1])
dic["muneurm"][feynman][3][look] = "print w('Feynman is jamming out with his bongos. He looks happy as a pig in shit.')"
dic["muneurm"][feynman][3][talk] = "print w('Feynman is too busy jamming out to talk to you right now.')"

dic["muneurm"][n_door][1] = {
    look: "print w('The door you just came through.')",
    talk: "print w('The door remains silent.')",
    opn: """print w('With an effort, you push open the door and go back to the central room.')
newrm = 'mainrm'""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["muneurm"][n_door][1][use] = dic["muneurm"][n_door][1][go] = copy.deepcopy(dic["muneurm"][n_door][1][opn])
    
dic["muneurm"][s_door][1] = {
    look: "print w('Another mysterious door. Who knows where this one leads?')",
    talk: "print w('The door remains silent.')",
    opn: """print w('''You walk over to the door and reach for the handle, but suddenly Feynman comes from nowhere and pushes you backwards, hard.

'Where do you think you're going, buddy?' he says. 'What a load of guff.' He sits back down.''')""",
    get: "print w('''Hey, you can't do that.''')"
    }
dic["muneurm"][s_door][1][use] = dic["muneurm"][s_door][1][go] = copy.deepcopy(dic["muneurm"][s_door][1][opn])
dic["muneurm"][s_door][2] = copy.deepcopy(dic["muneurm"][s_door][1])
dic["muneurm"][s_door][2][opn] = dic["muneurm"][s_door][2][use] = """print w('With Feynman safely distracted, you open the door easily and pass into the next room.')
newrm = 'entryrm'"""

dic["muneurm"][e_door] = copy.deepcopy(dic["muneurm"][s_door])
dic["muneurm"][w_door] = copy.deepcopy(dic["muneurm"][s_door])




# HIGGS BOSON ROOM
#(beyond locked door)
#And beyond that???


miscroom = {
    "preamble":"Bla bla bla, indeed.\n",
    "shoe boot footwear clog":"It's a ratty old boot-clog, no good to anyone.",
    "dog hound mutt terrier bob":"It's Bob, the master's ratty old fox terrier."
    }
