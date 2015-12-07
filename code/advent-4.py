import sys
import hashlib

with open(sys.argv[1], 'r') as f:
    key_prefix = f.read()

value = 0
found_five = False
while True:
    m = hashlib.md5()
    m.update(key_prefix)
    m.update(str(value))
    h = m.hexdigest()
    if h.startswith("000000"):
        print "%s: %i" % (h, value)
        break
    if not found_five and h.startswith("00000"):
        print "%s: %i" % (h, value)
        found_five = True
    value += 1