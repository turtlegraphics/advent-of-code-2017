#
# Advent of Code 2017
# Bryan Clair
#
# Day 6
#
import argparse

def cycle(banks):
    b = max(banks)
    target = banks.index(b)
    banks[target] = 0
    while b > 0:
        target = (target + 1) % len(banks)
        banks[target] += 1
        b -= 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
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

    data = open(args.file).readlines()

    banks = []
    for line in data:
        banks.extend([int(x) for x in line.split()])

    seen = {}
    step = 0
    while tuple(banks) not in seen:
        seen[tuple(banks)] = step
        step += 1
        cycle(banks)
        if args.verbose > 1:
            print step, banks

    print '(Part I) Step:', step
    print '(Part II) Loop length:', step - seen[tuple(banks)]
