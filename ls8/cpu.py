"""CPU functionality."""

import sys

LDI  = 1 
PRN  = 2 
HLT  = 3 
PUSH = 4
POP  = 5
CALL = 6
RET  = 7
INT  = 8
IRET = 9   
MUL  = 10

class CPU:
    def __init__(self):
        self.ram = [0] * 256
        self.reg = [0] * 8 
        self.pc = 0 # Program Counter
        self.running = True # flag
        self.FL = E # flag: L, G, E for CMP operands
        self.SP = 7 # Stack Pointer F4??
        self.IR = # Instruction Reg - copy of curr excting instr
        self.MAR = # Memry Address Reg - holds address
        self.MDR = # Memry Data Reg - holds value
        self.branchtable = {}
        self.branchtable[OP1] = self.fhandle_op1
        self.branchtable[OP2] = self.fhandle_op2
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
        self.pc += 2

    def ram_write(MDR, MAR): 
        self.ram[MAR] = MDR
        self.pc += 3

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
        # pc += 0?
        pc += 2

    def push(self):
        reg = memory[pc + 1]
        val = register[reg]
        # decrement SP
        register[SP] = (register[SP] - 1) % (len(memory))
        # copy val from stack
        memory[register[SP]] = val
        pc += 2

    def run(self):
        # if/elif = O(n) || O(1)
        # read address in pc
        # store result in IR (Instruction Register)
        if command == LDI: 
            # load immediate
            # store val in rgstr
            # set register to, not always a num
            address = register[pc + 1]
            val = register[pc + 2]
            self.ram_write(address)
            pc += 2

        elif command ==  PRN:
            # prints num value in rgstr
            address = register[pc + 1]
            target = self.ram_read(address)
            print(target)
            pc += 2

        elif command ==  HLT:
            running = False
            pc += 1

        elif commant == MUL:
            self.alu(MUL, reg_a, reg_b)
            # self.reg[reg_a] *= self.reg[reg_b]

        elif command ==  CALL:
            # decrement SP
            register[SP] -= 1
            memory[SP] = pc + 2
            # store the instruction
            reg = memory[pc + 1]

        elif command ==  RET:
            # return 
            pc = memory[register[SP]]
            register[SP] += 1

        elif command ==  INT:
            # Interrupt - issues intrrpt num stored in given reg
            # sets _n_th bit in IS reg to val in given reg
            # int_num = reg[num]
            # IS_reg[n] = int_num
            # return int_num

            # # IM register bitwise AND-ed with IS reg and result stored as:
            # maskedInterrupts = []
            # maskedInterrupts.push(IM_reg[bit])
            # # check each bit, 0-7
            # for range (0, len(maskedInterrupts)-1):
            #     if bit is set:
            #         #stop interrupts and clear bit from IS
            #         IS_reg[bit] = IS_reg[bit + 1]
            #         stack.push(PC)
            #         stack.push(FL)
            #         stack.push(IM_reg)
            #         return bit

        elif command ==  IRET:
            # return from an interrupt handler
            # regs R6-R0, then FL are poppd off stack
            # reg = memoery[pc + 1]
            # popped_reg = self.pop(stack[reg])
            # popped_FL = self.pop(stack[FL])
            # #  return addrss popped and stored in PC
            # address = register[pc + 1]
            # self.pop(stack[address])
            # pc = register[address]
            #  Interrpts are re-enbled

        else:
            print(f'Unknown command: {command}')
            sys.exit(1)

        pc += 1

ir = OP1
self.branchtable[ir]('foo')

ir = OP2
self.branchtable[ir]('bar')
