#
# Advent of Code 2017
# Bryan Clair
#
# Day 09
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

river = open(args.file).read().strip()

level = 1
garbage = False
ignore = False

score = 0
garbagecount = 0

for i in range(len(river)):
    c = river[i]

    if args.verbose > 2:
        print i,c

    if ignore:
        ignore = False
        continue
    if c == '!':
        ignore = True
        continue

    if garbage:
        if c == '>':
            garbage = False
        else:
            garbagecount += 1
        continue

    if c == '<':
        garbage = True
        if args.verbose > 1:
            print i,'garbage'
        continue

    if c == '{':
        score += level
        level += 1
        if args.verbose > 1:
            print i,'new level',level,'group'
        continue

    if c == '}':
        level -= 1
        continue

    if c == ',':
        continue

    print i,'bad character: "'+c+'"'
    assert(False)

print 'score:',score
print 'garbage chars:',garbagecount


    
