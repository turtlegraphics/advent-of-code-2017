#
# Advent of Code 2017
# Bryan Clair
#
# Day --
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

inputlines = [x.strip() for x in open(args.file).readlines()]

A0 = int(inputlines[0].split()[-1])
B0 = int(inputlines[1].split()[-1])

print('A0 =',A0)
print('B0 =',B0)
print

p = pow(2,31)-1
mask = pow(2,16)-1

print(p,mask)

factorA = 16807
factorB = 48271

maskA = 4-1
maskB = 8-1

a = A0
b = B0

if args.part == 1:
    print('Solving part 1 only')
    match = 0
    for i in range(40000000):
        a = a*factorA % p
        b = b*factorB % p
        if (a & mask == b & mask):
            match += 1
            print(i,match)
    print('Solution:',match)
    
if args.part == 2:
    print('Solving part 2 only')
    match = 0
    pairs = 0

    while pairs < 5000000:
        a = a*factorA % p
        while (a & maskA):
            a = a*factorA % p
            
        b = b*factorB % p
        while (b & maskB):
            b = b*factorB % p

        pairs += 1
        if (a & mask == b & mask):
            match += 1
            print(pairs,match)

    print('Solution:',match)
