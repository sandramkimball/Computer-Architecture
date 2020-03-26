import sys

PRINT_BEES      = 1
HALT            = 2
PRINT_NUM       = 3
SAVE            = 4
PRINT_REGISTER  = 5
ADD             = 6 
PUSH            = 7
POP             = 8
CALL            = 9
RET             = 10

memory = [None] * 256
register = [0] * 8 # xtrmly fast, small data grps(a word), NOT MEMORY 
cache #lil slower yet bigger than rgstr
filename = sys.argv[1]
SP = 7 # R7 is reserved as SP
pc = 0 # program counter that points to memory address
running = True # just a flag 


# PART 1
# example hardcoded memory:
memory = [
    PRINT_BEES,
    SAVE,
    65, 
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT
] 


while running: #this is the processor
    command = memory[pc]
    # print(memory)
    # print(register)
    print(pc)
    print('------')

    if command = PRINT_BEES:
        print('Bees!')
        pc += 1

    elif command == HALT:
        running = False
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc+1] 
        print(num)
        pc += 2

    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2

    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3

    elif command == PUSH:
        reg = memory[pc + 1]
        val = register[reg]
        #decrement the stack pointer (SP)
        register[SP] = (register[SP] - 1) % (len(memory))
        #copy value from stack at given reg to the address
        memory[register[SP]] = val
        pc += 2 # 2 because we had 1 arg

    elif command == POP:
        reg = memory[pc + 1]
        val = memory[register[SP]]
       # copy value from address to the memory
       register[reg] = val
       # increment SP
       register[SP] += 1
       pc += 2

    elif command == CALL:
        # decrement SP
        register[SP] -= 1
        memory[register[SP]] = pc + 2 # 2=memory directly after call
        # store the instruction
        reg = memory[pc + 1] #where register is at, address pointed to
        pc = register[reg]
        # why not use PUSH? It's not a function you can call, its hardware


    elif command == RET:
        pc = memory[register[SP]]
        register[SP] += 1
        

    else: 
        print(f'Unknown command: {command}')
        sys.exit(1)

    pc += 1


# PART 2
def factorial(n): # O(n)
    if n <= 1: # base case (without recursion, stack overflow happens)
        return 1
    return n * factorial(n-1) # pop it off the stack

def tailOptimizedFactorial(n):# O(1)
    total = 1
    for i in range(1, n + 1):
        total += 1
    return total
    
# print factorial(5)
# print tailOptimizedFactorial(5)

# STUDY:
# conversions between binary, hex, decimal
# bitwise ops, logical ops
# whate are computer components? processor(cpu, alu), memory, registers, bus
# what's an interupt?
# what is a stack, how it works, what's used for?
# what is the ls-8, how does it work, implement ops?
# Can register set variables? Registers have limited space, so use a stack: vars stored at the top, "we don't need this var/cmmnd anymore", POP! POP! POP! POP!... and back to the return!