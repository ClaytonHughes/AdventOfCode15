from collections import Counter
import sys

visits = Counter()
rvisits = Counter()

with open(sys.argv[1], 'r') as f:
    instructions = f.read()

move = {
    '^': lambda x, y: (x, y+1),
    'v': lambda x, y: (x, y-1),
    '<': lambda x, y: (x-1, y),
    '>': lambda x, y: (x+1, y)
}

def visit(x,y):
    visits[(x,y)] += 1

def rvisit(x,y):
    rvisits[(x,y)] += 1

x = 0
y = 0
sx = 0
sy = 0
rx = 0
ry = 0

visit(x,y)
visit(rx, ry)
turn = 0
for i in instructions:
    # santa-only
    x, y = move[i](x,y)
    visit(x,y)

    # santa-team
    if turn == 0:
        sx, sy = move[i](sx,sy)
        rvisit(sx,sy)
        turn = 1
    else:
        rx, ry = move[i](rx, ry)
        rvisit(rx,ry)
        turn = 0

print 'santa total visits: %i' % len(visits)
print 'robo team total visits: %i' % len(rvisits)