#
# Advent of Code 2017
# Bryan Clair
#
# Day 20
#

# Picking up again some years later, switching to Python3
import sys
sys.path.append('../../Advent 2022')
from aocutils import *

args = parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

import re
format = r"p=<#,#,#>, v=<#,#,#>, a=<#,#,#>"
format = format.replace('#','(-?\d+)')
parser = re.compile(format)

particles = []

amin = 100000
slowest = None

for i,line in enumerate(inputlines):
    vals = [int(x) for x in parser.match(line).groups()]
    particles.append(vals)
    a = Point3d(vals[6:9])
    if a.manabs() < amin:
        amin = a.manabs()
        slowest = i

print('part 1:',slowest)

def collide(i,j):
    """Return time at which i,j collide"""
    time = 0

    dp = Point3d(i[0:3]) - Point3d(j[0:3])
    dv = Point3d(i[3:6]) - Point3d(j[3:6])
    da = Point3d(i[6:9]) - Point3d(j[6:9])
    
    while dp.dot(dv) <= 0 or dv.dot(da) < 0:
        if dp.manabs() == 0:
            return time

        time += 1
        dv += da
        dp += dv

    return -1

collisions = [list() for t in range(100)]

print('  working...',end='')
maxt = 0
for i in range(len(particles)):
    if i % 100 == 0:
        print(9-i//100,end=' ',flush=True)
    for j in range(i):
        t = collide(particles[i],particles[j])
        if t > 0:
            if t > maxt:
                maxt = t
            collisions[t].append((i,j))
print()

remaining = set(range(len(particles)))

for t in range(maxt+1):
    destroyed = set()
    for (i,j) in collisions[t]:
        if (i in remaining) and (j in remaining):
            destroyed.add(i)
            destroyed.add(j)
    # print(len(destroyed),'destroyed at time',t)
    for i in destroyed:
        remaining.remove(i)

print('part 2:',len(remaining))


