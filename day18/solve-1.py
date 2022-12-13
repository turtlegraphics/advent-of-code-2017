#
# Advent of Code 2017
# Bryan Clair
#
# Day 18
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

class Fault(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
    
class Machine:
    def __init__(self,program):
        self.registers = {}
        self.pc = 0
        self.program = program
        self.sound = None
        
    def val(self,operand):
        if operand.isalpha():
            try:
                return self.registers[operand]
            except KeyError:
                self.registers[operand] = 0
                return 0
        else:
            return int(operand)
        
    def step(self):
        try:
            line = self.program[self.pc]
            self.pc += 1
        except IndexError:
            raise Fault("Program terminated")
        
        inst, ops = line.split(maxsplit=1)
        
        if inst == 'snd':
            self.sound = self.val(ops)
            return
        
        if inst == 'rcv':
            if self.val(ops):
                raise Fault("Recovered: " + str(self.sound))
            return
        
        if inst == 'jgz':
            X,Y = [self.val(op) for op in ops.split()]
            if X > 0:
                self.pc = self.pc - 1 + Y
            return

        op1,op2 = ops.split()
        assert(op1.isalpha())
        X = self.val(op1)
        Y = self.val(op2)
        if inst == 'set':
            result = Y
        elif inst == 'add':
            result = X + Y
        elif inst == 'mul':
            result = X * Y
        elif inst == 'mod':
            result = X % Y
        else:
            raise Fault("Bad operation: " + op1)
        
        self.registers[op1] = result

    def __str__(self):
        out = '-----\n'
        out += 'pc: ' + str(self.pc) + '\n'
        for reg in self.registers:
            out += reg + ': ' + str(self.registers[reg]) + '\n'
        return out
    
m = Machine(inputlines)

try:
    while True:
        m.step()
            
except Fault as e:
    print(e.msg)
    
print(m)
