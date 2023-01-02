#
# Advent of Code 2017
# Bryan Clair
#
# Day 23
#
import sys
sys.path.append('../../Advent 2022')
from aocutils import *

args = parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

class Fault(Exception):
    pass

class Block(Exception):
    pass

class Send(Exception):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)
    
class Machine:
    def __init__(self,program, registers = []):
        self.registers = {}
        self.pc = 0
        self.program = program
        self.input = []
        for r in registers:
            self.registers[r] = 0

        self.mulcount = 0

    def receive(self, val):
        self.input.append(val)
        
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

        # Messages
        if inst == 'snd':
            self.sendcount += 1
            raise Send(self.val(ops))
        
        if inst == 'rcv':
            assert(ops.isalpha())
            if self.input:
                self.registers[ops] = self.input.pop(0)
                return
            self.pc -= 1
            raise Block()

        # Jumps
        if inst[0] == 'j':
            X,Y = [self.val(op) for op in ops.split()]
            if inst == 'jgz':
                test = (X > 0)
            elif inst == 'jnz':
                test = (X != 0)
            else:
                raise Fault("Bad jump: "+inst)
            
            if test:
                self.pc = self.pc - 1 + Y

            return

        # Arithmetic
        op1,op2 = ops.split()
        assert(op1.isalpha())
        X = self.val(op1)
        Y = self.val(op2)
        if inst == 'set':
            result = Y
        elif inst == 'add':
            result = X + Y
        elif inst == 'sub':
            result = X - Y
        elif inst == 'mul':
            result = X * Y
            self.mulcount += 1
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
    
m = Machine(inputlines,registers=list('abcdefgh'))

try:
    while True:
        m.step()
except Fault:
    print('part 1:', m.mulcount)

m = Machine(inputlines,registers=list('abcdefgh'))
m.registers['a'] = 1
while True:
    print(m.program[m.pc])
    m.step()
    print(m)
    print()
    input()
