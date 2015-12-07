import sys

packages = []

class Package:
    def __init__(self, dims):
        self.dims = [int(d) for d in dims]
        self.trace = False

    def smallest_side(self):
        small_sides = sorted(self.dims)[:2]
        extra = small_sides[0] * small_sides[1]
        if self.trace:
            print 'extra space is %i %s' % (extra, str(small_sides))
        return extra

    def dimensions(self):
        dims = (2 * self.dims[0] * self.dims[1]) + \
               (2 * self.dims[0] * self.dims[2]) + \
               (2 * self.dims[1] * self.dims[2])
        if self.trace:
            print 'dimensions are %i %s' % (dims, str(self.dims))
        return dims

    def set_trace(self, do_trace):
        self.trace = do_trace

    def ribbon_perimeter(self):
        small_sides = sorted(self.dims)[:2]
        ribbon = 2 * (small_sides[0] + small_sides[1])
        if self.trace:
            print 'perimeter is %i %s' % (ribbon, str(small_sides))
        return ribbon

    def ribbon_volume(self):
        ribbon = self.dims[0] * self.dims[1] * self.dims[2]
        if self.trace:
            print 'volume is %i %s' % (ribbon, str(self.dims))
        return ribbon

with open(sys.argv[1],'r') as f:
    for line in f:
        packages.append(Package(line.split('x')))

total = 0
ribbon = 0
for p in packages:
    if total == 0:
        p.set_trace(True)
    if p.dims == [1, 10, 1]:
        p.set_trace(True)
    total += p.dimensions() + p.smallest_side()
    ribbon += p.ribbon_perimeter() + p.ribbon_volume()
    if p.trace:
        print

print 'paper: %i' % total
print 'ribbon: %i' % ribbon