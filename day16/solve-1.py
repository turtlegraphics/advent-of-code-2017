#
# Advent of Code 2017
# Bryan Clair
#
# Day 16
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

dance_moves = inputlines[0].split(',')


class Dance:
    def __init__(self,progs):
        self.progs = progs

    def __str__(self):
        return ''.join(self.progs)

    def spin(self,size):
        self.progs = self.progs[-size:] + self.progs[:-size]

    def exchange(self,x,y):
        temp = self.progs[x]
        self.progs[x] = self.progs[y]
        self.progs[y] = temp

    def partner(self,a,b):
        x = self.progs.index(a)
        y = self.progs.index(b)
        self.exchange(x,y)

    def do_move(self,move):
        if move[:1] == 's':
            size = int(move[1:])
            # print('spin',size)
            self.spin(size)
        elif move[:1] == 'x':
            where = [int(x) for x in move[1:].split('/')]
            # print('exchange',where[0],where[1])
            self.exchange(where[0],where[1])
        elif move[:1] == 'p':
            who = move[1:].split('/')
            # print('partner',who[0],who[1])
            self.partner(who[0],who[1])

dancers = 'abcdefghijklmnop'
d = Dance(list(dancers))
for move in dance_moves:
    d.do_move(move)
    
print('Part 1:',d)



    
