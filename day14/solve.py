#
# Advent of Code 2017
# Bryan Clair
#
# Day 14
#
import sys
import os
sys.path.append("..")
import aocutils
from knothash import knothash

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

key = inputlines[0]

def makehashes(key):
    # get hashes from file for speed
    hashfile = 'hashes-'+key+'.txt'
    if os.path.isfile(hashfile):
        return [x.strip() for x in open(hashfile).readlines()]

    # generate hashes, print them for user to copy into file
    h = []
    for row in range(128):
        text = key + '-' + str(row)
        x = knothash(text)
        print x
        h.append(x)
    return h

def part1(hashes):
    bitson = {
        '0':0,'1':1,'2':1,'3':2,
        '4':1,'5':2,'6':2,'7':3,
        '8':1,'9':2,'a':2,'b':3,
        'c':2,'d':3,'e':3,'f':4
        }

    used = 0
    for hash in hashes:
        for c in list(hash):
            used += bitson[c]

    return used

hashes = makehashes(key)

print 'Part 1:',part1(hashes)
