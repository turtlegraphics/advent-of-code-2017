#
# Advent of Code 2017
# Bryan Clair
#
# Day 19
#

# Picking up again some years later, switching to Python3

import sys
sys.path.append('../../Advent 2022')
from aocutils import *

args = parse_args()

inputlines = [x.strip('\n') for x in open(args.file).readlines()]

maze = Grid()
maze.scan(inputlines)

pos = Point(inputlines[0].find('|'), len(inputlines)-1)
dir = Point(0,-1)

steps = 0
path = ''

spot = maze[pos]
while spot != ' ':
    pos += dir
    steps += 1
    spot = maze[pos]
    if spot == '+':
        dir = Point(dir.y,dir.x)
        look = maze[pos + dir]
        if look == ' ':
            dir *= -1
    if spot.isalpha():
        path += spot
        
print('part 1:',path)
print('part 2:',steps)
