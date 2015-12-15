import sys

class Reindeer:
    def __init__(self, name, speed, duration, rest_duration):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest_duration = rest_duration
        self.distance = 0
        self.state = 'flying'
        self.duration_left = self.duration
        self.points = 0

    def tick(self, count):
        for _ in range(count):
            if self.state == 'flying':
                self.tick_fly()
            else:
                self.tick_rest()

    def tick_fly(self):
        self.distance += self.speed
        self.duration_left -= 1
        if self.duration_left == 0:
            self.duration_left = self.rest_duration
            self.state = 'resting'

    def tick_rest(self):
        self.duration_left -= 1
        if self.duration_left == 0:
            self.duration_left = self.duration
            self.state = 'flying'

    def __str__(self):
        return '%i %i %s [%s]' % (self.points, self.distance, self.name, self.state)

def process_speeds(speeds):
    names = []
    for s in speeds:
        tokens = s.split()
        name = tokens[0]
        speed = int(tokens[3])
        duration = int(tokens[6])
        rest_duration = int(tokens[-2])
        names.append(Reindeer(name, speed, duration, rest_duration))
    return names

def score_points(reindeer):
    max_dist = 0
    winners = []
    for r in reindeer:
        if max_dist < r.distance:
            max_dist = r.distance
            winners = [r.name]
        elif max_dist == r.distance:
            winners.append(r.name)
    for r in reindeer:
        if r.name in winners:
            r.points += 1

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        speeds = f.readlines()
else:
    speeds = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
              'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']

reindeer = process_speeds(speeds)

time = 0
def go_to(val):
    global time
    ticks = val - time 
    time = val
    print '\n%ss:' % time
    for _ in range(ticks):
        for r in reindeer:
            r.tick(1)
        score_points(reindeer)
    for r in reindeer:
        print r


go_to(2503)
