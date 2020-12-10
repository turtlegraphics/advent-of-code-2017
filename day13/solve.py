#
# Advent of Code 2017
# Bryan Clair
#
# Day 13
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

scanners = []   # using a list of tuples was *much* faster than a dict
for line in inputlines:
    d, r = [int(x) for x in line.split(':')]
    scanners.append((r,d))
scanners.sort() # put faster sentinels first.. not much effect since
                # the input file was already almost sorted by range

# Part 1
severity = 0
for r,d in scanners:
    badtime = 2*(r-1)
    if d % badtime == 0:
        severity += d*r
print 'part 1:',severity

# Part 2
def caught(delay):
    for r,d in scanners:
        if (d+delay) % (2*(r-1)) == 0:
            return True
    return False

import time
t0 = time.time()
delay = 0
inc = 1
if (2,1) in scanners:
    # this sentinel  will catch all the odd delays, so we need only
    # check the evens
    inc = 2
    if (3,2) in scanners:
        # this sentinel will catch all delays == 2 (mod 4) so we need only
        # check the multiples of 4
        inc = 4

while caught(delay):
    delay += inc
t1 = time.time()
print "part 2: %d (%0.2f seconds runtime)" % (delay,t1-t0)

