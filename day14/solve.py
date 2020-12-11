#
# Advent of Code 2017
# Bryan Clair
#
# Day 14
#
import sys
sys.path.append("..")
import aocutils
from knothash import knothash

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

key = inputlines[0]

bitson = {
    '0':0,'1':1,'2':1,'3':2,
    '4':1,'5':2,'6':2,'7':3,
    '8':1,'9':2,'a':2,'b':3,
    'c':2,'d':3,'e':3,'f':4
    }

used = 0
for row in range(128):
    text = key + '-' + str(row)
    hash = knothash(text)
    for c in list(hash):
        used += bitson[c]

print 'Part 1:',used
