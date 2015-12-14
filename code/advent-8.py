import sys
import re

trace = True

if len(sys.argv) == 1:
    strings = ['""']
    strings.append('"abc"')
    strings.append('"aaa\\"aaa"')
    strings.append('"\\x27"')

else:
    with open(sys.argv[1]) as f:
        strings = f.read().splitlines()

def code_chars(s):
    return len(s)

def memory_chars(s):
    s = s[1:-1]
    collapse_quotes = s.replace('\\"','~')
    collapse_slashes = collapse_quotes.replace('\\\\','*')
    return len(collapse_slashes) - 3 * collapse_slashes.count('\\x')

def encode_chars(s):
    explode_slashes = s.replace('\\','\\\\')
    explode_quotes = explode_slashes.replace('"','\\"')
    enquote = '"%s"' % explode_quotes
    if trace:
        print"    explode: %s" % enquote
    return len(enquote)


code_size = 0
memory_size = 0
inflate_size = 0

for s in strings:
    code_size += code_chars(s)
    memory_size += memory_chars(s)
    inflate_size += encode_chars(s)
    if trace:
        print "code len: %i mem size: %i inflate: %i [%s]" % \
            (code_chars(s), memory_chars(s), encode_chars(s), s)

print code_size - memory_size
print inflate_size - code_size

--
Clayton Hughes