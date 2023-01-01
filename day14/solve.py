#
# Advent of Code 2017
# Bryan Clair
#
# Day 14
#
import sys
import os
import itertools
import string
# Picking up again some years later, switching to Python3
sys.path.append('../../Advent 2022')
import aocutils
sys.path.append('..')
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
        print(x)
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

def makegrid(hashes):
    disk = aocutils.Grid()
    for r,hash in enumerate(hashes):
        binary = ''
        for hexdig in list(hash):
            binary += format(int(hexdig,16),"04b")
        for c,bit in enumerate(binary):
            if bit == '1':
                disk[r,c] = 0

    return disk

hashes = makehashes(key)
print('Part 1:',part1(hashes))

disk = makegrid(hashes)

region = 0
for p in disk:
    if disk[p] == 0:
        region += 1
        dist,prev = disk.dijkstra(p)
        for q in dist:
            disk[q] = region

# disk.display(blank='.')
print('Part 2:',region)
