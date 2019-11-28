#
# Advent of Code 2017
# Bryan Clair
#
# Day 4
#
import sys

def isvalid(line):
    seen = {}
    for word in line.split():
        if word in seen:
            return False
        seen[word] = True
    return True

def isvalid_anagram(line):
    seen = {}
    for word in line.split():
        worda = ''.join(sorted(list(word)))
        if worda in seen:
            return False
        seen[worda] = True
    return True
    
if __name__ == "__main__":
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    data = open(filename).readlines()

    valid = [0,0]
    for line in data:
        s = ''
        if isvalid(line):
            valid[0] += 1
            s += 'V='
        else:
            s += 'I='
        if isvalid_anagram(line):
            valid[1] += 1
            s += ' Va'
        else:
            s += ' Ia'
        print s,line.strip()

    print "Total valid:",valid[0]
    print "Total valid (anagrammed):",valid[1]
