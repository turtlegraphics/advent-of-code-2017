#
# Advent of Code 2019
# Bryan Clair
#
# Day --
#
import sys

def check(line):
    v = [int(s) for s in line.split()]
    for i in range(len(v)):
        for j in range(len(v)):
            
            if (i != j) and (v[i] % v[j] == 0):
                # print v[i],v[j]
                return v[i]/v[j]

if __name__ == "__main__":
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    data = open(filename).readlines()

    sum = 0
    for line in data:
        sum += check(line)
    print sum
