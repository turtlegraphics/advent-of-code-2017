#
# Advent of Code 2017
# Bryan Clair
#
# Day 5
#
import argparse

def show(inst,ip):
    if args.verbose <= 1:
        return
    out = ''
    for i in range(len(inst)):
        if i == ip:
            out += '('+str(inst[i])+')'
        else:
            out += ' '+str(inst[i])+' '
    print out

def run(inst):
    ip = 0
    step = 0
    try:
        while True:
            show(inst,ip)

            # Calculuate next step
            next = ip + inst[ip]

            # Adjust offset
            if args.part == 1:
                inst[ip] += 1
            else:
                if inst[ip] >= 3:
                    inst[ip] -= 1
                else:
                    inst[ip] += 1

            # Take next step
            ip = next
            step += 1
            if (step % 1000000 == 0) and (args.verbose > 0):
                print 'Step',step

    except IndexError:
        print 'Exit reached in',step,'steps.'

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

    inst = []
    for line in data:
        inst.append(int(line))

    run(inst)
    
