# This Python file uses the following encoding: utf-8

from gametext import *

#MAP

smdmap = {
0: [" "," "],
1: ["+  S T A N D A R D","    M O D E L    D U N G E O N  +"],
2: ["   ‾ ‾ ‾ ‾ ‾ ‾ ‾ ‾","    ‾ ‾ ‾ ‾ ‾    ‾ ‾ ‾ ‾ ‾ ‾ ‾   "],
'A': [" ","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"," "],
'B': ["|","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","%","|"],
'Y': [" ","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾","‾"," "],
'ZA': [" "," "],
'ZB': ["(x: LOCKED DOOR  |  $: STAIRS  |  @: YOUR LOCATION)"]
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
'C': u"|%%%%%%%%%%%%%%%%%%%%%%%|‾‾‾‾‾‾‾|%%%%%%%%%%%%%%%%%|",
'D': u"|%|‾‾‾‾‾‾‾|%%|‾‾‾‾‾‾‾|%%|      $|%%%|‾‾‾‾‾‾‾|%%%%%|",
'E': u"|%|       |%%|       |%%|_______|%%%|   γ   |%%%%%|",
'F': u"|%|       |%%|__   __|%%%%%%%%%%%%%%|_______|%%%%%|",
'G': u"|%|==| |==|%%%  |x|  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'H': u"|%|       |__|‾‾   ‾‾|__|‾‾‾‾‾‾‾|%%%|‾‾‾‾‾‾‾|%%%%%|",
'I': u"|%|                            $|%%%|   g   |%%%%%|",    
'J': u"|%|_______|‾‾|__   __|‾‾|_______|%%%|_______|%%%%%|",
'K': u"|%%%%%%%%%%%%%%%| |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'L': u"|%%%%/‾‾‾‾\__|‾‾   ‾‾‾‾‾‾‾‾‾‾‾|_____|‾‾‾‾‾‾‾‾‾‾‾|%|",
'M': u" >>        __                  xxxx      ???    |%|",
'N': u"|%%%%\____/  |__   ___________|‾‾‾‾‾|___________|%|",
'O': u"|%%%%%%%%%%%%%%%| |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'P': u"|%|‾‾‾‾‾‾‾|__|‾‾   ‾‾|__|‾‾‾‾‾‾‾|%%%|‾‾‾‾‾‾‾|%%%%%|",
'Q': u"|%|   νe    x    νμ   x     ντ  |%%%|   Z   |%%%%%|",
'R': u"|%|_______|‾‾|__   __|‾‾|_______|%%%|_______|%%%%%|",
'S': u"|%%%%%%%%%%%%%  |x|  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%|",
'T': u"|%|‾‾‾‾‾‾‾|__|‾‾   ‾‾|__|‾‾‾‾‾‾‾|%%%|‾‾‾‾‾‾‾|%%%%%|",
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

def mapdebug():
    k = showmap.keys()
    k.sort()
    for i in k:
        i = ''.join(showmap[i])
        print i

# DICTIONARY OF MAP DATA

mdic = {
    "entryrm": {'pos':['M',7]},
    "mainrm": {'pos':['M',17]},
    "strangerm": {'pos':['J',17]},
    "charmrm": {'pos':['F',17]},
    "downrm": {'pos':['I',8]},
    "uprm": {'pos':['F',6]},
    "toprm": {'pos':['D',30]},
    "bottomrm": {'pos':['I',26]},
    "muneurm": {'pos':['P',17]},
    "eneurm": {'pos':['Q',9]},
    "tneurm": {'pos':['Q',26]},
    "elecrm": {'pos':['U',8]},
    "muonrm": {'pos':['T',17]},
    "taurm": {'pos':['U',26]},
    "photonrm": {'pos':['D',38]},
    "gluonrm": {'pos':['I',38]},
    "Zrm": {'pos':['Q',38]},
    "Wrm": {'pos':['U',38]},
    "higgsrm": {'pos':['M',39]}
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
    'D': range(12,23),
    'E': range(12,23),
    'F': range(12,23)
    }

mdic["downrm"][1] = {
    'D': range(2,11),
    'E': range(2,11),
    'F': range(2,11),
    'G': range(2,11),
    'H': range(2,12),
    'I': range(2,12),
    'J': range(2,12)
    }

mdic["toprm"][1] = {
    'C': range(24,33),
    'D': range(24,33),
    'E': range(24,33)
    }

mdic["bottomrm"][1] = {
    'H': range(23,33),
    'I': range(23,33),
    'J': range(23,33)
    }

mdic["muneurm"][1] = {
    'P': range(12,23),
    'Q': range(12,23),
    'R': range(12,23),
    'S': range(14,21)
    }

mdic["eneurm"][1] = {
    'P': range(2,12),
    'Q': range(2,12),
    'R': range(2,12)
    }

mdic["tneurm"][1] = {
    'P': range(23,33),
    'Q': range(23,33),
    'R': range(23,33)
    }

mdic["elecrm"][1] = {
    'T': range(2,12),
    'U': range(2,12),
    'V': range(2,12)
    }

mdic["muonrm"][1] = {
    'T': range(12,23),
    'U': range(12,23),
    'V': range(12,23)
    }

mdic["taurm"][1] = {
    'T': range(23,33),
    'U': range(23,33),
    'V': range(23,33)
    }

mdic["photonrm"][1] = {
    'D': range(36,44),
    'E': range(36,44),
    'F': range(36,44)
    }

mdic["gluonrm"][1] = {
    'H': range(36,44),
    'I': range(36,44),
    'J': range(36,44)
    }

mdic["Zrm"][1] = {
    'P': range(36,44),
    'Q': range(36,44),
    'R': range(36,44)
    }

mdic["Wrm"][1] = {
    'T': range(36,44),
    'U': range(36,44),
    'V': range(36,44)
    }

mdic["higgsrm"][1] = {
    'L': range(35,48),
    'M': range(35,48),
    'N': range(35,48)
    }
