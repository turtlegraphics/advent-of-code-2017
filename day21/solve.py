#
# Advent of Code 2017
# Bryan Clair
#
# Day 21
#

# Picking up again some years later, switching to Python3
import sys
sys.path.append('../../Advent 2022')
from aocutils import *

args = parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

rules2 = []

def transform(m):
    """Generate rotations and transformations of m"""
    a = m.split()
    n = len(a)

    # build the dihedral group
    id = lambda x,y : (x,y)
    f1 = lambda x,y : (x,n-1-y)
    f2 = lambda x,y : (y,x)
    D4 = [id,f1,f2]
    D4.append(lambda x,y : f1(*f2(x,y)))
    D4.append(lambda x,y : f2(*f1(x,y)))
    D4.append(lambda x,y : f2(*f1(*f2(x,y))))
    D4.append(lambda x,y : f1(*f2(*f1(x,y))))
    D4.append(lambda x,y : f2(*f1(*f2(*f1(x,y)))))

    forms = []
    for t in D4:
        tm = ''
        for x in range(n):
            for y in range(n):
                tx,ty = t(x,y)
                tm += a[tx][ty]
            tm += '\n'
        forms.append(tm)
    return forms

rules = {}

for line in inputlines:
    m, r = line.split(' => ')
    m = m.replace('/','\n')
    forms = transform(m)
    result = Grid()
    result.scan(r.split('/'))
    for f in forms:
        rules[f] = result

def evolve(grid):
    dim = grid.width()
    if dim % 2 == 0:
        n = 2
    else:
        assert(dim % 3 == 0)
        n = 3
    np = n+1
    
    newgrid = Grid()
    
    for sx in range(dim // n):
        for sy in range(dim // n):
            # handle square sx,sy
            m = ''
            for x in range(n):
                for y in range(n):
                    m += grid[x+n*sx,y+n*sy]
                m += '\n'
            replace = rules[m]

            for x in range(np):
                for y in range(np):
                    newgrid[x+np*sx,y+np*sy] = replace[x,y]

    return newgrid

def count(grid):
    c = 0
    for g in grid:
        if grid[g] == '#':
            c += 1
    return c

grid = Grid()
grid.scan(['.#.','..#','###'])
for iteration in range(18):
    grid = evolve(grid)
    if iteration == 4:
        print('part 1:',count(grid))

print('part 2:',count(grid))
