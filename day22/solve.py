#
# Advent of Code 2017
# Bryan Clair
#
# Day 22
#

# Picking up again some years later, switching to Python3
import sys
sys.path.append('../../Advent 2022')
from aocutils import *

args = parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

class Carrier:
    def __init__(self):
        self.p = Turtle(x = grid.width()//2, y = grid.height()//2)
        self.p.face('N')
        self.icount = 0
        
    def infect(self,cur):
        if cur == '#':
            self.p.right()
            grid[self.p] = '.'
        else:
            assert(cur == '.')
            self.p.left()
            grid[self.p] = '#'
            self.icount += 1
            
    def burst(self):
        try:
            cur = grid[self.p]
        except KeyError:
            grid[self.p] = '.'
            cur = '.'

        self.infect(cur)
        
        self.p.forward(1)

class Carrier2(Carrier):
    def infect(self,cur):
        if cur == '#':
            grid[self.p] = 'F'
            self.p.right()
        elif cur == 'W':
            grid[self.p] = '#'
            self.icount += 1        
        elif cur == 'F':
            grid[self.p] = '.'
            self.p.right()
            self.p.right()
        else:
            assert(cur == '.')
            grid[self.p] = 'W'
            self.p.left()

grid = Grid()
grid.scan(inputlines)

c = Carrier()
for i in range(10000):
    c.burst()

print('part 1:',c.icount)


grid = Grid()
grid.scan(inputlines)
c = Carrier2()

from tqdm import tqdm

for i in tqdm(range(10000000)):
    c.burst()

print('part 2:',c.icount)

