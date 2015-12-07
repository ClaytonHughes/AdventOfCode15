import sys
import re

strings = []
trace = False
if len(sys.argv) == 1:
    trace = True
#    strings.append('ugknbfddgicrmopn')
#    strings.append('aaa')
#    strings.append('jchzalrnumimnmhp')
#    strings.append('haegwjzuvuyypxyu')
#    strings.append('dvszwmarrgswjxmb')
    strings.append('qjhvhtzxzqqjkmpb')
    strings.append('xxyxx')
    strings.append('uurcxstgmygtbstg')
    strings.append('ieodomkazucvgmuy')
else:
    with open(sys.argv[1], 'r') as f:
        strings = f.readlines()

def has_n_or_more_vowels(str, n):
    vowels = [l for l in str if l in "aeiou"]
    return n <= len(vowels)

def has_double_letter(str):
    return re.search(r'(.)\1', str) is not None

def has_naughty_strings(str):
    return re.search(r'ab', str) is not None or \
           re.search(r'cd', str) is not None or \
           re.search(r'pq', str) is not None or \
           re.search(r'xy', str) is not None

def is_nice(str):
    if trace:
        print str
    vowels = has_n_or_more_vowels(str, 3)
    if trace:
        print "  has n or more vowels: %r" % vowels
    doubles = has_double_letter(str)
    if trace:
        print "  has double letters:   %r" % doubles
    naughty = has_naughty_strings(str)
    if trace:
        print "  has naughty strings:  %r" % naughty
        if vowels and doubles and not naughty:
            print " nice!"
        else:
            print " naughty"
    return vowels and doubles and not naughty

def has_double_pair(str):
    return re.search(r'(..).*\1', str) is not None

def has_sandwich(str):
    return re.search(r'(.).\1', str) is not None

def is_new_nice(str):
    if trace:
        print str
    double_pair = has_double_pair(str)
    if trace:
        print "  has double pair: %r" % double_pair
    sandwich = has_sandwich(str)
    if trace:
        print "  has sandwich:    %r" % sandwich
        if double_pair and sandwich:
            print " (new) nice!"
        else:
            print " (new) naughty"
    return double_pair and sandwich

nice = [s for s in strings if is_nice(s)]
new_nice = [s for s in strings if is_new_nice(s)]

print "old style: %i" % len(nice)
print "new style: %i" % len(new_nice)