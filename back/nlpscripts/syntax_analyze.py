import nltk
nltk.download('averaged_perceptron_tagger')
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.data import load


def to_json(tag:list) -> str:
    json = "["
    for tagged_token in tag:
        json += "{\"word\":\"" + tagged_token[0] + "\",\"type\":\"" + tagged_token[1] + "\"},"
    json = json[:-1] + "]"
    return json

def syntax_analyze(text:str) -> str:
    sent_tokens = word_tokenize(text)
    return to_json(nltk.pos_tag(sent_tokens))

# print(syntax_analyze("""EPISODE 1 THE PHANTOM MENACE

# Turmoil has engulfed the Galactic Republic. The taxation of trade routes to
# outlaying star systems is in dispute.
# Hoping to resolve the matter with a blockade of deadly battleships, the
# greedy Trade Federation has stopped all shipping to the small planet of
# Naboo.
# While the congress of the Republic endlessly debates this alarming chain of
# events, the Supreme Chancellor has secretly dispatched two Jedi Knights,
# the guardians of peace and justice in the galaxy, to settle the
# conflict.....

# PAN DOWN to reveal a small space cruiser heading TOWARD CAMERA at great
# speed. PAN with the cruiser as it heads towardthe beautiful green planet of
# Naboo, which is surrounded by hundreds of Trade Federation battleships.

# INT. REPUBLIC CRUISER - COCKPIT


# In the cockpit of the cruise, the CAPTAIN and PILOT maneuver closer to one
# of the battleships.

# QUI-GON : (off screen voice) Captain.

# The Captain turns to an unseen figure sitting behind her.

# CAPTAIN : Yes, sir?
# QUI-GON : (V.O) Tell them we wish to board at once.
# CAPTAIN : Yes, sir.

# The CAPTAIN looks to her view screen, where NUTE GUNRAY, a Neimoidian trade
# viceroy, waits for a reply.

# CAPTAIN : (cont'd) With all due respect for the Trade Federation, the
# Ambassodors for the Supreme Chancellor wish to board immediately.
# NUTE : Yes, yes, of coarse...ahhh...as you know, our blockade is perfectly
# legal, and we'd be happy to recieve the Ambassador...Happy to.

# The screen goes black. Out the cockpit window, the sinister battleship
# looms ever closer.

# EXT. FEDERATION BATTLESHIP - DOCKING BAY - SPACE (FX)

# The small space cruiser docks in the enormous main bay of the Federation
# battleship.

# INT. FEDERATION BATTLESHIP - DOCKING BAY - SPACE

# A PROTOCOL DROID, TC-14, waits at the door to the docking bay. Two WORKER
# DROIDS, PK-4 and EG-9 watch.

# PK-4 : They must be important if the Viceroy sent one of those useless
# protocol gearheads to greet them.

# The door opens, and the Republic cruiser can be seen in the docking bay.
# Two darkly robed figures are greeted by TC-14.

# TC-14 : I'm TC-14 at your service. This way, please.

# They move off down the hallway.

# EG-9 : A Republic cruiser! That's trouble...don't you think?
# PR-4 : I'm not made to think."""))
