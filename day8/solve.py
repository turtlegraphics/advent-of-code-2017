#
# Advent of Code 2017
# Bryan Clair
#
# Day 8
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

registers = {}

high = 0

for line in inputlines:
    reg,op,val,keyword,treg,comp,tval = line.split()
    op = '+' if op=='inc' else '-'
    if reg not in registers:
        registers[reg] = 0
    if treg not in registers:
        registers[treg] = 0
    code = "if registers['%s'] %s %s:\n   registers['%s'] %s= %s" % (treg,comp,tval,reg,op,val)
    exec(code)

    m = max(registers.values())
    if m > high:
        high = m

print 'part 1:', m
print 'part 2:', high
