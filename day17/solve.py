#
# Advent of Code 2017
# Bryan Clair
#
# Day 17
#

# Picking up again some years later, switching to Python3

from argparse import ArgumentParser
def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose",
                        action = "count",
                        dest = "verbose",
                        default = 1,
                        help = "Set verbosity level (-v, -vv, -vvv,...)")
    parser.add_argument("-q", "--quiet",
                        action = "store_const",
                        const = 0,
                        dest = "verbose",
                        help = "Suppress output.")
    
    parser.add_argument("-p", "--part",
                        action="store",
                        dest = "part",
                        default = 1,
                        type = int,
                        help = "Which part of the problem to solve (1 or 2)")
    
    parser.add_argument("file",
                        nargs = "?",
                        default = "input.txt",
                        help = "Problem input file (optional).")
    args = parser.parse_args()
    if args.verbose > 2:
        print(args)

    return args


args = parse_args()

myinput = 380

# part 1

buf = [0]
val = 1
pos = 0

stop = 2017

while val <= stop:
    pos = (pos + myinput) % len(buf)
    pos += 1
    buf.insert(pos,val)
    val += 1

print('part 1:',buf[pos+1])

# part 2

zeropos = 0
afterzero = None

buflen = 1
val = 1
pos = 0

stop = 50000000

while val <= stop:
    if (val-1) % 10000000 == 0:
        print(5 - val // 10000000, '..', end=' ', flush=True)
    pos = (pos + myinput) % buflen
    if pos == zeropos:
        afterzero = val
    elif pos < zeropos:
        zeropos += 1
        
    pos += 1
    buflen += 1
    val += 1

print('0')
print('part 2:',afterzero)


