import sys
import re

dependency = {}
resolved = {}
trace = False

def munge_input(f):
    inputs = f.splitlines()
    for i in inputs:
        pre, post = i.split(' -> ')
        dependency[post] = pre

if len(sys.argv) == 1:
    trace = True
    munge_input("""123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""")
else:
    with open(sys.argv[1]) as f:
        munge_input(f.read())

binary_funcs = {}
binary_funcs['AND'] = lambda l,r: ((l & r) & 0xffff)
binary_funcs['OR'] = lambda l,r: ((l | r) & 0xffff)
binary_funcs['LSHIFT'] = lambda l,r: ((l << r) & 0xffff)
binary_funcs['RSHIFT'] = lambda l,r: ((l >> r) & 0xffff)

def resolve(operand, depth):
    if re.search(r'[a-z]+', operand):
        if operand not in resolved:
            resolved[operand] = find_value(operand, depth)
        return resolved[operand]
    else:
        return int(operand)

def parse(pre, depth):
    command = pre.split()
    if len(command) == 1:
        return resolve(command[0], depth)
    elif len(command) == 2:
        if command[0] != 'NOT':
            raise Exception('unknown unary command %s' % command[0])
        return (~resolve(command[1], depth) & 0xffff)
    else:
        if len(command) != 3:
            raise Exception('command too long %s' % command)
        if command[1] not in binary_funcs:
            raise Exception('unknown binary operand %s' % command[1])
        l = resolve(command[0], depth)
        r = resolve(command[2], depth)
        return binary_funcs[command[1]](l, r)

def find_value(x, depth=0):
    if trace:
        print "%s%s depends on %s" % (' ' * depth, x, dependency[x])
    return parse(dependency[x], depth + 1)

if len(sys.argv) == 1:
    for v in "defghixy":
        print "%s: %i" % (v, find_value(v))
else:
    v = sys.argv[2]
    new_b = find_value(v)
    print "%s: %i" % (v, new_b)
    resolved = { sys.argv[3]: new_b}
    new_a = find_value(v)
    print "%s': %i" % (v, new_a)
