# This Python file uses the following encoding: utf-8

from gametext import *


inv_txt = """
---------------------------------------------------

                I N V E N T O R Y
                - - - - - - - - -

              This is your inventory.
       You can look, use, or combine items;
     inv to reprint this list, or return/exit.
"""
inv2_txt = """
---------------------------------------------------
"""


## Inventory Dic

idic = {}


idic[bongos] = {
    0: {},
    1: {}
    }

idic[tripod] = copy.deepcopy(idic[bongos])
idic[up_bongos] = copy.deepcopy(idic[bongos])
idic[rope] = copy.deepcopy(idic[bongos])
idic[teaspoon] = copy.deepcopy(idic[bongos])

#idic[key_a] = copy.deepcopy(idic[bongos])
#idic[key_b] = copy.deepcopy(idic[bongos])
#idic[key_c] = copy.deepcopy(idic[bongos])

idic[bongos][1]['d'] = "print w('A set of cheap bongos with blue and red stars painted on the side.')"
idic[bongos][1]['use'] = {
    feynman: """print w('''You pull the bongos out of your bag. Feynman's eyes light up and he jumps from his chair.

'Hey, brilliant! I love the bongos.' He takes the drums off you, and turns them over in his hands. 'But wait a second.' He cocks his head to one side. 'I can't play these. There's no stand. You can't play the drums sitting down. You gotta move your body, that's where the rhythm comes from.' He hands the drums back to you and returns to his seat.''')"""
    }
idic[bongos][1]['combine'] = {
    tripod: """print w('You jam the bongos down onto the top of the tripod. Not a perfect fit, but it holds firm. You now have a serviceable set of upright bongos.')
states['inv'][bongos] = 0
states['inv'][tripod] = 0
states['inv'][up_bongos] = 1"""
    }

idic[tripod][1]['d'] = "print w('A rusty old tripod.')"
idic[tripod][1]['use'] = {
    feynman: """print w("'Why the hell are you showing me this?' Feynman scowls.")"""
    }
idic[tripod][1]['combine'] = {
    bongos: """print w('You jam the bongos down onto the top of the tripod. Not a perfect fit, but it holds firm. You now have a serviceable set of upright bongos.')
states['inv'][bongos] = 0
states['inv'][tripod] = 0
states['inv'][up_bongos] = 1"""
    }

idic[up_bongos][1]['d'] = "print w('A cheap pair of bongos wedged onto the top of a rusty old tripod.')"
idic[up_bongos][1]['use'] = {
    feynman: """print w('''You pull the bongos out of your bag. Feynman's eyes light up and he jumps from his chair.

'Hey, brilliant! I love the bongos.' He takes the drums off you, extends the legs of the tripod, and sets it on the ground. 'Watch this, fella,' he says, and begins to play. The music is odd. But he's well and truly distracted, so you can finally get through that door.''')
states['muneurm'][feynman] = 3
states['muneurm'][s_door] = 2
states['muneurm'][e_door] = 2
states['muneurm'][w_door] = 2
states['inv'][up_bongos] = 0"""
    }

idic[rope][1]['d'] = "print w('A long coil of rope.')"
idic[rope][1]['use'] = {
    gellmann: """print w("'Great,' Gell-Mann says, 'so you got yourself a rope. Now what?'")""",
    hadrons: """print w("You attach one end of the rope to the handle of the briefcase, using a highly secure knot passed down to you by your father (now deceased).")
states["inv"][rope] = 0
states['downrm'][rope] = 3
states['downrm'][gellmann] = 3
states['downrm'][roomd] = 2
states['uprm'][hadrons] = 2
states['uprm'][rope] = 1"""
    }

idic[teaspoon][1]['d'] = "print w('A silver teaspoon.')"
idic[teaspoon][1]['use'] = {
    }
