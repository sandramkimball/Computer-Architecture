"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010 
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET  = 0b00010001
LD   = 0b10000011
ST   = 0b10000100
PRA  = 0b01001000


class CPU:
    def __init__(self):
        self.ram = [0] * 256
        self.reg = [0] * 8 
        self.pc = 0 # Program Counter
        self.SP = 0xF4 # Stack Pointer
        # self.reg[self.SP] = 0xF3
        # self.MAR = # Memry Address Reg - holds address
        # self.MDR = # Memry Data Reg - holds value
        # self.branchtable = {}
        # self.branchtable[OP1] = self.fhandle_op1
        # self.branchtable[OP2] = self.fhandle_op2
        # self.FL = E # flag: L, G, E for CMP operands

    def load(self): 
        """Load a program into memory."""
        address = 0
        program = sys.argv[1]
        # program = 'ls8\examples\call.ls8'

        if len(sys.argv) != 2:
            print(f'usage: file.py {program}')
            sys.exit(1)
    
        try: 
            with open(program) as f:
                count = 0
                for line in f:
                    count += 1
                    # ignore comments
                    comment_split = line.split('#')
                    # strip out whitespace
                    num = comment.split[0].strip()
                    # ignore blank lines
                    if num == '':
                        continue

                    try:
                        val = int(num, 2)
                    except ValyeError:
                        continue

                    self.ram[address] = val
                    address += 1

        except FileNotFoundError:
            print('File not found')
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]

        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]

        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]

        elif op == "DIV":
            self.reg[reg_a] /= self.reg[reg_b]

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

    def ram_read(MAR):
        return self.ram[MAR]
        # self.pc += 2

    def ram_write(MAR, MDR): 
        self.ram[MAR] = MDR
        # self.pc += 3

    def run(self):
        # if/elif = O(n) || O(1)
        # read address in pc, store result in IR (Instruction Register)
        running = True
        while running is True:
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1) #address = register[pc + 1]
            operand_b = self.ram_read(self.pc + 2)

            # HLT
            if IR == 0b00000001: 
                running = False
                self.pc += 1

            # LDI
            elif IR == 0b10000010: 
                # load immediate, store val in reg
                self.reg[operand_a] = operand_b
                self.pc += 3

            # PRN
            elif IR == 0b01000111:
                # prints num value in rgstr
                print(self.reg[operand_a])
                self.pc += 2
 
            # MUL
            elif IR == 0b10100010:
                self.alu(MUL, reg_a, reg_b)
                # self.reg[reg_a] *= self.reg[reg_b]

            # PUSH
            elif IR == 0b01000101:
                # Copy val from address to given reg
                # decrement SP
                self.ram[self.SP] = self.reg[operand_a]
                self.SP -= 1
                self.pc += 2

            # POP
            elif IR == 0b01000110:
                # copy val from address
                # increment SP
                self.reg[operand_a] = self.ram[self.SP]
                self.SP += 1
                self.pc += 2

            # CALL
            elif IR == 0b01010000:
                # decrement SP
                register[SP] -= 1
                memory[SP] = pc + 2
                # store the instruction
                reg = memory[pc + 1]

            # RET
            elif IR == 0b00010001:
                # pop val from stack and return 
                self.pc = memory[register[SP]]
                register[SP] += 1

            # ADD
            elif IR == ADD:
                # pop val from stack and store in PC
                self.reg[operand_a] += self.reg[operands_b]
                self.pc += 3

            else:
                print(f'Unknown command: {command}')
                sys.exit(1)
    
    
    # def stack(self, n): 
    #     # starts at top address
    #     # vals stored in allocated ram portion
    #     # update SP
    #     if n <= 1:
    #         return 1
    #     return n * factorial(n-1)

    # def pop(self):
    #     reg = memory[pc + 1]
    #     val = register[reg]
    #     # copy val from address to memory
    #     register[reg] = val
    #     # pc += 0?
    #     self.pc += 2

    # def push(self):
    #     reg = memory[pc + 1]
    #     val = register[reg]
    #     # decrement SP
    #     register[self.SP] = (register[self.SP] - 1) % (len(memory))
    #     # copy val from stack
    #     memory[register[self.SP]] = val
    #     pc += 2
# self.SP is register[SP]