#
# Advent of Code 2017
# Bryan Clair
#
# Day --
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]
lengths = [int(x) for x in inputlines[0].split(',')]

n = 256

rope = range(n)

pos = 0
skip = 0

def printrope():
    if args.verbose <= 1:
        return
    for i in range(n):
        if pos == i:
            print '[%d]' % rope[i],
        else:
            print ' %d ' % rope[i],
    print

printrope()    
for l in lengths:
    head = pos
    tail = (pos + l - 1) % n
    swaps = l//2
    while swaps > 0:
        temp = rope[head]
        rope[head] = rope[tail]
        rope[tail] = temp
        swaps -= 1
        head = (head + 1) % n
        tail = (tail - 1) % n
    pos = (pos + l + skip) % n
    skip += 1
    printrope()

print 'part 1:',rope[0]*rope[1]
