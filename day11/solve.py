#
# Advent of Code 2017
# Bryan Clair
#
# Day 11
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

kidpath = inputlines[0].split(',')

# Grid:
# 
#  NW  N
#  SW    NE
#      S SE
#
#
steps = {
    'n' : (0,1),
    's' : (0,-1),
    'nw' : (-1,1),
    'se' : (1,-1),
    'sw' : (-1,0),
    'ne' : (1,0)
}

def griddist(x,y):
    """Returns distance from origin on hex grid"""
    diag = 0
    if (x > 0 and y < 0):
        diag = -min(abs(x),abs(y))
    if (x < 0 and y > 0):
        diag = min(abs(x),abs(y))
    return abs(diag) + abs(x + diag) + abs(y - diag)

kx,ky = (0,0)

far = 0

for d in kidpath:
    dx,dy = steps[d]
    kx += dx
    ky += dy
    dist = griddist(kx,ky)
    if dist > far:
        far = dist

# Test grid distance function.. all of these are 3 steps away from (0,0)
test = [(3,0),(1,2),(2,1),(0,3),(-1,3),(-2,3),(-3,3),(-3,2),(-3,1),
        (-3,0),(-2,-1),(-1,-2),(0,-3),(1,-3),(2,-3),(3,-3),(3,-2),(3,-1)]
for (x,y) in test:
    assert(griddist(x,y) == 3)

print 'part 1:', dist
print 'part 2:', far



