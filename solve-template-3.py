#
# Advent of Code 2017
# Bryan Clair
#
# Day --
#

# Picking up again some years later, switching to Python3
import sys
sys.path.append('../../Advent 2022')
from aocutils import *

args = parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

for line in inputlines:
    print(line)
    
