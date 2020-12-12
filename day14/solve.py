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

def display(hashes):
    for hash in hashes:
        binary = ''
        for c in list(hash):
            binary += format(int(c,16),"04b")
        bits = [c == '1' for c in list(binary)]

        row = ''
        for b in bits:
            row += '#' if b else '.'
        print row

def showregions(rows):
    for row in rows:
        out = ''
        for r in row:
            if r:
                out += str(r)
            else:
                out += '.'
        print out

class Region:
    newid = itertools.count().next
    symbols = '123456789' + string.ascii_letters
    def __init__(self):
        self.id  = Region.newid()
        self.subs = []  # track subregions

    def __str__(self):
        return Region.symbols[self.id % len(Region.symbols)]

    def set_id(self,val):
        self.id = val
        for sub in self.subs:
            sub.set_id(val)

    def join(self,other):
        if self.id < other.id:
#            print str(self) + ' eating ' + str(other)
            self.subs.append(other)
            other.set_id(self.id)
        else:
#            print str(other) + ' eating ' + str(self)
            other.subs.append(self)
            self.set_id(other.id)
            

def part2(hashes):
    oldrow = [None]*128
    rows = []

    for hash in hashes:
        binary = ''
        for c in list(hash):
            binary += format(int(c,16),"04b")
        bits = [c == '1' for c in list(binary)]

        row = []
        for col in range(128):
            if not bits[col]:
                # bit is off, no region here
                row.append(None)
                continue

            # bit is on
            above = (oldrow[col] != None)
            left = False if (col == 0) else bits[col-1]

            if (not left and not above):
                row.append(Region()) # new region begins
                continue

            if (not left and above):
                row.append(oldrow[col]) # connect above
                continue

            if (left and not above):
                row.append(row[col-1]) # connect to left
                continue

            assert(left and above)
            if oldrow[col-1] or (row[col-1].id == oldrow[col].id):
                # above and left already joined
                if (row[col-1].id != oldrow[col].id):
                    rows.append(row)
                    showregions(rows)
                assert(row[col-1].id == oldrow[col].id)
            else:
                # join above and left regions
                oldrow[col].join(row[col-1])

            # connect to above and left
            row.append(oldrow[col])

        # row complete
        rows.append(row)
        oldrow = row

    return rows

hashes = makehashes(key)
print 'Part 1:',part1(hashes)

rows = part2(hashes)
print rows
