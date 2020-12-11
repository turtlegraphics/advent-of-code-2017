#
# Advent of Code 2017
# Bryan Clair
#
# knothash
#
class Rope:
    def __init__(self,n):
        self.n = n
        self.pos = 0
        self.skip = 0
        self.rope = range(n)

    def __str__(self):
        out = ''
        for i in range(self.n):
            if self.pos == i:
                out += '[%d] ' % self.rope[i]
            else:
                out += '%d ' % self.rope[i]
        return out.strip()

    def round(self, lengths):
        for l in lengths:
            head = self.pos
            tail = (self.pos + l - 1) % self.n
            swaps = l//2
            while swaps > 0:
                temp = self.rope[head]
                self.rope[head] = self.rope[tail]
                self.rope[tail] = temp
                swaps -= 1
                head = (head + 1) % self.n
                tail = (tail - 1) % self.n
            self.pos = (self.pos + l + self.skip) % self.n
            self.skip += 1

    def dense(self):
        hash = ''
        for block in range(16):
            combo = 0
            for i in range(16):
                combo ^= self.rope[16*block + i]
            hash += "%x" % combo
        return hash

def knothash(text):
    lengths = [ord(x) for x in text] + [17, 31, 73, 47, 23]
    r = Rope(256)
    for t in range(64):
        r.round(lengths)
    return r.dense()

if __name__ == '__main__':
    day10 = '97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190'
    print knothash(day10)
    assert(knothash(day10) == 'aff593797989d665349efe11bb4fd99b')
