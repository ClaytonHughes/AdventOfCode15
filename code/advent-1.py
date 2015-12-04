import sys

with open(sys.argv[1],'r') as f:
    text = f.read()

print 'final floor: %i' % (text.count('(') - text.count(')'))

floor = 0
count = 0
for i in text:
    count += 1
    if i == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        break

print 'first negative floor: %i' % count