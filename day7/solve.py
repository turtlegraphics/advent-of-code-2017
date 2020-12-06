#
# Advent of Code 2017
# Bryan Clair
#
# Day 07
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

tree = {}
weights = {}
rootq = {}

for line in inputlines:
    node = line.split('->')
    nodename, pweight = node[0].split()
    weight = int(pweight[1:-1])
    weights[nodename] = weight
    try:
        children = [x.strip() for x in node[1].split(',')]
        tree[nodename] = children
        for c in children:
            rootq[c] = False
    except IndexError:
        tree[nodename] = []
        pass

for w in weights.keys():
    try:
        rootq[w]
    except:
        root = w

print 'part1:', root


def vote(weights):
    """Return the correct weight for a list."""
    if len(weights) == 0:
        return None
    if len(weights) == 1:
        return weights[0]
    if weights[0] == weights[1]:
        return weights[0]
    if weights[0] == weights[2]:
        return weights[0]
    assert(weights[1] == weights[2])
    return weights[1]

def findbad(node):
    weight = weights[node]
    found = None
    childweights = [findbad(c) for c in tree[node]]
    correct = vote(childweights)
    for i in range(len(tree[node])):
        w = childweights[i]
        weight += w
        if w != correct:
            badnode = tree[node][i]
            print w,'needs to be',correct
            print 'node',badnode,'has weight',weights[badnode]
            print 'it should have weight',weights[badnode] + correct - w
            sys.exit()
    return weight

findbad(root)
