import sys
from itertools import combinations_with_replacement

with open(sys.argv[1]) as f:
    stats = f.readlines()

class Ingredient:
    def __init__(self, name, cap, dur, fla, tex, cal):
        self.name = name
        self.cap = cap
        self.dur = dur
        self.fla = fla
        self.tex = tex
        self.cal = cal

def score(recipe):
    cap = 0
    dur = 0
    fla = 0
    tex = 0
    cal = 0
    for i in recipe:
        cap += i.cap
        dur += i.dur
        fla += i.fla
        tex += i.tex
        cal += i.cal
    if cap <= 0 or dur <= 0 or fla <= 0 or tex <= 0:
        return 0
    if cal != 500:
        return 0
    return cap*dur*fla*tex

ingreds = {}

for s in stats:
    tokens = s.split()
    name = tokens[0][:-1]
    cap = int(tokens[2][:-1])
    dur = int(tokens[4][:-1])
    fla = int(tokens[6][:-1])
    tex = int(tokens[8][:-1])
    cal = int(tokens[10])

    ingreds[name] = Ingredient(name, cap, dur, fla, tex, cal)

recipe = []

high_score = 0
for i in combinations_with_replacement(ingreds.values(), 100):
    rs = score(i)
    high_score = max(high_score, rs)

print high_score

