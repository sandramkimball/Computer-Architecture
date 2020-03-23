"""CPU functionality."""

import sys

class CPU:
    def __init__(self):
        memory = [0] * 256
        register = [0] * 8 
        pc = 0
        running = True

    def load(self):
        """Load a program into memory."""
        
        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    # MAR: Memory Address Register
    # MDR: Memory Data Register
    def ram_read(MAR):
        target = MAR[pc + 1]
        pc += 2
        return target

    def ram_write(MDR, MAR): 
        reg_a = MAR[pc + 1]
        reg_b = MAR[pc + 2]
        register[reg_a] += register[reg_b]
        # register[reg_a] += MDR ??
        pc += 3

    def run(self):
        # read address in pc
        # store result in IR (Instruction Register)
        if command == LDI:
            # load immediate
            # store val in rgstr
            # set register to:
            # not always a num

        elif command ==  PRN:
            # pseudo-instruction, 
            # prints num value in rgstr

        elif command ==  HLT:
            running = False
            sys.exit(1)

LDI = 1 
PRN = 2 
HLT = 3 