#
# Advent of Code 2019
# Bryan Clair
#
# Day --
#
import sys
from math import *

def coordinates(s):
    ring = int(sqrt(s))
    if ring % 2 == 0:
        ring -= 1
    if s == ring*ring:
        return ((ring-1)/2,-(ring-1)/2)
    offset = s - ring*ring
    side = offset/(ring + 1)
    mid = (ring + 1)/2
    delta = offset - (ring + 1)*side - mid

    if side == 0: # right side
        return (mid,delta)
    if side == 1: # top side
        return (-delta,mid)
    if side == 2: # left side
        return (-mid,-delta)
    if side == 3: # bottom side
        return (delta,-mid)

if __name__ == "__main__":
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    data = open(filename).readlines()

    input = int(data[0])
    print "Part 1"
    (x,y) = coordinates(input)
    print "coordinates (%d,%d)" % (x,y)
    print "distance:", abs(x) + abs(y)

    # Test coordinate grid
    print
    print "Grid test"
    grid = {}
    for i in range(1,50):
        grid[coordinates(i)] = i
    for y in range(3,-4,-1):
        for x in range(-3,4):
            print "%4d" % grid[(x,y)],
        print

    # Stress test
    print
    print "Stress test"
    neighbors = [(-1, 1), (0, 1), (1,1),
                 (-1,0)         , (1,0),
                 (-1,-1), (0,-1), (1,-1)]
    grid = {}
    grid[(0,0)] = 1
    v = 0
    i = 2
    while v <= input:
        v = 0
        (x,y) = coordinates(i)
        for (dx,dy) in neighbors:
            if (x+dx,y+dy) in grid:
                v += grid[(x+dx,y+dy)]
        grid[coordinates(i)] = v
        i += 1

    for y in range(4,-5,-1):
        for x in range(-4,5):
            if (x,y) in grid:
                print "%6d" % grid[(x,y)],
            else:
                print "   .  ",
        print

    print "First larger value:",v
