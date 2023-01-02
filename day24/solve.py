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
import networkx as nx

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

def best_bridge(start,depth=0):
    """Return the best bridge you can build starting at vertext start."""
    debug(' '*depth+'visiting',start,end=':')
    # find unused edges
    myedges = []
    for e in edges[start]:
        if e not in used:
            myedges.append(e)

    debug(' '*depth,myedges)

    if not myedges:
        return 0

    # use any loops
    for e in myedges:
        if e in loops:
            used.add(e)
            best = weight(e) + best_bridge(start,depth+1)
            used.remove(e)
            return best

    # try each edge
    best = 0
    for e in myedges:
        v1,v2 = e
        next = v2 if (v1 == start) else v1
        used.add(e)
        s = weight(e) + best_bridge(next,depth+1)
        used.remove(e)
        if s > best:
            best = s

    return best

print('part 1:',best_bridge(0))

            
