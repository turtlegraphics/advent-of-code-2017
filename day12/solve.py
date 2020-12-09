#
# Advent of Code 2017
# Bryan Clair
#
# Day 12
#
import sys
sys.path.append("..")
import aocutils
import networkx as nx

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

G = nx.Graph()

for line in inputlines:
    srcs,dests = line.split(' <-> ')
    src = int(srcs)
    dest = [int(x) for x in dests.split(',')]
    for d in dest:
        G.add_edge(src,d)

count = 0
for h in nx.connected_components(G):
    count += 1
    if 0 in h:
        print 'part 1:', len(h)

print 'part 2:',count
