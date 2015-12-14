import sys

class Route:
    def __init__(self, start):
        self.places = [start]
        self.distance = [0]

    def visit(self, place, distance):
        self.places.append(place)
        self.distance.append(int(distance))

    def pop(self):
        self.distance = self.distance[:-1]
        last_place = self.places[-1]
        self.places = self.places[:-1]
        return last_place

    def __str__(self):
        return ' -> '.join(self.places) + ' = %i' % sum(self.distance)

def prep_distances():
    distances = {}
    if len(sys.argv) == 1:
            atlas = ['London to Dublin = 464',
                     'London to Belfast = 518',
                     'Dublin to Belfast = 141']
    else:
        with open(sys.argv[1]) as f:
            atlas = f.read().splitlines()

    for d in atlas:
        start, _, dest, _ , dist = d.split()
        if start not in distances:
            distances[start] = {}
        distances[start][dest] = int(dist)
        if dest not in distances:
            distances[dest] = {}
        distances[dest][start] = int(dist)
    return distances

def print_route(visit_list):
    global smallest_distance
    global largest_distance
    global smallest_route
    global largest_route

    distance = 0
    for i in range (0, len(visit_list) - 1):
        distance += distances[visit_list[i]][visit_list[i+1]]

    print ' -> '.join(visit_list) + ' = %i ' % distance
    if distance < smallest_distance:
        smallest_distance = distance
        smallest_route = ' -> '.join(visit_list)
    if distance > largest_distance:
        largest_distance = distance
        largest_route = ' -> '.join(visit_list)

def enumerate_routes(visiting, visited):
    if not visiting:
        print_route(visited)
        return

    for next_stop in visiting:
        to_visit = list(visiting)
        to_visit.remove(next_stop)
        will_have_visited = list(visited)
        will_have_visited.append(next_stop)
        enumerate_routes(to_visit, will_have_visited)

smallest_distance = float('inf')
smallest_route = 'n/a'
largest_distance = float('-inf')
largest_route = 'n/a'
distances = prep_distances()
visited = []
enumerate_routes(distances.keys(), [])
print ' %i (%s)' % (smallest_distance, smallest_route)
print ' %i (%s)' % (largest_distance, largest_route)