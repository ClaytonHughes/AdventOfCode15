import sys

trace = False
trace = True
if len(sys.argv) == 1:
    trace = True
    commands = ["turn on 0,0 through 999,999"]
    commands.append("toggle 0,0 through 999,0")
    commands.append("turn off 499,499 through 500,500")
    commands.append("toggle 0,0 through 3,0")
else:
    with open(sys.argv[1]) as f:
        commands = f.readlines()

lights = [[0 for x in range(1000)] for x in range(1000)]
nlights = [[0 for x in range(1000)] for x in range(1000)]

class Corner:
    def __init__(self, c):
        self.x = int(c[0])
        self.y = int(c[1])

class CommandBuilder:
    def __init__(self):
        self.corners = []

    def state(self, state):
        if state not in 'on, off, toggle':
            raise Exception('bad command %s' % state)
        self.state = state

    def corner(self, corner):
        int_corner = tuple(corner.split(','))
        if len(int_corner) != 2:
            raise Exception('ill-formed corner: %s' % int_corner)
        if 2 <= len(self.corners):
            raise Exception('too many corners!')
        self.corners.append(int_corner)

    def build(self):
        if self.state is None or len(self.corners) != 2:
            raise Exception('Builder incomplete...')
        return Command(self.corners, self.state)

class Command:
    toggle = [1,0]

    def __init__(self, corners, state):
        self.state = state
        self.low_corner = Corner(corners[0])
        self.high_corner = Corner(corners[1])

    def do(self, lights):
        for i in range(self.low_corner.x, self.high_corner.x + 1):
            for j in range(self.low_corner.y, self.high_corner.y + 1):
                lights[i][j] = self.apply_state(lights[i][j])

    def do_nordic(self, lights):
        for i in range(self.low_corner.x, self.high_corner.x + 1):
            for j in range(self.low_corner.y, self.high_corner.y + 1):
                lights[i][j] = self.apply_nordic(lights[i][j])

    def apply_state(self, light):
        if self.state == 'off':
            return 0
        elif self.state == 'on':
            return 1
        else:
            return Command.toggle[light]

    def apply_nordic(self, light):
        if self.state == 'off':
            return max(0, light - 1)
        elif self.state == 'on':
            return light + 1
        else:
            return light + 2

def parse_command(cmd):
    bits = cmd.split()
    bob = CommandBuilder()
    if bits[0] == 'turn':
        bits = bits[1:]
    if trace:
        print 'command: "%s" ' % cmd
        print "bits: %s " % bits
    bob.state(bits[0])
    bob.corner(bits[1])
    bob.corner(bits[3])
    return bob.build()

def lights_on():
    total = 0
    for i in lights:
        for j in i:
            if 1 <= j:
                total += 1
    return total

def total_brightness():
    total = 0
    for i in nlights:
        for j in i:
            total += j
    return total

trace_count = 0
for c in commands:
    c = c.strip('\n')
    cmd = parse_command(c)
    cmd.do(lights)
    cmd.do_nordic(nlights)
    if trace:
        print '%s: lights on: %i (brightness: %i)' % (c, lights_on(), total_brightness())
        trace_count += 1
    if trace and 8 < trace_count:
        trace = False

# 418954 was too high
# 400410 is right
print "lights on: %i" % lights_on()
print "total brightness: %i" % total_brightness()