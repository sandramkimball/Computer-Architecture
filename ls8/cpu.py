"""CPU functionality."""

import sys

LDI  = 1 
PRN  = 2 
HLT  = 3 
MUL  = 4
# PUSH = 4
# POP  = 5

class CPU:
    def __init__(self):
        self.ram = [0] * 256
        self.reg = [0] * 8 
        self.pc = 0
        self.running = True
        self.SP = 7 # stndrd 8th register?? F4??
        self.branchtable = {}
        self.branchtable[OP1] = self.fhandle_op1
        self.branchtable[OP2] = self.fhandle_op2
        # self.fl = 
        # self.ie = 
        # self.op = 

    def load(self, filename):
        """Load a program into memory."""
        address = 0

        if len(sys.argv) != 2:
            print(f'usage: file.py {filename}')
            sys.exit(1)
    
        try: 
            with open(filename) as f:
                for line in f:
                    # want to ignore comments
                    comment_split = line.split('#')
                    # stip out whitespace
                    num = comment.split[0].strip()
                    # ignore blank lines
                    if num == '':
                        continue
                    print(line)

                    val = int(num)
                    self.memory[address] = val
                    # self.ram[address] = val
                    address += 1

        except FileNotFoundError:
            print('File not found')
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

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

    def ram_write(MDR, MAR): 
        self.ram[MAR] = MDR
        # self.pc += 3

    def stack(self, n): 
        # starts at top address
        # vals stored in allocated ram portion
        # update SP
        if n <= 1:
            return 1
        return n * factorial(n-1)

    def handle_op1(self, a):
        print('op 1: ' + a)

    def handle_opb(self, b):
        print('op 2: ' + b)

    def pop(self):
        reg = memory[pc + 1]
        val = register[reg]
        # copy val from address to memory
        regiter[reg] = val
        pc += 0

    def push(self):
        reg = memory[pc + 1]
        val = register[reg]
        # decrement SP
        register[SP] = (register[SP] - 1) % (len(memory))
        # copy val from stack
        memory[register[SP]] = valpc += 2

    def run(self):
        # if/elif = O(n) || if not, O(1)
        # read address in pc
        # store result in IR (Instruction Register)
        if command == LDI: 
            # load immediate
            # store val in rgstr
            # set register to:
            # not always a num
            address = register[pc + 1]
            val = register[pc + 2]
            self.ram_write(address)

        elif command ==  PRN:
            # prints num value in rgstr
            address = register[pc + 1]
            target = self.ram_read(address)
            print(target)

        elif command ==  HLT:
            running = False
            sys.exit(1)

        ir = OP1
        self.branchtable[ir]('foo')
        
        ir = OP2
        self.branchtable[ir]('bar')

    
