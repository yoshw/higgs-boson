# This Python file uses the following encoding: utf-8

import copy

#MAP

smdmap = {
0: [" "," "],
1: ["+  S T A N D A R D","    M O D E L    D U N G E O N  +"],
2: ["   ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾","    ‾ ‾ ‾ ‾ ‾    ‾ ‾ ‾ ‾ ‾ ‾ ‾   "],
'A': [" ","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"," "],
'B': ["|","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","|"],
'Y': [" ","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾"," "]
}
smdmap['C'] = copy.deepcopy(smdmap['B'])
smdmap['D'] = copy.deepcopy(smdmap['B'])
smdmap['E'] = copy.deepcopy(smdmap['B'])
smdmap['F'] = copy.deepcopy(smdmap['B'])
smdmap['G'] = copy.deepcopy(smdmap['B'])
smdmap['H'] = copy.deepcopy(smdmap['B'])
smdmap['I'] = copy.deepcopy(smdmap['B'])
smdmap['J'] = copy.deepcopy(smdmap['B'])
smdmap['K'] = copy.deepcopy(smdmap['B']) + ["     N"]
smdmap['L'] = copy.deepcopy(smdmap['B']) + ["     ^"]
smdmap['M'] = copy.deepcopy(smdmap['B']) + [" W < + > E"]
smdmap['N'] = copy.deepcopy(smdmap['B']) + ["     v"]
smdmap['O'] = copy.deepcopy(smdmap['B']) + ["     S"]
smdmap['P'] = copy.deepcopy(smdmap['B'])
smdmap['Q'] = copy.deepcopy(smdmap['B'])
smdmap['R'] = copy.deepcopy(smdmap['B'])
smdmap['S'] = copy.deepcopy(smdmap['B'])
smdmap['T'] = copy.deepcopy(smdmap['B'])
smdmap['U'] = copy.deepcopy(smdmap['B'])
smdmap['V'] = copy.deepcopy(smdmap['B'])
smdmap['W'] = copy.deepcopy(smdmap['B'])
smdmap['X'] = copy.deepcopy(smdmap['B'])

#SHOW MAP

#NB: overline = E2 80 BE, gamma = CE B3, mu = CE BC, tau = CF 84, nu = CE BD

showmap = {
'A': u" _________________________________________________ ",
'B': u"|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'C': u"|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'D': u"|%|‾‾‾‾‾‾‾|%%|‾‾‾‾‾‾‾|%%|‾‾‾‾‾‾‾|%%%|‾‾‾‾‾‾‾|%%%%%|",
'E': u"|%|   u   |%%|   c   |%%|   t   |%%%|   γ   |%%%%%|",
'F': u"|%|       |%%|__   __|%%|__   __|%%%|_______|%%%%%|",
'G': u"|%|==| |==|%%%  |x|  %%%%  | |  %%%%%%%%%%%%%%%%%%|",
'H': u"|%|       |__|‾‾   ‾‾|__|‾‾   ‾‾|%%%|‾‾‾‾‾‾‾|%%%%%|",
'I': u"|%|   d          s    x     b   |%%%|   g   |%%%%%|",
'J': u"|%|_______|‾‾|__   __|‾‾|_______|%%%|_______|%%%%%|",
'K': u"|%%%%%%%%%%%%%%%| |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'L': u"|%%%%/‾‾‾‾\__|‾‾   ‾‾‾‾‾‾‾‾‾‾‾|_____|‾‾‾‾‾‾‾‾‾‾‾|%|",
'M': u" >>        __                  xxxxx     ???    |%|",
'N': u"|%%%%\____/  |__   ___________|‾‾‾‾‾|___________|%|",
'O': u"|%%%%%%%%%%%%%%%| |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'P': u"|%|‾‾‾‾‾‾‾|__|‾‾   ‾‾|__|‾‾‾‾‾‾‾|%%%|‾‾‾‾‾‾‾|%%%%%|",
'Q': u"|%|   νe    x    νμ   x     ντ  |%%%|   Z   |%%%%%|",
'R': u"|%|__   __|‾‾|__   __|‾‾|__   __|%%%|_______|%%%%%|",
'S': u"|%%  | |  %%%%  |x|  %%%%  | |  %%%%%%%%%%%%%%%%%%|",
'T': u"|%|‾‾   ‾‾|__|‾‾   ‾‾|__|‾‾   ‾‾|%%%|‾‾‾‾‾‾‾|%%%%%|",
'U': u"|%|   e          μ          τ   |%%%|   W   |%%%%%|",
'V': u"|%|_______|‾‾|_______|‾‾|_______|%%%|_______|%%%%%|",
'W': u"|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'X': u"|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'Y': u" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ "
}

