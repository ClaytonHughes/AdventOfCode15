import sys
import re

if len(sys.argv) == 1:
    inputs = ['hijklmmn','abbceffg','abcdefgh','ghijklmn']
else:
    with open(sys.argv[1]) as f:
        inputs = [f.read()]

def increment_char(char, skip_bad=True):
    # wrap
    if skip_bad and char == 'z':
        return 'a'
    # skip bad letters entirely.
    if skip_bad and char == 'h':
        return 'j'
    if skip_bad and char == 'k':
        return 'm'
    if skip_bad and char == 'n':
        return 'p'
    return chr(ord(char) + 1)

def scrub_pass(text):
    chars = list(text)
    floor_found = False
    for i in range(len(chars)):
        if floor_found:
            chars[i] = 'a'
        elif chars[i] is 'i' or chars[i] is 'l' or chars[i] is 'o':
            floor_found = True
            chars[i] = increment_char(chars[i])
    return ''.join(chars)



def increment_pass(text):
    chars = list(text)
    for i in range(1, len(chars) + 1):
        chars[-i] = increment_char(chars[-i])
        if chars[-i] != 'a':
            break
    return ''.join(chars)

def meets_straight_rule(text, count):
    for i in range(0, len(text)-count):
        range_slice = text[i:i+count]
        straight_found = True
        for j in range(1, count):
            if range_slice[j] != increment_char(range_slice[j-1], skip_bad=False):
                straight_found = False
        if straight_found:
            return True
    return False

def meets_pair_rule(text):
    return re.search(r'(.)\1.*(.)\2', text) is not None

def is_valid(text):
    return meets_pair_rule(text) and meets_straight_rule(text, 3)

def find_next(text):
    password = increment_pass(scrub_pass(text))
    while not is_valid(password):
        password = increment_pass(password)
    return password


for i in inputs:
    new_pass = find_next(i)
    print "'%s' (%s %s) -> '%s' (%s %s) -> %s" % (i, meets_straight_rule(i, 3), meets_pair_rule(i), new_pass, meets_straight_rule(new_pass, 3), meets_pair_rule(new_pass), find_next(new_pass))