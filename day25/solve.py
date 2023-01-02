#
# Advent of Code 2017
# Bryan Clair
#
# Day 25
#

# Picking up again some years later, switching to Python3
import sys
sys.path.append('../../Advent 2022')
from aocutils import *

args = parse_args()

intxt = open(args.file).read()
chunks = intxt.split('\n\n')

start = chunks[0].split()[3][0]
runtime = int(chunks[0].split()[9])

rules = {}
for r in chunks[1:]:
    lines = r.split('\n')
    instate = lines[0].split()[2][0]
    rule = []
    for i in [0,1]:
        writeval = int(lines[2+4*i].split()[4][0])
        movedir = lines[3+4*i].split()[6][0]
        movedir = 1 if movedir == 'r' else -1
        nextstate = lines[4+4*i].split()[4][0]
        rule.append((writeval, movedir, nextstate))

    rules[instate] = rule

class Machine:
    def __init__(self,start,rules):
        self.rules = rules
        self.state = start
        self.pos = 0
        self.tape = {self.pos : 0}
        self.maxp = 0
        self.minp = 0
        
    def step(self):
        rule = self.rules[self.state][self.tape[self.pos]]
        writeval, movedir, nextstate = rule
        self.tape[self.pos] = writeval
        self.state = nextstate
        self.pos += movedir

        if self.pos not in self.tape:
            self.tape[self.pos] = 0

        if self.pos > self.maxp:
            self.maxp = self.pos
        if self.pos < self.minp:
            self.minp = self.pos

    def checksum(self):
        count = 0
        for i in self.tape:
            count += self.tape[i]
        return count
    
    def __str__(self):
        out = ''
        for i in range(self.minp,self.maxp+1):
            if i == self.pos:
                out += '['
            out += str(self.tape[i])
            if i == self.pos:
                out += ']'

        return(out)

m = Machine(start,rules)
for i in tqdm(range(runtime)):
    m.step()

print('part 1:',m.checksum())