#MAIN MAP FUNCTION

def mapp(rm):
    userpos(rm)

    k = smdmap.keys()
    k.sort()
    for i in k:
        i = ''.join(smdmap[i])
        print i

    smdmap[mdic[rm]['pos'][0]][mdic[rm]['pos'][1]] = showmap[mdic[rm]['pos'][0]][mdic[rm]['pos'][1]]

def sqshow(y,x):
    #    print y, x, "before: ", smdmap[y][x], "after: ", showmap[y][x]
    smdmap[y][x] = showmap[y][x]

def rmshow(rm):
    k = mdic[rm][1].keys()
    k.sort()
    for y in k:
        for x in mdic[rm][1][y]:
            sqshow(y,x)

def userpos(rm):
    smdmap[mdic[rm]['pos'][0]][mdic[rm]['pos'][1]] = '@'

# DICTIONARY OF MAP DATA

mdic = {
    "entryrm": {'pos':['M',7]},
    "mainrm": {'pos':['M',17]},
    "strangerm": {'pos':['J',17]},
    "charmrm": {},
    "downrm": {'pos':['I',8]},
    "uprm": {'pos':['F',6]},
    "toprm": {},
    "bottomrm": {},
    "muneurm": {'pos':['P',17]},
    "eneurm": {},
    "tneurm": {},
    "elecrm": {},
    "muonrm": {},
    "taurm": {},
    "photonrm": {},
    "gluonrm": {},
    "Zrm": {},
    "Wrm": {},
    "higgsrm": {}
    }

mdic["entryrm"][1] = {
    'L': range(5,12),
    'M': range(0,12),
    'N': range(5,12)
    }

mdic["mainrm"][1] = {
    'K': range(16,19),
    'L': range(12,35),
    'M': range(12,35),
    'N': range(12,35),
    'O': range(16,19)
    }

mdic["strangerm"][1] = {
    'G': range(14,21),
    'H': range(12,23),
    'I': range(12,23),
    'J': range(12,23)
    }

mdic["charmrm"][1] = {
    'L': [5,6,7,8,9,10,11],
    'M': [0,1,2,3,4,5,6,7,8,9,10,11],
    'N': [5,6,7,8,9,10,11]
    }

mdic["downrm"][1] = {
    'D': range(2,12),
    'E': range(2,12),
    'F': range(2,12),
    'G': range(2,12),
    'H': range(2,13),
    'I': range(2,13),
    'J': range(2,13)
    }

mdic["toprm"][1] = {
    'L': [5,6,7,8,9,10,11],
    'M': [0,1,2,3,4,5,6,7,8,9,10,11],
    'N': [5,6,7,8,9,10,11]
    }

mdic["bottomrm"][1] = {
    'L': [5,6,7,8,9,10,11],
    'M': [0,1,2,3,4,5,6,7,8,9,10,11],
    'N': [5,6,7,8,9,10,11]
    }

mdic["muneurm"][1] = {
    'L': [5,6,7,8,9,10,11],
    'M': [0,1,2,3,4,5,6,7,8,9,10,11],
    'N': [5,6,7,8,9,10,11]
    }
