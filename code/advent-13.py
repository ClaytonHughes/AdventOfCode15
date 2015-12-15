import sys
from itertools import permutations

table = {}

with open(sys.argv[1]) as f:
    haps = f.readlines()

for h in haps:
    name, _, direction, count, _, _, _, _, _, _, target = h.split()
    target = target[:-1]
    if name not in table.keys():
        table[name] = {}
    if direction == 'lose':
        count = int(count) * -1
    else:
        count = int(count)
    table[name][target] = count

def score(arrangement):
    score = 0
    for i in range(len(arrangement)):
        seat = arrangement[i]
        target = arrangement[i-1]
        if seat != 'self' and target != 'self':
            score += table[seat][target] + table[target][seat]
    return score


max_happiness = float("-inf")
for p in permutations(table.keys()):
    happiness = score(p)
    max_happiness = max(max_happiness, happiness)

print max_happiness

table['self'] = {}

max_happiness = float("-inf")
for p in permutations(table.keys()):
    happiness = score(p)
    max_happiness = max(max_happiness, happiness)

print max_happiness
