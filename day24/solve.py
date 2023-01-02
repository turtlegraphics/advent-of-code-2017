#
# Advent of Code 2017
# Bryan Clair
#
# Day 24
#

# Picking up again some years later, switching to Python3
import sys
sys.path.append('../../Advent 2022')
from aocutils import *

args = parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

loops = set()
used = set()
edges = {}

for i,line in enumerate(inputlines):
    v1,v2 = [int(x) for x in line.split('/')]
    if v1 < v2:
        v1,v2 = v2,v1
    e = (v1,v2)
    
    if v1 == v2:
        loops.add(e)
        
    if v1 not in edges:
        edges[v1] = []
    if v2 not in edges:
        edges[v2] = []
    edges[v1].append(e)
    if v1 != v2:
        edges[v2].append(e)

def weight(edge):
    v1,v2 = edge
    return v1+v2

maxdepth = 0
best_at_maxdepth = 0

def best_bridge(start,depth=0,sofar=0):
    """Return the best bridge you can build starting at vertext start.
    depth tracks how many edges used.
    sofar tracks how much strenght we've built so far."""
    
    # print(' '*depth+'visiting',start,end=':')
    # find unused edges
    myedges = []
    for e in edges[start]:
        if e not in used:
            myedges.append(e)

    #print(' '*depth,myedges)

    if not myedges:
        global maxdepth
        global best_at_maxdepth
        if depth > maxdepth:
            maxdepth = depth
            best_at_maxdepth = sofar
        elif depth == maxdepth:
            if sofar > best_at_maxdepth:
                best_at_maxdepth = sofar

    # use any loops - not really worth the effort, runs a smidge faster
    for e in myedges:
        if e in loops:
            used.add(e)
            best = weight(e) + best_bridge(start, depth+1, sofar+weight(e))
            used.remove(e)
            return best

    # try each edge
    best = 0
    for e in myedges:
        v1,v2 = e
        next = v2 if (v1 == start) else v1
        used.add(e)
        s = weight(e) + best_bridge(next, depth+1, sofar+weight(e))
        used.remove(e)
        if s > best:
            best = s

    return best

print('part 1:',best_bridge(0))
print('part 2:',best_at_maxdepth)
