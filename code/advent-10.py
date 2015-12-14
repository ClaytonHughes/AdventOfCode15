import sys

if len(sys.argv) == 1:
    digits = ['1', '11', '21', '1211', '111221']
else:
    with open(sys.argv[1]) as f:
        digits = f.read().split()

def look_and_say(digits, times):
    seq = digits
    for t in range(times):
        next_seq = ''
        count = 1
        for i in range(len(seq)):
            if i != len(seq) -1 and seq[i] == seq[i+1]:
                count += 1
            else:
                next_seq += '%i%s' % (count, seq[i])
                count = 1
        seq = next_seq
    return seq


print digits
if len(sys.argv) == 1:
    times = 1
elif len(sys.argv) == 3:
    times = int(sys.argv[2])
else:
    times = 40

for d in digits:
    output = look_and_say(d, times)
    print '%s: %s... %i' % (d, output[:10], len(output))