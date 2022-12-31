#
# Advent of Code 2017
# Bryan Clair
#
# Day 10
# -- updated 2022 for Python3
#
import sys
sys.path.append("../../Advent 2022")
import aocutils
sys.path.append("..")
from knothash import Rope

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

# Part one
lengths = [int(x) for x in inputlines[0].split(',')]
r = Rope(256)
r.round(lengths)
print('part 1:',r.rope[0]*r.rope[1])

# Part two
lengths = [ord(x) for x in inputlines[0]] + [17, 31, 73, 47, 23]
r = Rope(256)
for t in range(64):
    r.round(lengths)
print('part 2:',r.dense())
