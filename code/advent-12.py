import sys
import json

with open(sys.argv[1]) as f:
    blob = json.load(f)

def maybe_int(str):
    try:
        return int(str)
    except ValueError:
        return 0

def sum_keys(object):
    total = 0
    for i in object.keys():
        total += maybe_int(i)
    return total

def sum_list(lst, pred):
    total = 0
    for i in lst:
        total += sum_item(i, pred)
    return total

def sum_item(item, pred=None):
    if type(item) is type([]):
        return sum_list(item, pred)
    elif type(item) is type({}):
        if pred is not None and pred(item):
            return 0
        return sum_list(item.keys(), pred) + sum_list(item.values(), pred)
    else:
        return maybe_int(item)

def is_red(item):
    return u'red' in item.values()

print sum_item(blob)
print sum_item(blob, is_red)